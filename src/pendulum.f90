function f1(theta1,theta2,p1,p2,l1,l2,m1,m2)
    implicit none
    real*8::theta1,theta2,p1,p2,l1,l2,m1,m2,f1
    f1=(p1*l2-p2*l1*cos(theta1-theta2))/(l1*l1*l2*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2)))
end function f1

function f2(theta1,theta2,p1,p2,l1,l2,m1,m2)
    implicit none
    real*8::theta1,theta2,p1,p2,l1,l2,m1,m2,f2
    f2=(p2*(m1+m2)*l1-p1*m2*l2*cos(theta1-theta2))/(m2*l1*l2*l2*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2)))
end function f2
function f3(theta1,theta2,p1,p2,l1,l2,m1,m2)
    implicit none
    real*8::theta1,theta2,p1,p2,l1,l2,m1,m2,f3,g,a1,a2,a3
    g=9.8
    a1=(p1*p2*sin(theta1-theta2))/(l1*l2*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2)))
    a3=1/(2*l1*l1*l2*l2*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2))*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2)))
    a2=a3*(p1*p1*m2*l2*l2-2*p1*p2*m2*l1*l2*cos(theta1-theta2)+p2*p2*(m1+m2)*l1*l1)*sin(2*(theta1-theta2))
    f3=-(m1+m2)*g*l1*sin(theta1)-a1+a2
end function f3

function f4(theta1,theta2,p1,p2,l1,l2,m1,m2)
    implicit none
    real*8::theta1,theta2,p1,p2,l1,l2,m1,m2,f4,g,a1,a2,a3
    g=9.8
    a1=(p1*p2*sin(theta1-theta2))/(l1*l2*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2)))
    a3=1/(2*l1*l1*l2*l2*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2))*(m1+m2*sin(theta1-theta2)*sin(theta1-theta2)))
    a2=a3*(p1*p1*m2*l2*l2-2*p1*p2*m2*l1*l2*cos(theta1-theta2)+p2*p2*(m1+m2)*l1*l1)*sin(2*(theta1-theta2))
    f4=-m2*g*l2*sin(theta2)+a1-a2
end function f4

real*8 function euler_theta1(theta1,theta2,v1,v2,step,L1,L2,m1,m2)
    implicit none
    real*8::theta1,theta2,v1,v2,L1,L2,m1,m2,step,delta
    real*8,external::f1
    delta=theta1+step*f1(theta1,theta2,v1,v2,L1,L2,m1,m2)
    euler_theta1=theta1+step/2*(f1(theta1,theta2,v1,v2,L1,L2,m1,m2)+f1(delta,theta2,v1,v2,L1,L2,m1,m2))
    return
end function euler_theta1

real*8 function euler_theta2(theta1,theta2,v1,v2,step,L1,L2,m1,m2)
    implicit none
    real*8::theta1,theta2,v1,v2,L1,L2,m1,m2,step,delta
    real*8,external::f2
    delta=theta2+step*f2(theta1,theta2,v1,v2,L1,L2,m1,m2)
    euler_theta2=theta2+step/2*(f2(theta1,theta2,v1,v2,L1,L2,m1,m2)+f2(theta1,delta,v1,v2,L1,L2,m1,m2))
    return
end function euler_theta2

real*8 function euler_v1(theta1,theta2,v1,v2,step,L1,L2,m1,m2)
    implicit none
    real*8::theta1,theta2,v1,v2,L1,L2,m1,m2,step,g,delta
    real*8,external::f3
    g=9.8
    delta=v1+step*f3(theta1,theta2,v1,v2,L1,L2,m1,m2)
    euler_v1=v1+step/2*(f3(theta1,theta2,v1,v2,L1,L2,m1,m2)+f3(theta1,theta2,delta,v2,L1,L2,m1,m2))
    return
end function euler_v1

real*8 function euler_v2(theta1,theta2,v1,v2,step,L1,L2,m1,m2)
    implicit none
    real*8::theta1,theta2,v1,v2,L1,L2,m1,m2,step,g,delta
    real*8,external::f4
    g=9.8
    delta=v2+step*f4(theta1,theta2,v1,v2,L1,L2,m1,m2)
    euler_v2=v2+step/2*(f4(theta1,theta2,v1,v2,L1,L2,m1,m2)+f4(theta1,theta2,v1,delta,L1,L2,m1,m2))
    return
end function euler_v2