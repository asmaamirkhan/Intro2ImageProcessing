#-------------------------------------------------
#
# Project created by QtCreator 2019-07-12T09:38:28
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Detection
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui


####################################################
CONFIG += c++11
DEFINES += QT_DEPRECATED_WARNINGS

INCLUDEPATH += C:\esma\opencv\build\include

LIBS += C:\esma\opencv\build\bin\libopencv_core401.dll
LIBS += C:\esma\opencv\build\bin\libopencv_features2d401.dll
LIBS += C:\esma\opencv\build\bin\libopencv_highgui401.dll
LIBS += C:\esma\opencv\build\bin\libopencv_imgcodecs401.dll
LIBS += C:\esma\opencv\build\bin\libopencv_imgproc401.dll
LIBS += C:\esma\opencv\build\bin\libopencv_calib3d401.dll
LIBS += C:\esma\opencv\build\bin\libopencv_objdetect401.dll
