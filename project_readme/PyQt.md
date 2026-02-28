# PyQt - Notes

## What is it?
PyQt is a python library based on the Qt framework from C++. \
It has bindings, which interpret Python code and translate it into C++ code.

QtWidgets provides a set of UI elements... Windows, Buttons, Text Boxes

QWidget is the base class for all Widgets (eg: QMainWindow extends QWidget)
`QtWidgets.QApplication` is engine that runs an app with a GUI
`QtWidgets.QMainWindow` is the main window 
`QtWidgets.QGraphicsScene` is what is shown by a view.. kind of like
QGraphicsScene scene;
scene.addText("Hello, world!");

QGraphicsView view(&scene);
view.show();
A scene has no appearance and it must be shown through other means (such as a view)