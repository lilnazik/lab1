# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDoubleSpinBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 740)
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 121, 145, 255), stop:1 rgba(120, 255, 214, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.window_title = QLabel(self.centralwidget)
        self.window_title.setObjectName(u"window_title")
        self.window_title.setMinimumSize(QSize(500, 30))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(18)
        self.window_title.setFont(font1)
        self.window_title.setStyleSheet(u"background: none;")
        self.window_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.window_title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.method_title = QLabel(self.centralwidget)
        self.method_title.setObjectName(u"method_title")
        self.method_title.setMinimumSize(QSize(180, 80))
        self.method_title.setMaximumSize(QSize(180, 80))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(16)
        self.method_title.setFont(font2)
        self.method_title.setStyleSheet(u"background: none;")
        self.method_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.method_title)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(180, 30))
        self.radioButton.setMaximumSize(QSize(180, 30))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setPointSize(14)
        self.radioButton.setFont(font3)
        self.radioButton.setStyleSheet(u"background: none;")
        self.radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(180, 30))
        self.radioButton_2.setMaximumSize(QSize(180, 30))
        self.radioButton_2.setFont(font3)
        self.radioButton_2.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font3)
        self.radioButton_3.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.radioButton_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.limits_title = QLabel(self.centralwidget)
        self.limits_title.setObjectName(u"limits_title")
        self.limits_title.setMinimumSize(QSize(240, 80))
        self.limits_title.setMaximumSize(QSize(240, 80))
        self.limits_title.setFont(font2)
        self.limits_title.setStyleSheet(u"background: none;")
        self.limits_title.setScaledContents(False)
        self.limits_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.limits_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.limit_x1 = QLabel(self.centralwidget)
        self.limit_x1.setObjectName(u"limit_x1")
        self.limit_x1.setMinimumSize(QSize(30, 20))
        self.limit_x1.setMaximumSize(QSize(30, 20))
        self.limit_x1.setFont(font3)
        self.limit_x1.setStyleSheet(u"background: none;")
        self.limit_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.limit_x1)

        self.X1SpinBox = QDoubleSpinBox(self.centralwidget)
        self.X1SpinBox.setObjectName(u"X1SpinBox")
        self.X1SpinBox.setMinimumSize(QSize(60, 0))
        self.X1SpinBox.setMaximumSize(QSize(60, 16777215))
        self.X1SpinBox.setStyleSheet(u"background: #F9F9F9;")
        self.X1SpinBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.X1SpinBox.setDecimals(1)
        self.X1SpinBox.setMinimum(-100.000000000000000)
        self.X1SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout.addWidget(self.X1SpinBox)

        self.horizontalSpacer_7 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.limit_x2 = QLabel(self.centralwidget)
        self.limit_x2.setObjectName(u"limit_x2")
        self.limit_x2.setMinimumSize(QSize(30, 20))
        self.limit_x2.setMaximumSize(QSize(30, 20))
        self.limit_x2.setFont(font3)
        self.limit_x2.setStyleSheet(u"background: none;\n"
"margin: 0px;")
        self.limit_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.limit_x2)

        self.X2SpinBox = QDoubleSpinBox(self.centralwidget)
        self.X2SpinBox.setObjectName(u"X2SpinBox")
        self.X2SpinBox.setMinimumSize(QSize(60, 0))
        self.X2SpinBox.setMaximumSize(QSize(60, 16777215))
        self.X2SpinBox.setStyleSheet(u"background: #F9F9F9;\n"
"margin: 0px;")
        self.X2SpinBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.X2SpinBox.setDecimals(1)
        self.X2SpinBox.setMinimum(-100.000000000000000)
        self.X2SpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.X2SpinBox)

        self.horizontalSpacer_6 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.accuracy_label = QLabel(self.centralwidget)
        self.accuracy_label.setObjectName(u"accuracy_label")
        self.accuracy_label.setMinimumSize(QSize(90, 20))
        self.accuracy_label.setMaximumSize(QSize(90, 20))
        self.accuracy_label.setFont(font2)
        self.accuracy_label.setStyleSheet(u"background: none;\n"
"margin: 0px;")

        self.horizontalLayout_6.addWidget(self.accuracy_label)

        self.AccuracySpinBox = QDoubleSpinBox(self.centralwidget)
        self.AccuracySpinBox.setObjectName(u"AccuracySpinBox")
        self.AccuracySpinBox.setMinimumSize(QSize(60, 0))
        self.AccuracySpinBox.setMaximumSize(QSize(60, 16777215))
        self.AccuracySpinBox.setStyleSheet(u"background: #F9F9F9;\n"
"margin: 0px;")
        self.AccuracySpinBox.setMaximum(1.000000000000000)
        self.AccuracySpinBox.setSingleStep(0.010000000000000)

        self.horizontalLayout_6.addWidget(self.AccuracySpinBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.function_label = QLabel(self.centralwidget)
        self.function_label.setObjectName(u"function_label")
        self.function_label.setMinimumSize(QSize(200, 50))
        self.function_label.setMaximumSize(QSize(200, 50))
        self.function_label.setFont(font2)
        self.function_label.setStyleSheet(u"background: none;")
        self.function_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.function_label)

        self.function_input = QLineEdit(self.centralwidget)
        self.function_input.setObjectName(u"function_input")
        self.function_input.setMinimumSize(QSize(500, 30))
        self.function_input.setMaximumSize(QSize(500, 30))
        self.function_input.setFont(font3)
        self.function_input.setStyleSheet(u"background: #F9F9F9;")
        self.function_input.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.function_input)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.results_table = QTableWidget(self.centralwidget)
        if (self.results_table.columnCount() < 3):
            self.results_table.setColumnCount(3)
        font4 = QFont()
        font4.setFamilies([u"Noto Sans"])
        font4.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.results_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font5 = QFont()
        font5.setFamilies([u"Noto Sans"])
        font5.setPointSize(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.results_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.results_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.results_table.setObjectName(u"results_table")
        self.results_table.setMinimumSize(QSize(400, 300))
        self.results_table.setMaximumSize(QSize(400, 300))
        self.results_table.setFont(font3)
        self.results_table.setStyleSheet(u"background: #F9F9F9;")
        self.results_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.results_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.results_table)

        self.img_place = QLabel(self.centralwidget)
        self.img_place.setObjectName(u"img_place")
        self.img_place.setMinimumSize(QSize(400, 300))
        self.img_place.setMaximumSize(QSize(400, 300))
        self.img_place.setStyleSheet(u"background: #F9F9F9;")
        self.img_place.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.img_place)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, -1)
        self.Calculate = QPushButton(self.centralwidget)
        self.Calculate.setObjectName(u"Calculate")
        self.Calculate.setMinimumSize(QSize(250, 50))
        self.Calculate.setMaximumSize(QSize(250, 50))
        self.Calculate.setStyleSheet(u"QPushButton{\n"
"background: #F9F9F9;\n"
"border-radius: 20px;\n"
"\n"
"font-family: 'Noto Sans SC';\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #95BFFF;     \n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: #DFECFF;\n"
"}")

        self.horizontalLayout_5.addWidget(self.Calculate)

        self.Show = QPushButton(self.centralwidget)
        self.Show.setObjectName(u"Show")
        self.Show.setMinimumSize(QSize(250, 50))
        self.Show.setMaximumSize(QSize(250, 50))
        self.Show.setStyleSheet(u"QPushButton{\n"
"background: #F9F9F9;\n"
"border-radius: 20px;\n"
"\n"
"font-family: 'Noto Sans SC';\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #95BFFF;     \n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: #DFECFF;\n"
"}")

        self.horizontalLayout_5.addWidget(self.Show)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u0435\u043b\u044c\u043d\u0435 \u0440\u043e\u0437\u0432'\u044f\u0437\u0443\u0432\u0430\u043d\u043d\u044f \u043d\u0435\u043b\u0456\u043d\u0456\u0439\u043d\u0438\u0445 \u0440\u0456\u0432\u043d\u044f\u043d\u044c", None))
        self.method_title.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u043e\u0448\u0443\u043a\u0443\n"
