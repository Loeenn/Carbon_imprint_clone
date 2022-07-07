from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 990)
        MainWindow.setStyleSheet("QMainWindow{\n"
"  background-color:RGB(0,0,0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1941, 971))
        self.widget.setStyleSheet("background-color:black;")
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 480, 406))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(1, -1, 1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("QPushButton{\n"
"                    margin: 5px;\n"
"                          background-color: rgb(0,0,50);\n"
"                          border-style: inset;\n"
"                          color: white;\n"
"                          border-radius: 10px;\n"
"                          font: bold 7p;\n"
"                          min-width: 4em;\n"
"                      min-height:30px;\n"
"                          padding: 2px;}\n"
"QPushButton:pressed{\n"
"                          background-color: white;\n"
"                          color: black;}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"                    margin: 5px;\n"
"                          background-color: rgb(0,0,50);\n"
"                          border-style: inset;\n"
"                          color: white;\n"
"                          border-radius: 10px;\n"
"                          font: bold 7p;\n"
"                          min-width: 4em;\n"
"                      min-height:30px;\n"
"                          padding: 2px;}\n"
"QPushButton:pressed{\n"
"                          background-color: white;\n"
"                          color: black;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"                    margin: 5px;\n"
"                          background-color: rgb(0,0,50);\n"
"                          border-style: inset;\n"
"                          color: white;\n"
"                          border-radius: 10px;\n"
"                          font: bold 7p;\n"
"                          min-width: 4em;\n"
"                      min-height:30px;\n"
"                          padding: 2px;}\n"
"QPushButton:pressed{\n"
"                          background-color: white;\n"
"                          color: black;}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"                    margin: 5px;\n"
"                          background-color: rgb(0,0,50);\n"
"                          border-style: inset;\n"
"                          color: white;\n"
"                          border-radius: 10px;\n"
"                          font: bold 7p;\n"
"                          min-width: 4em;\n"
"                      min-height:30px;\n"
"                          padding: 2px;}\n"
"QPushButton:pressed{\n"
"                          background-color: white;\n"
"                          color: black;}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"                    margin: 5px;\n"
"                          background-color: rgb(0,0,50);\n"
"                          border-style: inset;\n"
"                          color: white;\n"
"                          border-radius: 10px;\n"
"                          font: bold 7p;\n"
"                          min-width: 4em;\n"
"                      min-height:30px;\n"
"                          padding: 2px;}\n"
"QPushButton:pressed{\n"
"                          background-color: white;\n"
"                          color: black;}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.Finential_statistic1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Finential_statistic1.setStyleSheet("color:white;\n"
"font: 100px;\n"
"margin: 20px, 0px, 20px, 0px;\n"
"\n"
"")
        self.Finential_statistic1.setWordWrap(True)
        self.Finential_statistic1.setObjectName("Finential_statistic1")
        self.gridLayout.addWidget(self.Finential_statistic1, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color:white;\n"
"font: 60px;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"                    margin: 5px;\n"
"                          background-color: rgb(0,0,120);\n"
"                          border-style: inset;\n"
"                          color: white;\n"
"                          border-radius: 15px;\n"
"                          border-color: beige;\n"
"                          font: bold 14p;\n"
"                          min-width: 10em;\n"
"                          padding: 10px;\n"
"                    margin-right:300px}\n"
"QPushButton:pressed{\n"
"                          background-color: white;\n"
"                          color: black;}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("color:white;\n"
"margin-right:230px;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color:white;\n"
"font: 18px;\n"
"text-align: left;")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Finential_statistic2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Finential_statistic2.setStyleSheet("color:white;\n"
"font: 27px;")
        self.Finential_statistic2.setWordWrap(True)
        self.Finential_statistic2.setObjectName("Finential_statistic2")
        self.horizontalLayout_2.addWidget(self.Finential_statistic2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(910, 230, 380, 380))
        self.frame_2.setStyleSheet("QFrame{\n"
"border-radius:190px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(85, 0, 255, 0), stop:0.75 rgb(68, 0, 68));\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setGeometry(QtCore.QRect(30, 30, 320, 320))
        self.widget_2.setStyleSheet("background-color:rgb(98, 0, 155);\n"
"border-radius:160px")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(50, 50, 220, 220))
        self.widget_3.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.188383 rgba(148, 0, 148, 255), stop:0.333922 rgba(188, 61, 188, 255), stop:0.529042 rgba(208, 67, 208, 255), stop:0.694346 rgba(188, 61, 188, 255), stop:0.841444 rgba(148, 0, 148, 255));\n"
"border-radius:110px")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(30, 30, 160, 160))
        self.widget_4.setStyleSheet("background-color:black;\n"
"border-radius:80px")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 111, 55))
        self.label_4.setStyleSheet("color:white;\n"
"font: 15px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.widget_19 = QtWidgets.QWidget(self.widget_4)
        self.widget_19.setGeometry(QtCore.QRect(30, 20, 141, 111))
        self.widget_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget_19)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 131, 87))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Finential_statistic1_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Finential_statistic1_2.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 50px;")
        self.Finential_statistic1_2.setWordWrap(True)
        self.Finential_statistic1_2.setObjectName("Finential_statistic1_2")
        self.horizontalLayout_3.addWidget(self.Finential_statistic1_2)
        self.Finential_statistic1_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Finential_statistic1_3.setStyleSheet("color:white;\n"
"font: 50px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_3.setWordWrap(True)
        self.Finential_statistic1_3.setObjectName("Finential_statistic1_3")
        self.horizontalLayout_3.addWidget(self.Finential_statistic1_3)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(1220, 40, 120, 120))
        self.widget_5.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.188383 rgba(111, 0, 148, 255), stop:0.333922 rgba(163, 61, 188, 255), stop:0.529042 rgba(168, 65, 208, 255), stop:0.694346 rgba(134, 59, 188, 255), stop:0.841444 rgba(91, 0, 144, 255));\n"
"border-radius:60px")
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 81, 55))
        self.label_5.setStyleSheet("color:white;\n"
"font: 15px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.Asset_sale = QtWidgets.QLabel(self.widget_5)
        self.Asset_sale.setGeometry(QtCore.QRect(30, 20, 81, 51))
        self.Asset_sale.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Asset_sale.setWordWrap(True)
        self.Asset_sale.setObjectName("Asset_sale")
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(1360, 270, 90, 90))
        self.widget_6.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.188383 rgba(111, 0, 148, 255), stop:0.333922 rgba(163, 61, 188, 255), stop:0.529042 rgba(168, 65, 208, 255), stop:0.694346 rgba(134, 59, 188, 255), stop:0.841444 rgba(91, 0, 144, 255));\n"
"border-radius:45px")
        self.widget_6.setObjectName("widget_6")
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 71, 55))
        self.label_7.setStyleSheet("color:white;\n"
"font: 12px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.Advertising = QtWidgets.QLabel(self.widget_6)
        self.Advertising.setGeometry(QtCore.QRect(10, 0, 81, 61))
        self.Advertising.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Advertising.setWordWrap(True)
        self.Advertising.setObjectName("Advertising")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(1420, 610, 100, 100))
        self.widget_7.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.188383 rgba(111, 0, 148, 255), stop:0.333922 rgba(163, 61, 188, 255), stop:0.529042 rgba(168, 65, 208, 255), stop:0.694346 rgba(134, 59, 188, 255), stop:0.841444 rgba(91, 0, 144, 255));\n"
"border-radius:50px;")
        self.widget_7.setObjectName("widget_7")
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 71, 41))
        self.label_8.setStyleSheet("color:white;\n"
"font: 12px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.Subscription = QtWidgets.QLabel(self.widget_7)
        self.Subscription.setGeometry(QtCore.QRect(10, 10, 71, 51))
        self.Subscription.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Subscription.setWordWrap(True)
        self.Subscription.setObjectName("Subscription")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(890, 120, 100, 100))
        self.widget_8.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.188383 rgba(111, 0, 148, 255), stop:0.333922 rgba(163, 61, 188, 255), stop:0.529042 rgba(168, 65, 208, 255), stop:0.694346 rgba(134, 59, 188, 255), stop:0.841444 rgba(91, 0, 144, 255));\n"
