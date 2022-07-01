from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import finplot as fplt
import pandas as pd
import datetime as DT
import sys




"""График"""
class Chart(QMainWindow):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)
        self.setStyleSheet("border-radius: 25px;")
        fplt.foreground = '#7c7c7d'
        fplt.background = '#191b20'
        fplt.odd_plot_background = '#242424'
        fplt.candle_bull_color = fplt.volume_bull_color = fplt.candle_bull_body_color = fplt.volume_bull_body_color = '#2ebd85'
        fplt.candle_bear_color = fplt.volume_bear_color = '#e0294a'
        fplt.cross_hair_color = '#eefa'
        fplt.y_label_width = 40
        fplt.display_timezone = DT.timezone.utc
        price = fplt.create_plot_widget(self, init_zoom_periods=100, yscale='linear')
        price.set_visible(crosshair=True, xaxis=True, yaxis=True, xgrid=True, ygrid=True)
        self.axs = [price]
        df = pd.read_csv('BTCUSDT15M.csv')
        df["time"] = df["time"].apply(lambda x: datetime.strptime(x[:16], '%Y-%m-%d %H:%M'))
        self.plots = []
        self.plots.append(fplt.candlestick_ochl(df[['time', 'open', 'close', 'high', 'low']], ))
        fplt.autoviewrestore()
        fplt.show(qt_exec=False)
        price.ax_widget.setStyleSheet("border: 2px solid; border-radius: 25px;")
        self.setCentralWidget(price.ax_widget)

    def price_refresh(self):
        df = pd.read_csv('BTCUSDT15M.csv')
        df["time"] = df["time"].apply(lambda x: datetime.strptime(x[:16], '%Y-%m-%d %H:%M'))
        self.plots[0].update_data(df[['time', 'open', 'close', 'high', 'low']])


