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
    QString path = QFileDialog::getOpenFileName();
    detectFaces(path.toStdString());
    ui->label->setText(QString::fromStdString(LABEL));
}

void detectFaces(string path){
    vector <Rect> faces;
    Mat image = imread(path,IMREAD_COLOR);
    Mat rgb;
    cvtColor(image, rgb,COLOR_BGR2GRAY);
    CascadeClassifier cdc;
    cdc.load("C:\\Users\\asmaa\\Desktop\\OPENCV\\Classifiers\\haarcascade_frontalface_default.xml");
    cdc.detectMultiScale(rgb, faces, 1.13, 4 );

    for(int i=0; i<faces.size(); i++){
        rectangle(image, faces[i], Scalar(255,0,0), 10);
    }

    //putText(image, "Number of detected faces: "+to_string(faces.size()), Point(100,100), FONT_HERSHEY_DUPLEX,1,CV_RGB(0,255,0),5);
    LABEL = "RESULT:\nNumber of detected faces: "+to_string(faces.size());

    namedWindow(path, WINDOW_AUTOSIZE);
    imshow(path, image);
}
