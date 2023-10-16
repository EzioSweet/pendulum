
from matplotlib import figure
import pendulum as pdm
import numpy as np
from PySide2.QtCore import QRect,QMetaObject,QCoreApplication,Slot
from PySide2.QtWidgets import QCheckBox, QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton,QApplication,QMainWindow,QStatusBar
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qtcairo import FigureCanvasQTCairo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(530, 10, 171, 366))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.fig = plt.figure()
        self.canvasCairo = FigureCanvasQTCairo(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim((-3,3))
        self.ax.set_ylim((-3,3))
        self.canvasLayout = QVBoxLayout()
        self.canvasLayout.addWidget(self.canvasCairo) 
        self.ani=None
        self.canvas = QWidget(self.centralwidget)
        self.canvas.setObjectName(u"canvas")
        self.canvas.setGeometry(QRect(10, 10, 501, 431))
        self.canvas.setLayout(self.canvasLayout)

        self.verticalLayout.addWidget(self.label)

        self.m1line = QLineEdit(self.verticalLayoutWidget)
        self.m1line.setObjectName(u"m1line")

        self.verticalLayout.addWidget(self.m1line)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.m2line = QLineEdit(self.verticalLayoutWidget)
        self.m2line.setObjectName(u"m2line")

        self.verticalLayout.addWidget(self.m2line)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.l1line = QLineEdit(self.verticalLayoutWidget)
        self.l1line.setObjectName(u"l1line")

        self.verticalLayout.addWidget(self.l1line)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.l2line = QLineEdit(self.verticalLayoutWidget)
        self.l2line.setObjectName(u"l2line")

        self.verticalLayout.addWidget(self.l2line)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.theta1line = QLineEdit(self.verticalLayoutWidget)
        self.theta1line.setObjectName(u"theta1line")

        self.verticalLayout.addWidget(self.theta1line)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.theta2line = QLineEdit(self.verticalLayoutWidget)
        self.theta2line.setObjectName(u"theta2line")

        self.verticalLayout.addWidget(self.theta2line)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.step = QLineEdit(self.verticalLayoutWidget)
        self.step.setObjectName(u"step")

        self.verticalLayout.addWidget(self.step)

        self.check = QCheckBox(self.centralwidget)
        self.check.setObjectName(u"check")
        self.check.setGeometry(530,380,70,41)

        self.check2 = QCheckBox(self.centralwidget)
        self.check2.setObjectName(u"check2")
        self.check2.setGeometry(530,400,70,41)
        self.plot = QPushButton(self.centralwidget)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(600, 390, 100, 41))
        self.plot.clicked.connect(self.draw)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.x1=[]
        self.x2=[]
        self.y1=[]
        self.y2=[]
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PySide2+Fortran\u590d\u6446\u4eff\u771f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"m1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"m2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"l1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"l2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"theta1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"theta2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.m1line.setText("1")
        self.m2line.setText("1")
        self.l1line.setText("1")
        self.l2line.setText("1")
        self.theta1line.setText("0.33")
        self.theta2line.setText("0")
        self.step.setText("0.001")
        self.check.setText("轨迹")
        self.check2.setText("拖影")
        self.plot.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
    # retranslateUi
    @Slot()
    def draw(self):
        self.x1=[]
        self.y1=[]
        self.x2=[]
        self.y2=[]
        self.l1= float(self.l1line.text())
        self.l2= float(self.l2line.text())
        self.m1= float(self.m1line.text())
        self.m2= float(self.m2line.text())
        self.theta1=np.pi * float(self.theta1line.text())
        self.theta2=np.pi * float(self.theta2line.text())
        self.p1=0
        self.p2=0
        self.dt = float(self.step.text())
        self.line1, = self.ax.plot([], [], 'o-', lw=2)
        self.line2, = self.ax.plot([], [], 'o-', lw=2)
        self.line3, = self.ax.plot([],[],'-',lw=2)
        self.line4, = self.ax.plot([],[],'-',lw=2)
        self.t = np.arange(0, 100, self.dt)
        self.theta1_list=[]
        self.theta2_list=[]
        self.p1_list=[]
        self.p2_list=[]
        self.k1=[0,0,0,0]
        self.k2=[0,0,0,0]
        self.k3=[0,0,0,0]
        self.k4=[0,0,0,0]
        for i in self.t:
            if i==0:
                continue
            self.k1[0]=pdm.f1(self.theta1,self.theta2,self.p1,self.p2,self.l1,self.l2,self.m1,self.m2)
            self.k1[1]=pdm.f2(self.theta1,self.theta2,self.p1,self.p2,self.l1,self.l2,self.m1,self.m2)
            self.k1[2]=pdm.f3(self.theta1,self.theta2,self.p1,self.p2,self.l1,self.l2,self.m1,self.m2)
            self.k1[3]=pdm.f4(self.theta1,self.theta2,self.p1,self.p2,self.l1,self.l2,self.m1,self.m2)
            self.k2[0]=pdm.f1(self.theta1+self.dt*self.k1[0]/2,self.theta2+self.dt*self.k1[1]/2,self.p1+self.dt*self.k1[2]/2,self.p2+self.dt*self.k1[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k2[1]=pdm.f2(self.theta1+self.dt*self.k1[0]/2,self.theta2+self.dt*self.k1[1]/2,self.p1+self.dt*self.k1[2]/2,self.p2+self.dt*self.k1[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k2[2]=pdm.f3(self.theta1+self.dt*self.k1[0]/2,self.theta2+self.dt*self.k1[1]/2,self.p1+self.dt*self.k1[2]/2,self.p2+self.dt*self.k1[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k2[3]=pdm.f4(self.theta1+self.dt*self.k1[0]/2,self.theta2+self.dt*self.k1[1]/2,self.p1+self.dt*self.k1[2]/2,self.p2+self.dt*self.k1[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k3[0]=pdm.f1(self.theta1+self.dt*self.k2[0]/2,self.theta2+self.dt*self.k2[1]/2,self.p1+self.dt*self.k2[2]/2,self.p2+self.dt*self.k2[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k3[1]=pdm.f2(self.theta1+self.dt*self.k2[0]/2,self.theta2+self.dt*self.k2[1]/2,self.p1+self.dt*self.k2[2]/2,self.p2+self.dt*self.k2[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k3[2]=pdm.f3(self.theta1+self.dt*self.k2[0]/2,self.theta2+self.dt*self.k2[1]/2,self.p1+self.dt*self.k2[2]/2,self.p2+self.dt*self.k2[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k3[3]=pdm.f4(self.theta1+self.dt*self.k2[0]/2,self.theta2+self.dt*self.k2[1]/2,self.p1+self.dt*self.k2[2]/2,self.p2+self.dt*self.k2[3]/2,self.l1,self.l2,self.m1,self.m2)
            self.k4[0]=pdm.f1(self.theta1+self.dt*self.k3[0],self.theta2+self.dt*self.k3[1],self.p1+self.dt*self.k3[2],self.p2+self.dt*self.k3[3],self.l1,self.l2,self.m1,self.m2)
            self.k4[1]=pdm.f2(self.theta1+self.dt*self.k3[0],self.theta2+self.dt*self.k3[1],self.p1+self.dt*self.k3[2],self.p2+self.dt*self.k3[3],self.l1,self.l2,self.m1,self.m2)
            self.k4[2]=pdm.f3(self.theta1+self.dt*self.k3[0],self.theta2+self.dt*self.k3[1],self.p1+self.dt*self.k3[2],self.p2+self.dt*self.k3[3],self.l1,self.l2,self.m1,self.m2)
            self.k4[3]=pdm.f4(self.theta1+self.dt*self.k3[0],self.theta2+self.dt*self.k3[1],self.p1+self.dt*self.k3[2],self.p2+self.dt*self.k3[3],self.l1,self.l2,self.m1,self.m2)
            theta11=self.theta1+(self.dt/6)*(self.k1[0]+2*self.k2[0]+2*self.k3[0]+self.k4[0])
            theta22=self.theta2+(self.dt/6)*(self.k1[1]+2*self.k2[1]+2*self.k3[1]+self.k4[1])
            v11=self.p1+(self.dt/6)*(self.k1[2]+2*self.k2[2]+2*self.k3[2]+self.k4[2])
            v22=self.p2+(self.dt/6)*(self.k1[3]+2*self.k2[3]+2*self.k3[3]+self.k4[3])
            if theta11>np.pi:
                theta11-=2*np.pi
            elif theta11<-np.pi:
                theta11+=2*np.pi
            if theta22>np.pi:
                theta22-=2*np.pi
            elif theta22<-np.pi:
                theta22+=2*np.pi
            self.theta1_list.append(theta11)
            self.theta2_list.append(theta22)
            self.p1_list.append(v11)
            self.p2_list.append(v22)
            self.theta1=theta11
            self.theta2=theta22
            self.p1=v11
            self.p2=v22
        self.ax.set_xlim((-self.l1-self.l2,self.l1+self.l2))
        self.ax.set_ylim((-self.l1-self.l2,self.l1+self.l2))
        if self.ani:
            self.ani.event_source.stop()
            self.ani=None
        self.ani = FuncAnimation(self.fig, self.animate,frames=len(self.t),interval=self.dt*1000, blit=True)
    def animate(self, j):
        self.x1.append(self.l1 * np.sin(self.theta1_list[j]))
        self.y1.append(-self.l1 * np.cos(self.theta1_list[j]))
        self.x2.append(self.x1[j] + self.l2 * np.sin(self.theta2_list[j]))
        self.y2.append(self.y1[j] - self.l2 * np.cos(self.theta2_list[j]))
        self.line1.set_data([0,self.x1[j]], [0,self.y1[j]])
        self.line2.set_data([self.x1[j],self.x2[j]], [self.y1[j],self.y2[j]])
        if self.check.isChecked():
            if self.check2.isChecked():
                self.line3.set_data(self.x1[-200:],self.y1[-200:])
                self.line4.set_data(self.x2[-200:],self.y2[-200:])
            else:
                self.line3.set_data(self.x1,self.y1)
                self.line4.set_data(self.x2,self.y2)
            return self.line1,self.line2,self.line3,self.line4
        else:
            return self.line1,self.line2
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    MainWindow = QMainWindow()    
    ui = Ui_MainWindow()          
    ui.setupUi(MainWindow)  
    MainWindow.show()       
    sys.exit(app.exec_())