"border-radius:50px;")
        self.widget_8.setObjectName("widget_8")
        self.label_9 = QtWidgets.QLabel(self.widget_8)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 71, 41))
        self.label_9.setStyleSheet("color:white;\n"
"font: 12px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.Licencing = QtWidgets.QLabel(self.widget_8)
        self.Licencing.setGeometry(QtCore.QRect(10, 10, 81, 51))
        self.Licencing.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Licencing.setWordWrap(True)
        self.Licencing.setObjectName("Licencing")
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setGeometry(QtCore.QRect(780, 530, 120, 120))
        self.widget_9.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.188383 rgba(111, 0, 148, 255), stop:0.333922 rgba(163, 61, 188, 255), stop:0.529042 rgba(168, 65, 208, 255), stop:0.694346 rgba(134, 59, 188, 255), stop:0.841444 rgba(91, 0, 144, 255));\n"
"border-radius:60px")
        self.widget_9.setObjectName("widget_9")
        self.label_10 = QtWidgets.QLabel(self.widget_9)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 81, 55))
        self.label_10.setStyleSheet("color:white;\n"
"font: 15px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.Usage_fees = QtWidgets.QLabel(self.widget_9)
        self.Usage_fees.setGeometry(QtCore.QRect(20, 20, 81, 51))
        self.Usage_fees.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Usage_fees.setWordWrap(True)
        self.Usage_fees.setObjectName("Usage_fees")
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setGeometry(QtCore.QRect(1100, 620, 80, 80))
        self.widget_10.setStyleSheet("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.188383 rgba(111, 0, 148, 255), stop:0.333922 rgba(163, 61, 188, 255), stop:0.529042 rgba(168, 65, 208, 255), stop:0.694346 rgba(134, 59, 188, 255), stop:0.841444 rgba(91, 0, 144, 255));\n"
"border-radius:40px;")
        self.widget_10.setObjectName("widget_10")
        self.label_11 = QtWidgets.QLabel(self.widget_10)
        self.label_11.setGeometry(QtCore.QRect(20, 40, 61, 31))
        self.label_11.setStyleSheet("color:white;\n"
"font: 12px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.Licencing_2 = QtWidgets.QLabel(self.widget_10)
        self.Licencing_2.setGeometry(QtCore.QRect(10, 0, 81, 51))
        self.Licencing_2.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Licencing_2.setWordWrap(True)
        self.Licencing_2.setObjectName("Licencing_2")
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(1490, 180, 90, 90))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:45px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: black;\n"
"border-radius:35px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.widget_45 = QtWidgets.QWidget(self.frame)
        self.widget_45.setGeometry(QtCore.QRect(10, 10, 81, 61))
        self.widget_45.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_45.setObjectName("widget_45")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.widget_45)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Finential_statistic1_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.Finential_statistic1_4.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Finential_statistic1_4.setWordWrap(True)
        self.Finential_statistic1_4.setObjectName("Finential_statistic1_4")
        self.horizontalLayout_4.addWidget(self.Finential_statistic1_4)
        self.Finential_statistic1_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.Finential_statistic1_5.setStyleSheet("color:white;\n"
"font: 20px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_5.setWordWrap(True)
        self.Finential_statistic1_5.setObjectName("Finential_statistic1_5")
        self.horizontalLayout_4.addWidget(self.Finential_statistic1_5)
        self.frame_9 = QtWidgets.QFrame(self.widget)
        self.frame_9.setGeometry(QtCore.QRect(1570, 690, 90, 90))
        self.frame_9.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:45px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.frame_10.setStyleSheet("QFrame{\n"
"background-color: black;\n"
"border-radius:35px;\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.widget_18 = QtWidgets.QWidget(self.frame_10)
        self.widget_18.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.widget_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.widget_18)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Finential_statistic1_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.Finential_statistic1_26.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Finential_statistic1_26.setWordWrap(True)
        self.Finential_statistic1_26.setObjectName("Finential_statistic1_26")
        self.horizontalLayout_10.addWidget(self.Finential_statistic1_26)
        self.Finential_statistic1_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.Finential_statistic1_27.setStyleSheet("color:white;\n"
"font: 20px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_27.setWordWrap(True)
        self.Finential_statistic1_27.setObjectName("Finential_statistic1_27")
        self.horizontalLayout_10.addWidget(self.Finential_statistic1_27)
        self.frame_14 = QtWidgets.QFrame(self.widget)
        self.frame_14.setGeometry(QtCore.QRect(1100, 770, 90, 90))
        self.frame_14.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:45px;\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_14.setObjectName("frame_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.frame_15.setStyleSheet("QFrame{\n"
"background-color: black;\n"
"border-radius:35px;\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_15.setObjectName("frame_15")
        self.widget_44 = QtWidgets.QWidget(self.frame_15)
        self.widget_44.setGeometry(QtCore.QRect(10, 10, 71, 51))
        self.widget_44.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_44.setObjectName("widget_44")
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.widget_44)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Finential_statistic1_40 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        self.Finential_statistic1_40.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Finential_statistic1_40.setWordWrap(True)
        self.Finential_statistic1_40.setObjectName("Finential_statistic1_40")
        self.horizontalLayout_14.addWidget(self.Finential_statistic1_40)
        self.Finential_statistic1_41 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        self.Finential_statistic1_41.setStyleSheet("color:white;\n"
"font: 20px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_41.setWordWrap(True)
        self.Finential_statistic1_41.setObjectName("Finential_statistic1_41")
        self.horizontalLayout_14.addWidget(self.Finential_statistic1_41)
        self.frame_18 = QtWidgets.QFrame(self.widget)
        self.frame_18.setGeometry(QtCore.QRect(700, 630, 90, 90))
        self.frame_18.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:45px;\n"
"}")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_18.setObjectName("frame_18")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.frame_19.setStyleSheet("QFrame{\n"
"background-color: black;\n"
"border-radius:35px;\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_19.setObjectName("frame_19")
        self.widget_43 = QtWidgets.QWidget(self.frame_19)
        self.widget_43.setGeometry(QtCore.QRect(10, 10, 71, 51))
        self.widget_43.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_43.setObjectName("widget_43")
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self.widget_43)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.horizontalLayoutWidget_17.setObjectName("horizontalLayoutWidget_17")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.Finential_statistic1_51 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        self.Finential_statistic1_51.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Finential_statistic1_51.setWordWrap(True)
        self.Finential_statistic1_51.setObjectName("Finential_statistic1_51")
        self.horizontalLayout_17.addWidget(self.Finential_statistic1_51)
        self.Finential_statistic1_52 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        self.Finential_statistic1_52.setStyleSheet("color:white;\n"
"font: 20px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_52.setWordWrap(True)
        self.Finential_statistic1_52.setObjectName("Finential_statistic1_52")
        self.horizontalLayout_17.addWidget(self.Finential_statistic1_52)
        self.frame_22 = QtWidgets.QFrame(self.widget)
        self.frame_22.setGeometry(QtCore.QRect(730, 110, 90, 90))
        self.frame_22.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:45px;\n"
"}")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_22.setObjectName("frame_22")
        self.frame_25 = QtWidgets.QFrame(self.frame_22)
        self.frame_25.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.frame_25.setStyleSheet("QFrame{\n"
"background-color: black;\n"
"border-radius:35px;\n"
"}")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_25.setObjectName("frame_25")
        self.widget_42 = QtWidgets.QWidget(self.frame_25)
        self.widget_42.setGeometry(QtCore.QRect(10, 10, 81, 61))
        self.widget_42.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_42.setObjectName("widget_42")
        self.horizontalLayoutWidget_26 = QtWidgets.QWidget(self.widget_42)
        self.horizontalLayoutWidget_26.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.horizontalLayoutWidget_26.setObjectName("horizontalLayoutWidget_26")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_26)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.Finential_statistic1_73 = QtWidgets.QLabel(self.horizontalLayoutWidget_26)
        self.Finential_statistic1_73.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Finential_statistic1_73.setWordWrap(True)
        self.Finential_statistic1_73.setObjectName("Finential_statistic1_73")
        self.horizontalLayout_26.addWidget(self.Finential_statistic1_73)
        self.Finential_statistic1_74 = QtWidgets.QLabel(self.horizontalLayoutWidget_26)
        self.Finential_statistic1_74.setStyleSheet("color:white;\n"
"font: 20px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_74.setWordWrap(True)
        self.Finential_statistic1_74.setObjectName("Finential_statistic1_74")
        self.horizontalLayout_26.addWidget(self.Finential_statistic1_74)
        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setGeometry(QtCore.QRect(1540, 300, 151, 71))
        self.widget_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_11.setObjectName("widget_11")
        self.frame_7 = QtWidgets.QFrame(self.widget_11)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.frame_7.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.widget_22 = QtWidgets.QWidget(self.frame_7)
        self.widget_22.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_22.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.widget_22)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 32, 21))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Finential_statistic1_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.Finential_statistic1_20.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_20.setWordWrap(True)
        self.Finential_statistic1_20.setObjectName("Finential_statistic1_20")
        self.horizontalLayout_8.addWidget(self.Finential_statistic1_20)
        self.Finential_statistic1_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.Finential_statistic1_21.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_21.setWordWrap(True)
        self.Finential_statistic1_21.setObjectName("Finential_statistic1_21")
        self.horizontalLayout_8.addWidget(self.Finential_statistic1_21)
        self.Finential_statistic1_19 = QtWidgets.QLabel(self.widget_11)
        self.Finential_statistic1_19.setGeometry(QtCore.QRect(50, 20, 101, 19))
        self.Finential_statistic1_19.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_19.setWordWrap(True)
        self.Finential_statistic1_19.setObjectName("Finential_statistic1_19")
        self.Finential_statistic1_18 = QtWidgets.QLabel(self.widget_11)
        self.Finential_statistic1_18.setGeometry(QtCore.QRect(60, 40, 41, 20))
        self.Finential_statistic1_18.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_18.setWordWrap(True)
        self.Finential_statistic1_18.setObjectName("Finential_statistic1_18")
        self.widget_12 = QtWidgets.QWidget(self.widget)
        self.widget_12.setGeometry(QtCore.QRect(1620, 240, 151, 81))
        self.widget_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_12.setObjectName("widget_12")
        self.frame_6 = QtWidgets.QFrame(self.widget_12)
        self.frame_6.setGeometry(QtCore.QRect(0, 10, 40, 40))
        self.frame_6.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.widget_24 = QtWidgets.QWidget(self.frame_6)
        self.widget_24.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_24.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayoutWidget_30 = QtWidgets.QWidget(self.widget_24)
        self.horizontalLayoutWidget_30.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_30.setObjectName("horizontalLayoutWidget_30")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_30)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.Finential_statistic1_82 = QtWidgets.QLabel(self.horizontalLayoutWidget_30)
        self.Finential_statistic1_82.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_82.setWordWrap(True)
        self.Finential_statistic1_82.setObjectName("Finential_statistic1_82")
        self.horizontalLayout_30.addWidget(self.Finential_statistic1_82)
        self.Finential_statistic1_85 = QtWidgets.QLabel(self.horizontalLayoutWidget_30)
        self.Finential_statistic1_85.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_85.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_85.setWordWrap(True)
        self.Finential_statistic1_85.setObjectName("Finential_statistic1_85")
        self.horizontalLayout_30.addWidget(self.Finential_statistic1_85)
        self.Finential_statistic1_15 = QtWidgets.QLabel(self.widget_12)
        self.Finential_statistic1_15.setGeometry(QtCore.QRect(60, 0, 101, 19))
        self.Finential_statistic1_15.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_15.setWordWrap(True)
        self.Finential_statistic1_15.setObjectName("Finential_statistic1_15")
        self.Finential_statistic1_14 = QtWidgets.QLabel(self.widget_12)
        self.Finential_statistic1_14.setGeometry(QtCore.QRect(70, 20, 41, 20))
        self.Finential_statistic1_14.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_14.setWordWrap(True)
        self.Finential_statistic1_14.setObjectName("Finential_statistic1_14")
        self.widget_13 = QtWidgets.QWidget(self.widget)
        self.widget_13.setGeometry(QtCore.QRect(1630, 170, 161, 80))
        self.widget_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_13.setObjectName("widget_13")
        self.frame_5 = QtWidgets.QFrame(self.widget_13)
        self.frame_5.setGeometry(QtCore.QRect(0, 20, 40, 40))
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.widget_25 = QtWidgets.QWidget(self.frame_5)
        self.widget_25.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_25.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_25.setObjectName("widget_25")
        self.horizontalLayoutWidget_31 = QtWidgets.QWidget(self.widget_25)
        self.horizontalLayoutWidget_31.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_31.setObjectName("horizontalLayoutWidget_31")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_31)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.Finential_statistic1_86 = QtWidgets.QLabel(self.horizontalLayoutWidget_31)
        self.Finential_statistic1_86.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_86.setWordWrap(True)
        self.Finential_statistic1_86.setObjectName("Finential_statistic1_86")
        self.horizontalLayout_31.addWidget(self.Finential_statistic1_86)
        self.Finential_statistic1_87 = QtWidgets.QLabel(self.horizontalLayoutWidget_31)
        self.Finential_statistic1_87.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_87.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_87.setWordWrap(True)
        self.Finential_statistic1_87.setObjectName("Finential_statistic1_87")
        self.horizontalLayout_31.addWidget(self.Finential_statistic1_87)
        self.Finential_statistic1_11 = QtWidgets.QLabel(self.widget_13)
        self.Finential_statistic1_11.setGeometry(QtCore.QRect(40, 0, 101, 19))
        self.Finential_statistic1_11.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_11.setWordWrap(True)
        self.Finential_statistic1_11.setObjectName("Finential_statistic1_11")
        self.Finential_statistic1_10 = QtWidgets.QLabel(self.widget_13)
        self.Finential_statistic1_10.setGeometry(QtCore.QRect(50, 20, 41, 20))
        self.Finential_statistic1_10.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_10.setWordWrap(True)
        self.Finential_statistic1_10.setObjectName("Finential_statistic1_10")
        self.widget_14 = QtWidgets.QWidget(self.widget)
        self.widget_14.setGeometry(QtCore.QRect(1580, 110, 161, 80))
        self.widget_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_14.setObjectName("widget_14")
        self.frame_4 = QtWidgets.QFrame(self.widget_14)
        self.frame_4.setGeometry(QtCore.QRect(10, 20, 40, 40))
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.widget_26 = QtWidgets.QWidget(self.frame_4)
        self.widget_26.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_26.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayoutWidget_32 = QtWidgets.QWidget(self.widget_26)
        self.horizontalLayoutWidget_32.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_32.setObjectName("horizontalLayoutWidget_32")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_32)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.Finential_statistic1_88 = QtWidgets.QLabel(self.horizontalLayoutWidget_32)
        self.Finential_statistic1_88.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_88.setWordWrap(True)
        self.Finential_statistic1_88.setObjectName("Finential_statistic1_88")
        self.horizontalLayout_32.addWidget(self.Finential_statistic1_88)
        self.Finential_statistic1_89 = QtWidgets.QLabel(self.horizontalLayoutWidget_32)
        self.Finential_statistic1_89.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_89.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_89.setWordWrap(True)
        self.Finential_statistic1_89.setObjectName("Finential_statistic1_89")
        self.horizontalLayout_32.addWidget(self.Finential_statistic1_89)
        self.Finential_statistic1_9 = QtWidgets.QLabel(self.widget_14)
        self.Finential_statistic1_9.setGeometry(QtCore.QRect(60, 20, 41, 20))
        self.Finential_statistic1_9.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_9.setWordWrap(True)
        self.Finential_statistic1_9.setObjectName("Finential_statistic1_9")
        self.Finential_statistic1_8 = QtWidgets.QLabel(self.widget_14)
        self.Finential_statistic1_8.setGeometry(QtCore.QRect(50, 0, 101, 19))
        self.Finential_statistic1_8.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_8.setWordWrap(True)
        self.Finential_statistic1_8.setObjectName("Finential_statistic1_8")
        self.widget_15 = QtWidgets.QWidget(self.widget)
        self.widget_15.setGeometry(QtCore.QRect(1480, 90, 120, 80))
        self.widget_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_15.setObjectName("widget_15")
        self.Finential_statistic1_23 = QtWidgets.QLabel(self.widget_15)
        self.Finential_statistic1_23.setGeometry(QtCore.QRect(60, 20, 41, 20))
        self.Finential_statistic1_23.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_23.setWordWrap(True)
        self.Finential_statistic1_23.setObjectName("Finential_statistic1_23")
        self.frame_8 = QtWidgets.QFrame(self.widget_15)
        self.frame_8.setGeometry(QtCore.QRect(10, 20, 40, 40))
        self.frame_8.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.widget_27 = QtWidgets.QWidget(self.frame_8)
        self.widget_27.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_27.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_27.setObjectName("widget_27")
        self.horizontalLayoutWidget_33 = QtWidgets.QWidget(self.widget_27)
        self.horizontalLayoutWidget_33.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_33.setObjectName("horizontalLayoutWidget_33")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_33)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.Finential_statistic1_90 = QtWidgets.QLabel(self.horizontalLayoutWidget_33)
        self.Finential_statistic1_90.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_90.setWordWrap(True)
        self.Finential_statistic1_90.setObjectName("Finential_statistic1_90")
        self.horizontalLayout_33.addWidget(self.Finential_statistic1_90)
        self.Finential_statistic1_91 = QtWidgets.QLabel(self.horizontalLayoutWidget_33)
        self.Finential_statistic1_91.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_91.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_91.setWordWrap(True)
        self.Finential_statistic1_91.setObjectName("Finential_statistic1_91")
        self.horizontalLayout_33.addWidget(self.Finential_statistic1_91)
        self.Finential_statistic1_22 = QtWidgets.QLabel(self.widget_15)
        self.Finential_statistic1_22.setGeometry(QtCore.QRect(50, 0, 101, 19))
        self.Finential_statistic1_22.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_22.setWordWrap(True)
        self.Finential_statistic1_22.setObjectName("Finential_statistic1_22")
        self.widget_17 = QtWidgets.QWidget(self.widget)
        self.widget_17.setGeometry(QtCore.QRect(1580, 800, 120, 80))
        self.widget_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_17.setObjectName("widget_17")
        self.frame_12 = QtWidgets.QFrame(self.widget_17)
        self.frame_12.setGeometry(QtCore.QRect(60, 0, 40, 40))
        self.frame_12.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.widget_20 = QtWidgets.QWidget(self.frame_12)
        self.widget_20.setGeometry(QtCore.QRect(0, 10, 51, 21))
        self.widget_20.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.widget_20)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(0, 0, 32, 21))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.Finential_statistic1_33 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.Finential_statistic1_33.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_33.setWordWrap(True)
        self.Finential_statistic1_33.setObjectName("Finential_statistic1_33")
        self.horizontalLayout_12.addWidget(self.Finential_statistic1_33)
        self.Finential_statistic1_34 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.Finential_statistic1_34.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_34.setWordWrap(True)
        self.Finential_statistic1_34.setObjectName("Finential_statistic1_34")
        self.horizontalLayout_12.addWidget(self.Finential_statistic1_34)
        self.Finential_statistic1_28 = QtWidgets.QLabel(self.widget_17)
        self.Finential_statistic1_28.setGeometry(QtCore.QRect(0, 0, 101, 19))
        self.Finential_statistic1_28.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_28.setWordWrap(True)
        self.Finential_statistic1_28.setObjectName("Finential_statistic1_28")
        self.Finential_statistic1_35 = QtWidgets.QLabel(self.widget_17)
        self.Finential_statistic1_35.setGeometry(QtCore.QRect(0, 20, 41, 20))
        self.Finential_statistic1_35.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_35.setWordWrap(True)
        self.Finential_statistic1_35.setObjectName("Finential_statistic1_35")
        self.widget_23 = QtWidgets.QWidget(self.widget)
        self.widget_23.setGeometry(QtCore.QRect(1250, 810, 151, 81))
        self.widget_23.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_23.setObjectName("widget_23")
        self.frame_13 = QtWidgets.QFrame(self.widget_23)
        self.frame_13.setGeometry(QtCore.QRect(0, 10, 40, 40))
        self.frame_13.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_13.setObjectName("frame_13")
        self.widget_28 = QtWidgets.QWidget(self.frame_13)
        self.widget_28.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_28.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayoutWidget_34 = QtWidgets.QWidget(self.widget_28)
        self.horizontalLayoutWidget_34.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_34.setObjectName("horizontalLayoutWidget_34")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_34)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.Finential_statistic1_92 = QtWidgets.QLabel(self.horizontalLayoutWidget_34)
        self.Finential_statistic1_92.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_92.setWordWrap(True)
        self.Finential_statistic1_92.setObjectName("Finential_statistic1_92")
        self.horizontalLayout_34.addWidget(self.Finential_statistic1_92)
        self.Finential_statistic1_93 = QtWidgets.QLabel(self.horizontalLayoutWidget_34)
        self.Finential_statistic1_93.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_93.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_93.setWordWrap(True)
        self.Finential_statistic1_93.setObjectName("Finential_statistic1_93")
        self.horizontalLayout_34.addWidget(self.Finential_statistic1_93)
        self.Finential_statistic1_17 = QtWidgets.QLabel(self.widget_23)
        self.Finential_statistic1_17.setGeometry(QtCore.QRect(70, 20, 41, 20))
        self.Finential_statistic1_17.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_17.setWordWrap(True)
        self.Finential_statistic1_17.setObjectName("Finential_statistic1_17")
        self.Finential_statistic1_39 = QtWidgets.QLabel(self.widget_23)
        self.Finential_statistic1_39.setGeometry(QtCore.QRect(60, 0, 81, 19))
        self.Finential_statistic1_39.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_39.setWordWrap(True)
        self.Finential_statistic1_39.setObjectName("Finential_statistic1_39")
        self.widget_29 = QtWidgets.QWidget(self.widget)
        self.widget_29.setGeometry(QtCore.QRect(1180, 870, 151, 81))
        self.widget_29.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_29.setObjectName("widget_29")
        self.frame_17 = QtWidgets.QFrame(self.widget_29)
        self.frame_17.setGeometry(QtCore.QRect(0, 10, 40, 40))
        self.frame_17.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_17.setObjectName("frame_17")
        self.widget_30 = QtWidgets.QWidget(self.frame_17)
        self.widget_30.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_30.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_30.setObjectName("widget_30")
        self.horizontalLayoutWidget_35 = QtWidgets.QWidget(self.widget_30)
        self.horizontalLayoutWidget_35.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_35.setObjectName("horizontalLayoutWidget_35")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_35)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.Finential_statistic1_94 = QtWidgets.QLabel(self.horizontalLayoutWidget_35)
        self.Finential_statistic1_94.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_94.setWordWrap(True)
        self.Finential_statistic1_94.setObjectName("Finential_statistic1_94")
        self.horizontalLayout_35.addWidget(self.Finential_statistic1_94)
        self.Finential_statistic1_95 = QtWidgets.QLabel(self.horizontalLayoutWidget_35)
        self.Finential_statistic1_95.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_95.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_95.setWordWrap(True)
        self.Finential_statistic1_95.setObjectName("Finential_statistic1_95")
        self.horizontalLayout_35.addWidget(self.Finential_statistic1_95)
        self.Finential_statistic1_24 = QtWidgets.QLabel(self.widget_29)
        self.Finential_statistic1_24.setGeometry(QtCore.QRect(50, 50, 41, 20))
        self.Finential_statistic1_24.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_24.setWordWrap(True)
        self.Finential_statistic1_24.setObjectName("Finential_statistic1_24")
        self.Finential_statistic1_36 = QtWidgets.QLabel(self.widget_29)
        self.Finential_statistic1_36.setGeometry(QtCore.QRect(50, 30, 101, 19))
        self.Finential_statistic1_36.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_36.setWordWrap(True)
        self.Finential_statistic1_36.setObjectName("Finential_statistic1_36")
        self.widget_31 = QtWidgets.QWidget(self.widget)
        self.widget_31.setGeometry(QtCore.QRect(1010, 870, 151, 81))
        self.widget_31.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_31.setObjectName("widget_31")
        self.frame_28 = QtWidgets.QFrame(self.widget_31)
        self.frame_28.setGeometry(QtCore.QRect(70, 0, 40, 40))
        self.frame_28.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_28.setObjectName("frame_28")
        self.widget_32 = QtWidgets.QWidget(self.frame_28)
        self.widget_32.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_32.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_32.setObjectName("widget_32")
        self.horizontalLayoutWidget_36 = QtWidgets.QWidget(self.widget_32)
        self.horizontalLayoutWidget_36.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_36.setObjectName("horizontalLayoutWidget_36")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_36)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.Finential_statistic1_96 = QtWidgets.QLabel(self.horizontalLayoutWidget_36)
        self.Finential_statistic1_96.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_96.setWordWrap(True)
        self.Finential_statistic1_96.setObjectName("Finential_statistic1_96")
        self.horizontalLayout_36.addWidget(self.Finential_statistic1_96)
        self.Finential_statistic1_97 = QtWidgets.QLabel(self.horizontalLayoutWidget_36)
        self.Finential_statistic1_97.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_97.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_97.setWordWrap(True)
        self.Finential_statistic1_97.setObjectName("Finential_statistic1_97")
        self.horizontalLayout_36.addWidget(self.Finential_statistic1_97)
        self.Finential_statistic1_25 = QtWidgets.QLabel(self.widget_31)
        self.Finential_statistic1_25.setGeometry(QtCore.QRect(10, 40, 41, 20))
        self.Finential_statistic1_25.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_25.setWordWrap(True)
        self.Finential_statistic1_25.setObjectName("Finential_statistic1_25")
        self.Finential_statistic1_42 = QtWidgets.QLabel(self.widget_31)
        self.Finential_statistic1_42.setGeometry(QtCore.QRect(10, 20, 71, 19))
        self.Finential_statistic1_42.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_42.setWordWrap(True)
        self.Finential_statistic1_42.setObjectName("Finential_statistic1_42")
        self.widget_33 = QtWidgets.QWidget(self.widget)
        self.widget_33.setGeometry(QtCore.QRect(780, 740, 151, 81))
        self.widget_33.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_33.setObjectName("widget_33")
        self.frame_16 = QtWidgets.QFrame(self.widget_33)
        self.frame_16.setGeometry(QtCore.QRect(0, 10, 40, 40))
        self.frame_16.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_16.setObjectName("frame_16")
        self.widget_34 = QtWidgets.QWidget(self.frame_16)
        self.widget_34.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_34.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_34.setObjectName("widget_34")
        self.horizontalLayoutWidget_37 = QtWidgets.QWidget(self.widget_34)
        self.horizontalLayoutWidget_37.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_37.setObjectName("horizontalLayoutWidget_37")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_37)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.Finential_statistic1_98 = QtWidgets.QLabel(self.horizontalLayoutWidget_37)
        self.Finential_statistic1_98.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_98.setWordWrap(True)
        self.Finential_statistic1_98.setObjectName("Finential_statistic1_98")
        self.horizontalLayout_37.addWidget(self.Finential_statistic1_98)
        self.Finential_statistic1_99 = QtWidgets.QLabel(self.horizontalLayoutWidget_37)
        self.Finential_statistic1_99.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_99.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_99.setWordWrap(True)
        self.Finential_statistic1_99.setObjectName("Finential_statistic1_99")
        self.horizontalLayout_37.addWidget(self.Finential_statistic1_99)
        self.Finential_statistic1_37 = QtWidgets.QLabel(self.widget_33)
        self.Finential_statistic1_37.setGeometry(QtCore.QRect(50, 50, 41, 20))
        self.Finential_statistic1_37.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_37.setWordWrap(True)
        self.Finential_statistic1_37.setObjectName("Finential_statistic1_37")
        self.Finential_statistic1_50 = QtWidgets.QLabel(self.widget_33)
        self.Finential_statistic1_50.setGeometry(QtCore.QRect(50, 30, 101, 19))
        self.Finential_statistic1_50.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_50.setWordWrap(True)
        self.Finential_statistic1_50.setObjectName("Finential_statistic1_50")
        self.widget_35 = QtWidgets.QWidget(self.widget)
        self.widget_35.setGeometry(QtCore.QRect(590, 740, 151, 81))
        self.widget_35.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_35.setObjectName("widget_35")
        self.frame_20 = QtWidgets.QFrame(self.widget_35)
        self.frame_20.setGeometry(QtCore.QRect(70, 0, 40, 40))
        self.frame_20.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_20.setObjectName("frame_20")
        self.widget_36 = QtWidgets.QWidget(self.frame_20)
        self.widget_36.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_36.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_36.setObjectName("widget_36")
        self.horizontalLayoutWidget_38 = QtWidgets.QWidget(self.widget_36)
        self.horizontalLayoutWidget_38.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_38.setObjectName("horizontalLayoutWidget_38")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_38)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.Finential_statistic1_100 = QtWidgets.QLabel(self.horizontalLayoutWidget_38)
        self.Finential_statistic1_100.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_100.setWordWrap(True)
        self.Finential_statistic1_100.setObjectName("Finential_statistic1_100")
        self.horizontalLayout_38.addWidget(self.Finential_statistic1_100)
        self.Finential_statistic1_101 = QtWidgets.QLabel(self.horizontalLayoutWidget_38)
        self.Finential_statistic1_101.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_101.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_101.setWordWrap(True)
        self.Finential_statistic1_101.setObjectName("Finential_statistic1_101")
        self.horizontalLayout_38.addWidget(self.Finential_statistic1_101)
        self.Finential_statistic1_38 = QtWidgets.QLabel(self.widget_35)
        self.Finential_statistic1_38.setGeometry(QtCore.QRect(10, 40, 41, 20))
        self.Finential_statistic1_38.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_38.setWordWrap(True)
        self.Finential_statistic1_38.setObjectName("Finential_statistic1_38")
        self.Finential_statistic1_53 = QtWidgets.QLabel(self.widget_35)
        self.Finential_statistic1_53.setGeometry(QtCore.QRect(10, 30, 71, 19))
        self.Finential_statistic1_53.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_53.setWordWrap(True)
        self.Finential_statistic1_53.setObjectName("Finential_statistic1_53")
        self.widget_37 = QtWidgets.QWidget(self.widget)
        self.widget_37.setGeometry(QtCore.QRect(660, 220, 131, 141))
        self.widget_37.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_37.setObjectName("widget_37")
        self.frame_29 = QtWidgets.QFrame(self.widget_37)
        self.frame_29.setGeometry(QtCore.QRect(40, 10, 40, 40))
        self.frame_29.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_29.setObjectName("frame_29")
        self.widget_39 = QtWidgets.QWidget(self.frame_29)
        self.widget_39.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_39.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_39.setObjectName("widget_39")
        self.horizontalLayoutWidget_40 = QtWidgets.QWidget(self.widget_39)
        self.horizontalLayoutWidget_40.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_40.setObjectName("horizontalLayoutWidget_40")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_40)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.Finential_statistic1_104 = QtWidgets.QLabel(self.horizontalLayoutWidget_40)
        self.Finential_statistic1_104.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_104.setWordWrap(True)
        self.Finential_statistic1_104.setObjectName("Finential_statistic1_104")
        self.horizontalLayout_40.addWidget(self.Finential_statistic1_104)
        self.Finential_statistic1_105 = QtWidgets.QLabel(self.horizontalLayoutWidget_40)
        self.Finential_statistic1_105.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_105.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_105.setWordWrap(True)
        self.Finential_statistic1_105.setObjectName("Finential_statistic1_105")
        self.horizontalLayout_40.addWidget(self.Finential_statistic1_105)
        self.Finential_statistic1_80 = QtWidgets.QLabel(self.widget_37)
        self.Finential_statistic1_80.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.Finential_statistic1_80.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_80.setWordWrap(True)
        self.Finential_statistic1_80.setObjectName("Finential_statistic1_80")
        self.Finential_statistic1_81 = QtWidgets.QLabel(self.widget_37)
        self.Finential_statistic1_81.setGeometry(QtCore.QRect(10, 90, 41, 20))
        self.Finential_statistic1_81.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_81.setWordWrap(True)
        self.Finential_statistic1_81.setObjectName("Finential_statistic1_81")
        self.widget_40 = QtWidgets.QWidget(self.widget)
        self.widget_40.setGeometry(QtCore.QRect(600, 80, 121, 121))
        self.widget_40.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.widget_40.setObjectName("widget_40")
        self.frame_30 = QtWidgets.QFrame(self.widget_40)
        self.frame_30.setGeometry(QtCore.QRect(60, 10, 40, 40))
        self.frame_30.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_30.setObjectName("frame_30")
        self.widget_41 = QtWidgets.QWidget(self.frame_30)
        self.widget_41.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_41.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_41.setObjectName("widget_41")
        self.horizontalLayoutWidget_41 = QtWidgets.QWidget(self.widget_41)
        self.horizontalLayoutWidget_41.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_41.setObjectName("horizontalLayoutWidget_41")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_41)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.Finential_statistic1_106 = QtWidgets.QLabel(self.horizontalLayoutWidget_41)
        self.Finential_statistic1_106.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_106.setWordWrap(True)
        self.Finential_statistic1_106.setObjectName("Finential_statistic1_106")
        self.horizontalLayout_41.addWidget(self.Finential_statistic1_106)
        self.Finential_statistic1_107 = QtWidgets.QLabel(self.horizontalLayoutWidget_41)
        self.Finential_statistic1_107.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_107.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_107.setWordWrap(True)
        self.Finential_statistic1_107.setObjectName("Finential_statistic1_107")
        self.horizontalLayout_41.addWidget(self.Finential_statistic1_107)
        self.Finential_statistic1_109 = QtWidgets.QLabel(self.widget_40)
        self.Finential_statistic1_109.setGeometry(QtCore.QRect(10, 80, 41, 20))
        self.Finential_statistic1_109.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_109.setWordWrap(True)
        self.Finential_statistic1_109.setObjectName("Finential_statistic1_109")
        self.Finential_statistic1_60 = QtWidgets.QLabel(self.widget_40)
        self.Finential_statistic1_60.setGeometry(QtCore.QRect(10, 60, 101, 19))
        self.Finential_statistic1_60.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_60.setWordWrap(True)
        self.Finential_statistic1_60.setObjectName("Finential_statistic1_60")
        self.widget_46 = QtWidgets.QWidget(self.widget)
        self.widget_46.setGeometry(QtCore.QRect(1780, 69, 120, 111))
        self.widget_46.setStyleSheet("background-color: rgb(2, 13, 87);\n"
"border-radius:20px;")
        self.widget_46.setObjectName("widget_46")
        self.Advertising_2 = QtWidgets.QLabel(self.widget_46)
        self.Advertising_2.setGeometry(QtCore.QRect(20, 0, 91, 41))
        self.Advertising_2.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_2.setWordWrap(True)
        self.Advertising_2.setObjectName("Advertising_2")
        self.Advertising_3 = QtWidgets.QLabel(self.widget_46)
        self.Advertising_3.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.Advertising_3.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;")
        self.Advertising_3.setWordWrap(True)
        self.Advertising_3.setObjectName("Advertising_3")
        self.Advertising_4 = QtWidgets.QLabel(self.widget_46)
        self.Advertising_4.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.Advertising_4.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;")
        self.Advertising_4.setWordWrap(True)
        self.Advertising_4.setObjectName("Advertising_4")
        self.widget_48 = QtWidgets.QWidget(self.widget)
        self.widget_48.setGeometry(QtCore.QRect(1780, 190, 120, 361))
        self.widget_48.setStyleSheet("background-color: rgb(2, 13, 87);\n"
"border-radius:20px;")
        self.widget_48.setObjectName("widget_48")
        self.Advertising_6 = QtWidgets.QLabel(self.widget_48)
        self.Advertising_6.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.Advertising_6.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 23px;\n"