"""Домашняя страница с графиком"""
class Home_page(QMainWindow):
    def __init__(self, parent=None):
        super(Home_page, self).__init__(parent)
        self.centralwidget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QGridLayout(self.centralwidget)

        """Информационная панель"""
        self.info_table = QtWidgets.QPushButton()
        self.info_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHeightForWidth(self.info_table.sizePolicy().hasHeightForWidth())
        self.info_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.info_table.setFont(font)
        self.info_table.setStyleSheet("QPushButton {"
                                             "  font-size: 15pt;"
                                             "  width: 400px;"
                                             "  color: #808080;"
                                             "  background: None;"
                                             "  border: 1px solid;"
                                             "  border-radius: 6px;} ")
        self.layout.addWidget(self.info_table, 1, 1, 1, 1)

        """График"""
        self.chart = Chart()
        self.chart.setStyleSheet("border: 2px solid; border-radius: 5px;  background-color: #f0f0f3;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(211, 211, 214))
        self.chart.setGraphicsEffect(shadow)
        self.layout.addWidget(self.chart, 1, 2, 1, 1)

        self.setCentralWidget(self.centralwidget)


"""Меню программы"""
class Menu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.dragPos = QtCore.QPoint()
        self.setContentsMargins(0,0,0,0)
        self.horizontallayout = QtWidgets.QHBoxLayout(self)
        self.horizontallayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("QWidget {border:0px ; border-radius:10px;  background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffffff, stop:1 #ffffff);}")
        self.centralwidget.setContentsMargins(5, 5, 15, 5)
        self.horizontallayout.addWidget(self.centralwidget)
        self.menu_bar = QtWidgets.QGridLayout(self.centralwidget)


        self.menu_bar.setSpacing(5)
        self.menu_bar.setContentsMargins(0, 0, 0, 0)


        """Кнопка домой"""
        icon_home = QtGui.QIcon()
        icon_home.addPixmap(QtGui.QPixmap("images/Home.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home = QtWidgets.QPushButton()
        self.pushButton_home.setSizeIncrement(QtCore.QSize(60, 60))
        self.pushButton_home.setBaseSize(QtCore.QSize(60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
        self.pushButton_home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setIcon(icon_home)
        self.pushButton_home.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_home.setStyleSheet("QPushButton {"
                                              "  height:50px;"
                                              "  width:50px;"
                                              "  padding: -4px -4px  -4px  -4px;"
                                              "  background: None;"
                                              "  border: None;"
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                                "  border: None;"
                                              " background-color: rgba(0, 255, 51, 250);"
                                              " border-radius: 5px;}")
        self.menu_bar.addWidget(self.pushButton_home, 1, 2, 1, 1)

        """кнопка настройки"""
        self.pushButton_setings = QtWidgets.QPushButton()
        self.pushButton_setings.setSizeIncrement(QtCore.QSize(60, 60))
        self.pushButton_setings.setBaseSize(QtCore.QSize(60, 60))
        self.pushButton_setings.setAutoRepeatDelay(50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_setings.sizePolicy().hasHeightForWidth())
        self.pushButton_setings.setSizePolicy(sizePolicy)
        self.pushButton_setings.setText("")
        self.pushButton_setings.setChecked(True)
        self.pushButton_setings.setIcon(QtGui.QIcon("images/Setings.png"))
        self.pushButton_setings.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_setings.setStyleSheet("QPushButton {"
                                              "  height:50px;"
                                              "  width:50px;"
                                              "  padding: -4px -4px  -4px  -4px;"
                                              "  background: None;"
                                              "  border: None;"
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                              " background-color: rgba(0, 255, 51, 250);"
                                              " border-radius: 5px;}")
        self.menu_bar.addWidget(self.pushButton_setings,1,3,1,1,QtCore.Qt.AlignLeft)

        """кнопка старт стоп"""
        self.checkBox_Start = QtWidgets.QPushButton()
        self.checkBox_Start.setSizePolicy(sizePolicy)
        self.checkBox_Start.setObjectName("off")
        self.checkBox_Start.setIcon(QtGui.QIcon("images/Play.png"))
        self.checkBox_Start.setIconSize(QtCore.QSize(50, 50))
        self.checkBox_Start.setStyleSheet("QPushButton  {"
                                              "  height:50px;"
                                              "  width:50px;"
                                              "  padding: -4px -4px  -4px  -4px;"
                                              "  background: None;"
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                              " background-color: rgba(0, 255, 51, 250);"
                                              " border-radius: 5px;}")
        self.menu_bar.addWidget(self.checkBox_Start, 1, 1, 1, 1)


        """кнопка закрытия"""
        self.exit = QtWidgets.QPushButton()
        self.exit.setSizeIncrement(QtCore.QSize(30, 30))
        self.exit.setBaseSize(QtCore.QSize(30, 30))
        self.exit.setAutoRepeatDelay(50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_setings.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setChecked(True)
        self.exit.setStyleSheet("QPushButton {"
                                              "  height:20px;"
                                              "  width:20px;"
                                              "  padding: 0px 0px  0px  0px;"
                                              "  background: #000000;"
                                              "  border: None;"
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                              " background-color: #b4b2d6;"
                                              " border-radius: 10px;}")
        self.menu_bar.addWidget(self.exit,1,6,1,1)

        """кнопка во весь экран"""
        self.expand = QtWidgets.QPushButton()
        self.expand.setSizeIncrement(QtCore.QSize(30, 30))
        self.expand.setBaseSize(QtCore.QSize(30, 30))
        self.expand.setAutoRepeatDelay(50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expand.sizePolicy().hasHeightForWidth())
        self.expand.setSizePolicy(sizePolicy)
        self.expand.setChecked(True)
        self.expand.setStyleSheet("QPushButton {"
                                              "  height:20px;"
                                              "  width:20px;"
                                              "  padding: 0px 0px  0px  0px;"
                                              "  background: #ffe600;"
                                              "  border: None;"
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                              " background-color: #b4b2d6;"
                                              " border-radius: 10px;}")
        self.menu_bar.addWidget(self.expand,1,5,1,1)

        """кнопка свернуть"""
        self.cut = QtWidgets.QPushButton()
        self.cut.setSizeIncrement(QtCore.QSize(30, 30))
        self.cut.setBaseSize(QtCore.QSize(30, 30))
        self.cut.setAutoRepeatDelay(50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cut.sizePolicy().hasHeightForWidth())
        self.cut.setSizePolicy(sizePolicy)
        self.cut.setChecked(True)
        self.cut.setStyleSheet("QPushButton {"
                                              "  height:20px;"
                                              "  width:20px;"
                                              "  padding: 0px 0px  0px  0px;"
                                              "  background: #8a8a80;"
                                              "  border: None;"
                                              "  border-radius: 10px;} "
                                              "QPushButton::hover {"
                                              " background-color: #b4b2d6;"
                                              " border-radius: 10px;}")
        self.menu_bar.addWidget(self.cut,1,4,1,1)


"""Окно программы"""
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.visible_window = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout.addWidget(self.visible_window )
        self.visible_window.setStyleSheet(
            "QWidget {border:0px; border-radius:10px;  background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffe600, stop:1 #ffe600);}"
            "QLineEdit{\n"
            "background:white;"
            "    border:0px;    \n"
            "    border: 2px solid #B3B3B3;\n"
            "    font-family:\'Microsoft YaHei\';\n"
            "    border-radius:5px;\n"
            "    font-size:20px;\n"
            "    font-weight:bold;\n"
            "    }\n"
            "\n"
            "QLineEdit:hover{\n"
            "    border: 3px solid #66A3FF;\n"
            "    }\n"
            "\n"
            "QLineEdit:focus{\n"
            "    border: 3px solid #E680BD;\n"
            "    }\n"
            "\n"
            "QWidget#main_widget{\n"
            "    background:white;\n"
            "    border-radius:10px;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "    text-align:right;\n"
            "    font-family:\'Microsoft YaHei\';\n"
            "    font-size:30px;\n"
            "    font-weight:bold;\n"
            "    }\n"
            "\n"
            "QPushButton{\n"
            "    border:0px;\n"
            "    height:30px;\n"
            "    border-radius:15px;\n"
            "    font-family:\'Microsoft YaHei\';\n"
            "    font-size:20px;\n"
            "    color:white;\n"
            "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);\n"
            "    }\n"
            "\n"
            " QPushButton:hover{\n"
            "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
            " }\n"
            " \n"
            " QPushButton:pressed{\n"
            "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
            "     }\n"

            "")

        #Простая с страница с надписью
        page_setings = QtWidgets.QLabel("Настройки", alignment=QtCore.Qt.AlignCenter)
        #Страница с графиком
        page_home = Home_page(self.visible_window)

        stackedwidget = QtWidgets.QStackedWidget(self.visible_window)
        stackedwidget.setContentsMargins(0,0,0,0)

        self.menubar = Menu(self.visible_window)
        self.menubar.cut.clicked.connect(self.minimize)
        self.menubar.expand.clicked.connect(self.maximized)
        self.menubar.installEventFilter(self)

        self.button_for_windows = QtWidgets.QButtonGroup(self.visible_window)
        self.button_for_windows.buttonClicked[int].connect(stackedwidget.setCurrentIndex)

        """кнопка старт стоп"""
        self.button_for_windows.addButton(self.menubar.checkBox_Start)

        """кнопка домой"""
        self.button_for_windows.addButton(self.menubar.pushButton_home, stackedwidget.addWidget(page_home))

        """кнопка настройки"""
        self.button_for_windows.addButton(self.menubar.pushButton_setings, stackedwidget.addWidget(page_setings))




        self.window = QtWidgets.QVBoxLayout(self.visible_window)
        self.window.setContentsMargins(5,5,5,5)
        self.window.addWidget(self.menubar)
        self.window.addWidget(stackedwidget)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(25)
        self.shadow.setColor(QColor(0, 0, 0))
        self.visible_window.setGraphicsEffect(self.shadow)
        self.setCentralWidget(self.centralwidget)

    """Управление окном"""
    def minimize(self):
        self.showMinimized()

    def maximized(self):
        """Изменяем внешний вид при разворачивании на весь экран"""
        if self.isMaximized():
            self.visible_window.setStyleSheet("QWidget {border:0px; border-radius:10px;  background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffe600, stop:1 #ffe600); padding: 0px 0px  0px  0px;}")
            self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.showNormal()
        else:
            self.visible_window.setStyleSheet("QWidget {border:0px; border-radius:0px;  background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffe600, stop:1 #ffe600); padding: 0px 0px  0px  0px;}")
            self.horizontalLayout.setContentsMargins(0,0,0,0)
            self.showMaximized()

    def eventFilter(self, obj, event):
        """Двигать окно программы"""
        if event.type() == QEvent.MouseButtonPress:
            self.dragPos = event.globalPos()
        if event.type() == QEvent.MouseMove:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
        return True




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())