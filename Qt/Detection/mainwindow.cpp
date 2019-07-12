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
void detectFaces(string);

string LABEL = "";

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

    // detect faces
    detectFaces(path.toStdString());

    // set label text
    ui->label->setText(QString::fromStdString(LABEL));
}

void detectFaces(string path){
    vector <Rect> faces;

    // open image
    Mat image = imread(path,IMREAD_COLOR);
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
    namedWindow(path, WINDOW_AUTOSIZE);
    imshow(path, image);
}