"text-align: center;\n"
"")
        self.Advertising_6.setWordWrap(True)
        self.Advertising_6.setObjectName("Advertising_6")
        self.Advertising_5 = QtWidgets.QLabel(self.widget_48)
        self.Advertising_5.setGeometry(QtCore.QRect(20, 0, 71, 31))
        self.Advertising_5.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 15px;\n"
"text-align: center;\n"
"")
        self.Advertising_5.setWordWrap(True)
        self.Advertising_5.setObjectName("Advertising_5")
        self.widget_47 = QtWidgets.QWidget(self.widget_48)
        self.widget_47.setGeometry(QtCore.QRect(-10, 60, 131, 261))
        self.widget_47.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_47.setObjectName("widget_47")
        self.Advertising_7 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_7.setGeometry(QtCore.QRect(20, 10, 21, 31))
        self.Advertising_7.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_7.setWordWrap(True)
        self.Advertising_7.setObjectName("Advertising_7")
        self.progressBar = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar.setGeometry(QtCore.QRect(50, 20, 71, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_2.setGeometry(QtCore.QRect(50, 40, 71, 16))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setFormat("")
        self.progressBar_2.setObjectName("progressBar_2")
        self.Advertising_8 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_8.setGeometry(QtCore.QRect(20, 30, 21, 31))
        self.Advertising_8.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_8.setWordWrap(True)
        self.Advertising_8.setObjectName("Advertising_8")
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_3.setGeometry(QtCore.QRect(50, 60, 71, 16))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setFormat("")
        self.progressBar_3.setObjectName("progressBar_3")
        self.Advertising_9 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_9.setGeometry(QtCore.QRect(20, 50, 21, 31))
        self.Advertising_9.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_9.setWordWrap(True)
        self.Advertising_9.setObjectName("Advertising_9")
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_4.setGeometry(QtCore.QRect(50, 80, 71, 16))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setFormat("")
        self.progressBar_4.setObjectName("progressBar_4")
        self.Advertising_10 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_10.setGeometry(QtCore.QRect(20, 70, 21, 31))
        self.Advertising_10.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_10.setWordWrap(True)
        self.Advertising_10.setObjectName("Advertising_10")
        self.Advertising_11 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_11.setGeometry(QtCore.QRect(20, 90, 21, 31))
        self.Advertising_11.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_11.setWordWrap(True)
        self.Advertising_11.setObjectName("Advertising_11")
        self.progressBar_5 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_5.setGeometry(QtCore.QRect(50, 100, 71, 16))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setFormat("")
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_6.setGeometry(QtCore.QRect(50, 200, 71, 16))
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setFormat("")
        self.progressBar_6.setObjectName("progressBar_6")
        self.progressBar_7 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_7.setGeometry(QtCore.QRect(50, 160, 71, 16))
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setFormat("")
        self.progressBar_7.setObjectName("progressBar_7")
        self.Advertising_12 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_12.setGeometry(QtCore.QRect(20, 130, 21, 31))
        self.Advertising_12.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_12.setWordWrap(True)
        self.Advertising_12.setObjectName("Advertising_12")
        self.Advertising_13 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_13.setGeometry(QtCore.QRect(20, 170, 21, 31))
        self.Advertising_13.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_13.setWordWrap(True)
        self.Advertising_13.setObjectName("Advertising_13")
        self.progressBar_8 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_8.setGeometry(QtCore.QRect(50, 180, 71, 16))
        self.progressBar_8.setProperty("value", 24)
        self.progressBar_8.setFormat("")
        self.progressBar_8.setObjectName("progressBar_8")
        self.progressBar_9 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_9.setGeometry(QtCore.QRect(50, 120, 71, 16))
        self.progressBar_9.setProperty("value", 24)
        self.progressBar_9.setFormat("")
        self.progressBar_9.setObjectName("progressBar_9")
        self.Advertising_14 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_14.setGeometry(QtCore.QRect(20, 150, 21, 31))
        self.Advertising_14.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_14.setWordWrap(True)
        self.Advertising_14.setObjectName("Advertising_14")
        self.Advertising_15 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_15.setGeometry(QtCore.QRect(20, 190, 21, 31))
        self.Advertising_15.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_15.setWordWrap(True)
        self.Advertising_15.setObjectName("Advertising_15")
        self.progressBar_10 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_10.setGeometry(QtCore.QRect(50, 140, 71, 16))
        self.progressBar_10.setProperty("value", 24)
        self.progressBar_10.setFormat("")
        self.progressBar_10.setObjectName("progressBar_10")
        self.Advertising_16 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_16.setGeometry(QtCore.QRect(20, 110, 21, 31))
        self.Advertising_16.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_16.setWordWrap(True)
        self.Advertising_16.setObjectName("Advertising_16")
        self.Advertising_17 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_17.setGeometry(QtCore.QRect(20, 210, 21, 31))
        self.Advertising_17.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_17.setWordWrap(True)
        self.Advertising_17.setObjectName("Advertising_17")
        self.progressBar_11 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_11.setGeometry(QtCore.QRect(50, 220, 71, 16))
        self.progressBar_11.setProperty("value", 24)
        self.progressBar_11.setFormat("")
        self.progressBar_11.setObjectName("progressBar_11")
        self.Advertising_18 = QtWidgets.QLabel(self.widget_47)
        self.Advertising_18.setGeometry(QtCore.QRect(20, 230, 21, 31))
        self.Advertising_18.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"text-align: center;\n"
"")
        self.Advertising_18.setWordWrap(True)
        self.Advertising_18.setObjectName("Advertising_18")
        self.progressBar_12 = QtWidgets.QProgressBar(self.widget_47)
        self.progressBar_12.setGeometry(QtCore.QRect(50, 240, 71, 16))
        self.progressBar_12.setProperty("value", 24)
        self.progressBar_12.setFormat("")
        self.progressBar_12.setObjectName("progressBar_12")
        self.Advertising_19 = QtWidgets.QLabel(self.widget_48)
        self.Advertising_19.setGeometry(QtCore.QRect(60, 340, 91, 61))
        self.Advertising_19.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_19.setWordWrap(True)
        self.Advertising_19.setObjectName("Advertising_19")
        self.Advertising_20 = QtWidgets.QLabel(self.widget_48)
        self.Advertising_20.setGeometry(QtCore.QRect(20, 320, 91, 41))
        self.Advertising_20.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_20.setWordWrap(True)
        self.Advertising_20.setObjectName("Advertising_20")
        self.widget_49 = QtWidgets.QWidget(self.widget)
        self.widget_49.setGeometry(QtCore.QRect(1780, 570, 120, 391))
        self.widget_49.setStyleSheet("background-color: rgb(2, 13, 87);\n"
"border-radius:20px;")
        self.widget_49.setObjectName("widget_49")
        self.Advertising_21 = QtWidgets.QLabel(self.widget_49)
        self.Advertising_21.setGeometry(QtCore.QRect(30, 10, 71, 41))
        self.Advertising_21.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 30px;\n"
"text-align: center;\n"
"")
        self.Advertising_21.setWordWrap(True)
        self.Advertising_21.setObjectName("Advertising_21")
        self.Advertising_22 = QtWidgets.QLabel(self.widget_49)
        self.Advertising_22.setGeometry(QtCore.QRect(20, 50, 91, 41))
        self.Advertising_22.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_22.setWordWrap(True)
        self.Advertising_22.setObjectName("Advertising_22")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_49)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 81, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Advertising_23 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Advertising_23.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_23.setWordWrap(True)
        self.Advertising_23.setObjectName("Advertising_23")
        self.horizontalLayout_5.addWidget(self.Advertising_23)
        self.Advertising_24 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Advertising_24.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_24.setWordWrap(True)
        self.Advertising_24.setObjectName("Advertising_24")
        self.horizontalLayout_5.addWidget(self.Advertising_24)
        self.frame_26 = QtWidgets.QFrame(self.widget_49)
        self.frame_26.setGeometry(QtCore.QRect(10, 130, 100, 100))
        self.frame_26.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(0, 184, 200, 255), stop:0.75 rgba(0, 34, 255, 255));\n"
