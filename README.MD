# PySide2+Fortran 双摆仿真软件

## 使用说明

请确保主Python环境已安装pipenv和f2py，运行build.bat即可运行

## 注意

本项目使用的f2py使用的为mingw64-gfortran来将fortran编译静态库，如果使用ifort/ift/nvcc之类的编译器，请手动修改build.bat中的f2py相关来确保运行。