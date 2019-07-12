/*
@author: Asmaa ~ 2019
*/

#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/imgproc/imgproc.hpp>
using namespace cv;

using namespace std;

#include <QFileDialog>
#include <QString>

// function protoype
void detectFacesHaar();
void detectFacesHOG();

string LABEL = "";
string PATH="";
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    // get image path
    QString path = QFileDialog::getOpenFileName();

    // save path
    PATH = path.toStdString();
    ui->PathLabel->setText(path);
}

void MainWindow::on_HaarOprion_clicked()
{
    detectFacesHaar();

    // set label text
    ui->label->setText(QString::fromStdString(LABEL));
}

void MainWindow::on_HogOption_clicked()
{
    //TODO: implement HOG classifier
}

void detectFacesHaar(){
    vector <Rect> faces;

    // open image
    Mat image = imread(PATH,IMREAD_COLOR);
    Mat gray;

    // convert into gray scale
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // initialize haar cascade
    CascadeClassifier cdc;
    cdc.load("C:\\Users\\asmaa\\Desktop\\OPENCV\\Classifiers\\haarcascade_frontalface_default.xml");

    // detect faces
    equalizeHist(gray,gray);
    cdc.detectMultiScale(gray, faces, 1.13, 5 );

    // draw triangles
    for(int i=0; i<faces.size(); i++){
        rectangle(image, faces[i], Scalar(255,0,0), 10);
    }

    // set label text
    LABEL = "RESULT:\nNumber of detected faces: "+to_string(faces.size());

    // show window
    namedWindow(PATH, WINDOW_AUTOSIZE);
    imshow(PATH, image);
}

void detectFacesHOG(){
    vector <Rect> faces;

    // open image
    Mat image = imread(PATH,IMREAD_COLOR);
    Mat gray;

    // convert into gray scale
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // initialize haar cascade
    CascadeClassifier cdc;
    cdc.load("C:\\Users\\asmaa\\Desktop\\OPENCV\\Classifiers\\haarcascade_frontalface_default.xml");

    // detect faces
    equalizeHist(gray,gray);
    cdc.detectMultiScale(gray, faces, 1.13, 4 );

    // draw triangles
    for(int i=0; i<faces.size(); i++){
        rectangle(image, faces[i], Scalar(255,0,0), 10);
    }

    // set label text
    LABEL = "RESULT:\nNumber of detected faces: "+to_string(faces.size());

    // show window
    namedWindow(PATH, WINDOW_AUTOSIZE);
    imshow(PATH, image);
}