"border-radius:50px;\n"
"")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.widget_50 = QtWidgets.QWidget(self.frame_26)
        self.widget_50.setGeometry(QtCore.QRect(10, 10, 80, 80))
        self.widget_50.setStyleSheet("background-color: rgb(2, 13, 87);\n"
"border-radius:40px;")
        self.widget_50.setObjectName("widget_50")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_49)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 240, 81, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Advertising_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Advertising_25.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_25.setWordWrap(True)
        self.Advertising_25.setObjectName("Advertising_25")
        self.horizontalLayout_6.addWidget(self.Advertising_25)
        self.Advertising_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Advertising_26.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_26.setWordWrap(True)
        self.Advertising_26.setObjectName("Advertising_26")
        self.horizontalLayout_6.addWidget(self.Advertising_26)
        self.Advertising_27 = QtWidgets.QLabel(self.widget_49)
        self.Advertising_27.setGeometry(QtCore.QRect(30, 280, 91, 41))
        self.Advertising_27.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 20px;\n"
"text-align: center;\n"
"")
        self.Advertising_27.setWordWrap(True)
        self.Advertising_27.setObjectName("Advertising_27")
        self.Advertising_28 = QtWidgets.QLabel(self.widget_49)
        self.Advertising_28.setGeometry(QtCore.QRect(30, 330, 71, 41))
        self.Advertising_28.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 30px;\n"
