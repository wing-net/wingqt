# wingqt

Cross-platform desktop application for simple and semi-automatic morphological analysis of mosquito wings.

wingqt is built with python and the Qt toolkit.

## Requirements

- python3
- pyqt5

### Running wingqt:
```
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
- [ ] add move/dragging functionality
- [ ] add (marked) image saving
- [ ] add file picker to choose export name
- [ ] give menu bar actual functionality
- [ ] add keybindings for switching modes etc
- [ ] add draggable box/line to mark length
- [ ] hook up detection schemes to automatically mark length, points
- [ ] add keybindings for switching modes etc
- [ ] add config options? (export format, detection scheme, etc)