"\u043a\u043e\u0440\u0435\u043d\u044f", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0456\u0442\u0435\u0440\u0430\u0446\u0456\u0439", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0434\u0438\u0445\u043e\u0442\u043e\u043c\u0456\u0457", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u041d\u044c\u044e\u0442\u043e\u043d\u0430", None))
        self.limits_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044f \u043c\u0435\u0436\n"
"\u043f\u043e\u0448\u0443\u043a\u0443 \u043a\u043e\u0440\u0435\u043d\u044f", None))
        self.limit_x1.setText(QCoreApplication.translate("MainWindow", u"\u04251:", None))
        self.limit_x2.setText(QCoreApplication.translate("MainWindow", u"\u04252:", None))
        self.accuracy_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u0456\u0441\u0442\u044c:", None))
        self.function_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043d\u044f \u0444\u0443\u043d\u043a\u0446\u0456\u0457", None))
        ___qtablewidgetitem = self.results_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041a-\u0442\u044c \u0456\u0442\u0435\u0440\u0430\u0446\u0456\u0439", None));
        ___qtablewidgetitem1 = self.results_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0456\u043d\u044c", None));
        ___qtablewidgetitem2 = self.results_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u043d\u044f", None));
        self.img_place.setText("")
        self.Calculate.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0437\u0440\u0430\u0445\u0443\u0432\u0430\u0442\u0438", None))
        self.Show.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0456\u043a", None))
    # retranslateUi