"text-align: center;\n"
"")
        self.Advertising_28.setWordWrap(True)
        self.Advertising_28.setObjectName("Advertising_28")
        self.widget_16 = QtWidgets.QWidget(self.widget)
        self.widget_16.setGeometry(QtCore.QRect(1670, 700, 91, 80))
        self.widget_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_16.setObjectName("widget_16")
        self.Finential_statistic1_32 = QtWidgets.QLabel(self.widget_16)
        self.Finential_statistic1_32.setGeometry(QtCore.QRect(0, 0, 41, 20))
        self.Finential_statistic1_32.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_32.setWordWrap(True)
        self.Finential_statistic1_32.setObjectName("Finential_statistic1_32")
        self.frame_11 = QtWidgets.QFrame(self.widget_16)
        self.frame_11.setGeometry(QtCore.QRect(10, 40, 40, 40))
        self.frame_11.setStyleSheet("QFrame{\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:20px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.widget_21 = QtWidgets.QWidget(self.frame_11)
        self.widget_21.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.widget_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.widget_21)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 36, 21))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Finential_statistic1_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.Finential_statistic1_29.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_29.setWordWrap(True)
        self.Finential_statistic1_29.setObjectName("Finential_statistic1_29")
        self.horizontalLayout_11.addWidget(self.Finential_statistic1_29)
        self.Finential_statistic1_30 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.Finential_statistic1_30.setStyleSheet("color:white;\n"
"font: 10px;\n"
"background-color:rgba(255, 255, 255, 0);")
        self.Finential_statistic1_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Finential_statistic1_30.setWordWrap(True)
        self.Finential_statistic1_30.setObjectName("Finential_statistic1_30")
        self.horizontalLayout_11.addWidget(self.Finential_statistic1_30)
        self.Finential_statistic1_31 = QtWidgets.QLabel(self.widget_16)
        self.Finential_statistic1_31.setGeometry(QtCore.QRect(0, 20, 101, 19))
        self.Finential_statistic1_31.setStyleSheet("color:white;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10px;\n"
"padding-left:5px;\n"
"text-align: right;")
        self.Finential_statistic1_31.setWordWrap(True)
        self.Finential_statistic1_31.setObjectName("Finential_statistic1_31")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1900, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "2020"))
        self.pushButton_2.setText(_translate("MainWindow", "2021"))
        self.pushButton_5.setText(_translate("MainWindow", "2022"))
        self.pushButton_6.setText(_translate("MainWindow", "2023"))
        self.pushButton_7.setText(_translate("MainWindow", "2024"))
        self.Finential_statistic1.setText(_translate("MainWindow", "920,120"))
        self.label_2.setText(_translate("MainWindow", "Finencial Statistic"))
        self.pushButton_3.setText(_translate("MainWindow", "Income Sources"))
        self.label.setText(_translate("MainWindow", "Some not intresting text about somethink  that nobody will read"))
        self.label_3.setText(_translate("MainWindow", "Income Torgets "))
        self.Finential_statistic2.setText(_translate("MainWindow", "720,883"))
        self.label_4.setText(_translate("MainWindow", "Income Achived"))
        self.Finential_statistic1_2.setText(_translate("MainWindow", "80"))
        self.Finential_statistic1_3.setText(_translate("MainWindow", "%"))
        self.label_5.setText(_translate("MainWindow", "Asset sale"))
        self.Asset_sale.setText(_translate("MainWindow", "77,422"))
        self.label_7.setText(_translate("MainWindow", "Advertising"))
        self.Advertising.setText(_translate("MainWindow", "117,541"))
        self.label_8.setText(_translate("MainWindow", "Subscription"))
        self.Subscription.setText(_translate("MainWindow", "130,229"))
        self.label_9.setText(_translate("MainWindow", "Licencing"))
        self.Licencing.setText(_translate("MainWindow", "157,387"))
        self.label_10.setText(_translate("MainWindow", "Usage fees"))
        self.Usage_fees.setText(_translate("MainWindow", "177,100"))
        self.label_11.setText(_translate("MainWindow", "Renting"))
        self.Licencing_2.setText(_translate("MainWindow", "61,204"))
        self.Finential_statistic1_4.setText(_translate("MainWindow", "16"))
        self.Finential_statistic1_5.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_26.setText(_translate("MainWindow", "15"))
        self.Finential_statistic1_27.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_40.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_41.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_51.setText(_translate("MainWindow", "21"))
        self.Finential_statistic1_52.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_73.setText(_translate("MainWindow", "21"))
        self.Finential_statistic1_74.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_20.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_21.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_19.setText(_translate("MainWindow", "YouTube Chanal"))
        self.Finential_statistic1_18.setText(_translate("MainWindow", "56,222"))
        self.Finential_statistic1_82.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_85.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_15.setText(_translate("MainWindow", "Google Ad"))
        self.Finential_statistic1_14.setText(_translate("MainWindow", "5,300"))
        self.Finential_statistic1_86.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_87.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_11.setText(_translate("MainWindow", "Facbook Page"))
        self.Finential_statistic1_10.setText(_translate("MainWindow", "2,430"))
        self.Finential_statistic1_88.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_89.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_9.setText(_translate("MainWindow", "2,430"))
        self.Finential_statistic1_8.setText(_translate("MainWindow", "Company Webside"))
        self.Finential_statistic1_23.setText(_translate("MainWindow", "56,700"))
        self.Finential_statistic1_90.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_91.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_22.setText(_translate("MainWindow", "Television Ad"))
        self.Finential_statistic1_33.setText(_translate("MainWindow", "9"))
        self.Finential_statistic1_34.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_28.setText(_translate("MainWindow", "Prime"))
        self.Finential_statistic1_35.setText(_translate("MainWindow", "71,220"))
        self.Finential_statistic1_92.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_93.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_17.setText(_translate("MainWindow", "5,300"))
        self.Finential_statistic1_39.setText(_translate("MainWindow", "Equpments"))
        self.Finential_statistic1_94.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_95.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_24.setText(_translate("MainWindow", "5,300"))
        self.Finential_statistic1_36.setText(_translate("MainWindow", "Lands"))
        self.Finential_statistic1_96.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_97.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_25.setText(_translate("MainWindow", "5,300"))
        self.Finential_statistic1_42.setText(_translate("MainWindow", "Offices"))
        self.Finential_statistic1_98.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_99.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_37.setText(_translate("MainWindow", "5,300"))
        self.Finential_statistic1_50.setText(_translate("MainWindow", "Reneval"))
        self.Finential_statistic1_100.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_101.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_38.setText(_translate("MainWindow", "5,300"))
        self.Finential_statistic1_53.setText(_translate("MainWindow", "New"))
        self.Finential_statistic1_104.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_105.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_80.setText(_translate("MainWindow", "Software Metered Licence"))
        self.Finential_statistic1_81.setText(_translate("MainWindow", "99,500"))
        self.Finential_statistic1_106.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_107.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_109.setText(_translate("MainWindow", "99,500"))
        self.Finential_statistic1_60.setText(_translate("MainWindow", "Floatin License"))
        self.Advertising_2.setText(_translate("MainWindow", "69,541"))
        self.Advertising_3.setText(_translate("MainWindow", "Average"))
        self.Advertising_4.setText(_translate("MainWindow", "Manthly income"))
        self.Advertising_6.setText(_translate("MainWindow", "Profits"))
        self.Advertising_5.setText(_translate("MainWindow", "Operating"))
        self.Advertising_7.setText(_translate("MainWindow", "Dec"))
        self.Advertising_8.setText(_translate("MainWindow", "Nov"))
        self.Advertising_9.setText(_translate("MainWindow", "Oct"))
        self.Advertising_10.setText(_translate("MainWindow", "Sep"))
        self.Advertising_11.setText(_translate("MainWindow", "Aug"))
        self.Advertising_12.setText(_translate("MainWindow", "Jun"))
        self.Advertising_13.setText(_translate("MainWindow", "Apr"))
        self.Advertising_14.setText(_translate("MainWindow", "May"))
        self.Advertising_15.setText(_translate("MainWindow", "Mar"))
        self.Advertising_16.setText(_translate("MainWindow", "Jul"))
        self.Advertising_17.setText(_translate("MainWindow", "Feb"))
        self.Advertising_18.setText(_translate("MainWindow", "ian"))
        self.Advertising_19.setText(_translate("MainWindow", "69,541"))
        self.Advertising_20.setText(_translate("MainWindow", "169,541"))
        self.Advertising_21.setText(_translate("MainWindow", "B2B"))
        self.Advertising_22.setText(_translate("MainWindow", "714,241"))
        self.Advertising_23.setText(_translate("MainWindow", "86.16"))
        self.Advertising_24.setText(_translate("MainWindow", "%"))
        self.Advertising_25.setText(_translate("MainWindow", "86.16"))
        self.Advertising_26.setText(_translate("MainWindow", "%"))
        self.Advertising_27.setText(_translate("MainWindow", "714,241"))
        self.Advertising_28.setText(_translate("MainWindow", "B2C"))
        self.Finential_statistic1_32.setText(_translate("MainWindow", "59,300"))
        self.Finential_statistic1_29.setText(_translate("MainWindow", "7"))
        self.Finential_statistic1_30.setText(_translate("MainWindow", "%"))
        self.Finential_statistic1_31.setText(_translate("MainWindow", "Premium"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())