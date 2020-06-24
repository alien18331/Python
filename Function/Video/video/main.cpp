#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <ctime>
extern "C" {
#include <wiringPi.h>
}

using namespace cv;
using namespace std;
void camera();
void Delay(int);


void camera()
{
    wiringPiSetup();
    Mat frame;
    VideoCapture cap;
    int apiID = cv::CAP_ANY;      // 0 = autodetect default API
    int i=1;
    int j=0;
    bool status=true;
    char aaa[1024];
    pinMode(1, INPUT);
    pullUpDnControl(1,PUD_UP);
    cap.open(apiID);
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
    }
    cout << "Start grabbing" << endl
        << "Press any key to terminate" << endl;
    while(1)
    {
        //clock_t now = clock();
        cap.read(frame);
        if (frame.empty()) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }

        if (digitalRead(1)==LOW)
        {
            j=5;
            status=false;
        }
        if (digitalRead(1)==HIGH)
        {
            j=j-1;
            if (status==false & j==0)
            {
                cout <<"low\n";
                sprintf(aaa, "test-%d.jpg", ++i);
                imwrite (aaa, frame);
                status=true;
            }
        }
        if (j<=0) j=0;

        imshow("Live", frame);
        if (waitKey(5) >= 0)
            break;
        //int dtime = clock()-now;
        //cout <<dtime<<"\n";

    }
}

int main()
{
    camera();
}

