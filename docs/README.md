# Welcome to the [wingqt](https://github.com/wing-net/wingqt) documentation!

This page serves to document the software and its uses, as well as helping troubleshoot or answer frequently asked questions.

## Contents
* [About Wingqt](#about)
* [Installation](#installation)
* [Getting Started](#gettingstarted)
    * [Features](#features)
    * [Opening Images](#opening)
    * [Annotation Tools](#annotation)
    * [Exporting Data](#exporting)
* [Development](#development)
* [Troubleshooting](#troubleshooting)


## <a id="about"></a>About Wingqt
stuff


## <a id="installation"></a>Installation

The easiest way to get started with wingqt is to install an executable for your system found on the [releases paege](https://github.com/wing-net/wingqt/releases). Simply extract the archive and run the executable (`wingqt.exe` for windows, or `wingqt` for MacOS and linux). You can move the wignqt folder anywhere, but be sure to not remove the executable from this folder (it is recommened to make a shortcut for it).

If you are concerned about running executables or would like to run it straight from the source, you can do so very easily since wingqt is written in 100% python. 

**Requirements:**
* Python 3.8+
* opencv-python, imutils, pyqt5

First, clone the repository

```git clone https://github.com/wing-net/wingqt.git```

Make sure you are using a correct python version have all of the required dependencies

```python --version```

**IMPORTANT** if you are a using windows there is a bug in later numpy releases so make sure to install the version below, users on MacOS or Linux need not worry

```pip3 install numpy==1.19.3```

```pip3 install pyqt opencv-python imutils```

With everything installed now, you should be able to run the program

```cd wingqt```

```python3 wingqt.py```


## <a id="gettingstarted"></a>Getting Started
stuff

### <a id="opening"></a>Opening Images
stuff
![open](resources/open.gif)

### <a id="annotation"></a>Annotation Tools
stuff

### <a id="exporting"></a>Exporting Data
stuff


## <a id="development"></a>Development
stuff


## <a id="troubleshooting"></a>Troubleshooting
stuff


