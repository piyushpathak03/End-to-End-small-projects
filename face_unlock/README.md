# Lock/Unlock Ubuntu OS 

## Introduction
We can lock and unlock our Ubuntu system using face recognition(currently only on Ubuntu). 

## Article about implementation
[Automatically Locking & Unlocking Ubuntu with Computer Vision Using a Human Face!!!](https://medium.com/p/automatically-locking-unlocking-ubuntu-with-computer-vision-using-a-human-face-db35cbe312f7?source=email-7d2dbe2d619d--writer.postDistributed&sk=b7d25089643c2c719eb6e36aecfef085)

## Demo
![Demo video](demo.gif)

## Requirements

Install below the required library in your local machine.

1) python 3.7
2) opencv 4.1.0
3) numpy 
4) face-recognition
5) sudo apt-get install gnome-screensaver
6) sudo apt-get install xdotool

## Quick Start
I have used three python files to solve this issue.

1) **face_generate.py**
 This will detect your face and save it in the dataset folder then the new folder will create with your name.
 
2) **face_train.py**
 This python file will open the dataset folder and take your image from that and train your face using the K-nearest neighbor algorithm and face_recognition library.
 
3) **face_unlock.py**
 This is an important python file that will detect your face using the webcam and unlock the system.

## Having problems?

If you run into problems, Please feel free to connect me on [Linkedin](https://www.linkedin.com/in/bala-venkatesh-67964247/) and [Twitter](https://twitter.com/balavenkatesh22)


## Contributing

Code contributions are also very welcome. feel free to open an issue for that too.


To do:
- [ ] Support Windows and Mac OS.
- [ ] Train face using browser(UI).
- [ ] Increase performance and speed.


## About me

**Piyush Pathak**

[**PORTFOLIO**](https://anirudhrapathak3.wixsite.com/piyush)

[**GITHUB**](https://github.com/piyushpathak03)

[**BLOG**](https://medium.com/@piyushpathak03)


# 📫 Follw me: 

[![Linkedin Badge](https://img.shields.io/badge/-PiyushPathak-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/piyushpathak03/)](https://www.linkedin.com/in/piyushpathak03/)

<p  align="right"><img height="100" src = "https://media.giphy.com/media/l3URDstnIjBNY7rwLB/giphy.gif"></p>
