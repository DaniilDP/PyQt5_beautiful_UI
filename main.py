from PyQt5 import QtGui, QtWidgets
from tomorrow import threads
import sys, time, random
from UIX import MainWindow




APP = QtWidgets.QApplication(sys.argv)
UI = MainWindow()
UI.resize(1200, 700)
UI.show()


@threads(1)
def main():
    """Имитация работы (просто смена цыета кнопки старт)"""
    while UI.menubar.checkBox_Start.objectName() == 'on':
        UI.menubar.checkBox_Start.setStyleSheet("QPushButton {"
                                              "  height:50px;"
                                              "  border: None;"
                                              "  width:50px;"
                                              "  padding: -4px -4px  -4px  -4px;"
                                              f'background-color : rgba({random.randint(0, 250)}, {random.randint(0, 250)}, {random.randint(0, 250)}, 150);'
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                              " background-color: rgba(0, 255, 51, 250);"
                                              " border-radius: 5px;}")
        time.sleep(1)


def pushbutton():
    time.sleep(0.1)
    if UI.menubar.checkBox_Start.objectName() == 'off':
        UI.menubar.checkBox_Start.setObjectName("on")
        UI.menubar.checkBox_Start.setIcon(QtGui.QIcon("images/Paus.png"))
        main()
    else:
        UI.menubar.checkBox_Start.setObjectName("off")
        UI.menubar.checkBox_Start.setIcon(QtGui.QIcon("images/Play.png"))
        UI.menubar.checkBox_Start.setStyleSheet("QPushButton {"
                                              "  height:50px;"
                                              "  border: None;"
                                              "  width:50px;"
                                              "  padding: -4px -4px  -4px  -4px;"
                                              "  background: None;"
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                              " background-color: rgba(0, 255, 51, 250);"
                                              " border-radius: 5px;}")

if __name__ == "__main__":
    UI.menubar.exit.clicked.connect(UI.close)
    #Подключение функции к кнопке
    UI.menubar.checkBox_Start.clicked.connect(pushbutton)
    sys.exit(APP.exec_())