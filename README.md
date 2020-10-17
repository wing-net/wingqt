# wingqt

desktop application for _the project_

## Requirements

- python3
- pyqt5

```$ pip install pyqt5```

## Notes

ui created with qtdesigner and python code generated with `pyuic5`

to generate:
```$ pyuic5 -x mainwindow.ui -o mainwindow.py```
note that this will overwrite any application logic/additions to the python script 

## TODO

- refactor/clean up generated code
- add matplotlib plot to central canvas and integrate this with analysis stuff
- implement tools stuff (add,move,erase..)
- implement file handling (loading, exporting)
