# wingqt

Cross-platform desktop application for simple and semi-automatic morphological analysis of mosquito wings.

wingqt is built with python and the Qt toolkit.

## Requirements

- python3
- pyqt5
- opencv-python, imutils

### Running wingqt:
```
$ git clone https://github.com/wing-net/wingqt.git && cd wingqt

$ python --version    # _if python points to python2 for you, use python3 and pip3_
Python 3.8.6

$ pip install numpy==1.19.3    # _important to specify this version if using windows_
...

$ pip install pyqt5 opencv-python imutils
...

$ python wingqt.py

```

## Todo

 - [x] refactor/clean up generated code
 - [x] add central canvas with QPainter 
 - [x] implement tools stuff (add,erase..) 
 - [x] implement file handling (loading, exporting) 
 - [x] add move/dragging functionality
 - [x] add file picker to choose export name 
 - [x] add session saving for open image files
 - [x] add swap files for session recovery
 - [x] give menu bar actual functionality 
 - [ ] add keybindings for switching modes etc 
 - [x] add draggable box/line to mark/display length
 - [ ] hook up detection schemes to automatically mark length, points
 - [x] improve UI (pressed appearance on buttons, etc)
 - [x] add detect-all, export-all
 - [ ] change resource loading and other relative path stuff (file picker defaults)
 - [ ] launcher scripts for macos/win/linux
 - [ ] docs


