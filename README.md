# wingqt

Cross-platform desktop application for simple and semi-automatic morphological analysis of mosquito wings.

wingqt is built with python and the Qt toolkit.

## Requirements

- python3
- pyqt5

### Running wingqt:
```
~/ $ git clone https://github.com/wing-net/wingqt.git && cd wingqt

wingqt/ $ python --version
Python 3.8.6

wingqt/ $ pip install pyqt5
...

wingqt/ $ python wingqt.py

```

## Todo

 - [x] refactor/clean up generated code
 - [x] add central canvas with QPainter 
 - [x] implement tools stuff (add,erase..) 
 - [x] implement file handling (loading, exporting) 
 - [x] add move/dragging functionality
 - [x] add file picker to choose export name 
 - [ ] add (marked) image saving 
 - [ ] give menu bar actual functionality 
 - [ ] add keybindings for switching modes etc 
 - [ ] add draggable box/line to mark/display length
 - [ ] hook up detection schemes to automatically mark length, points
 - [ ] improve UI (pressed appearance on buttons, etc)
 - [ ] add config options? (export format, detection scheme, etc)