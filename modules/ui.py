# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setMinimumSize(QtCore.QSize(800, 640))
        MainWindow.setMaximumSize(QtCore.QSize(800, 640))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 340, 351, 231))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 150, 178, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.if_end_do = QtWidgets.QComboBox(self.layoutWidget)
        self.if_end_do.setEditable(True)
        self.if_end_do.setObjectName("if_end_do")
        self.if_end_do.addItem("")
        self.if_end_do.addItem("")
        self.if_end_do.addItem("")
        self.if_end_do.addItem("")
        self.horizontalLayout_11.addWidget(self.if_end_do)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 120, 228, 18))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.template_matching = QtWidgets.QRadioButton(self.layoutWidget1)
        self.template_matching.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.template_matching.setChecked(True)
        self.template_matching.setObjectName("template_matching")
        self.horizontalLayout_10.addWidget(self.template_matching)
        self.sift_matching = QtWidgets.QRadioButton(self.layoutWidget1)
        self.sift_matching.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sift_matching.setObjectName("sift_matching")
        self.horizontalLayout_10.addWidget(self.sift_matching)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 81, 311, 24))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.image_compression = QtWidgets.QSlider(self.layoutWidget2)
        self.image_compression.setMinimum(40)
        self.image_compression.setMaximum(100)
        self.image_compression.setProperty("value", 80)
        self.image_compression.setSliderPosition(80)
        self.image_compression.setOrientation(QtCore.Qt.Horizontal)
        self.image_compression.setInvertedAppearance(False)
        self.image_compression.setInvertedControls(False)
        self.image_compression.setObjectName("image_compression")
        self.horizontalLayout_9.addWidget(self.image_compression)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(13, 42, 264, 18))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.runmod_nomal = QtWidgets.QRadioButton(self.layoutWidget3)
        self.runmod_nomal.setChecked(True)
        self.runmod_nomal.setObjectName("runmod_nomal")
        self.gridLayout.addWidget(self.runmod_nomal, 0, 1, 1, 1)
        self.runmod_compatibility = QtWidgets.QRadioButton(self.layoutWidget3)
        self.runmod_compatibility.setObjectName("runmod_compatibility")
        self.gridLayout.addWidget(self.runmod_compatibility, 0, 2, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 190, 139, 18))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.debug = QtWidgets.QCheckBox(self.layoutWidget4)
        self.debug.setObjectName("debug")
        self.horizontalLayout_8.addWidget(self.debug)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 0, 20, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 351, 301))
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 260, 194, 22))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.click_deviation = QtWidgets.QSpinBox(self.layoutWidget5)
        self.click_deviation.setMinimumSize(QtCore.QSize(60, 0))
        self.click_deviation.setMinimum(3)
        self.click_deviation.setMaximum(50)
        self.click_deviation.setProperty("value", 10)
        self.click_deviation.setDisplayIntegerBase(10)
        self.click_deviation.setObjectName("click_deviation")
        self.horizontalLayout_7.addWidget(self.click_deviation)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 220, 190, 22))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.interval_seconds = QtWidgets.QDoubleSpinBox(self.layoutWidget6)
        self.interval_seconds.setMinimumSize(QtCore.QSize(60, 0))
        self.interval_seconds.setMinimum(1.0)
        self.interval_seconds.setMaximum(600.0)
        self.interval_seconds.setSingleStep(0.5)
        self.interval_seconds.setProperty("value", 5.0)
        self.interval_seconds.setObjectName("interval_seconds")
        self.horizontalLayout_6.addWidget(self.interval_seconds)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.layoutWidget7 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 180, 212, 22))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.loop_min = QtWidgets.QDoubleSpinBox(self.layoutWidget7)
        self.loop_min.setMinimumSize(QtCore.QSize(80, 0))
        self.loop_min.setMinimum(1.0)
        self.loop_min.setMaximum(600.0)
        self.loop_min.setSingleStep(0.5)
        self.loop_min.setProperty("value", 120.0)
        self.loop_min.setObjectName("loop_min")
        self.horizontalLayout_5.addWidget(self.loop_min)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.layoutWidget8 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget8.setGeometry(QtCore.QRect(10, 110, 154, 22))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.select_target_path_mode_combobox = QtWidgets.QComboBox(self.layoutWidget8)
        self.select_target_path_mode_combobox.setEditable(True)
        self.select_target_path_mode_combobox.setObjectName("select_target_path_mode_combobox")
        self.select_target_path_mode_combobox.addItem("")
        self.select_target_path_mode_combobox.addItem("")
        self.select_target_path_mode_combobox.addItem("")
        self.select_target_path_mode_combobox.addItem("")
        self.select_target_path_mode_combobox.addItem("")
        self.select_target_path_mode_combobox.addItem("")
        self.horizontalLayout_3.addWidget(self.select_target_path_mode_combobox)
        self.layoutWidget9 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget9.setGeometry(QtCore.QRect(10, 70, 282, 25))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget9)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.show_handle_title = QtWidgets.QLineEdit(self.layoutWidget9)
        self.show_handle_title.setObjectName("show_handle_title")
        self.horizontalLayout_2.addWidget(self.show_handle_title)
        self.btn_select_handle = QtWidgets.QPushButton(self.layoutWidget9)
        self.btn_select_handle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_select_handle.setObjectName("btn_select_handle")
        self.horizontalLayout_2.addWidget(self.btn_select_handle)
        self.layoutWidget10 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget10.setGeometry(QtCore.QRect(10, 30, 282, 18))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget10)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.rd_btn_windows_mod = QtWidgets.QRadioButton(self.layoutWidget10)
        self.rd_btn_windows_mod.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rd_btn_windows_mod.setChecked(True)
        self.rd_btn_windows_mod.setObjectName("rd_btn_windows_mod")
        self.horizontalLayout.addWidget(self.rd_btn_windows_mod)
        self.rd_btn_android_adb = QtWidgets.QRadioButton(self.layoutWidget10)
        self.rd_btn_android_adb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rd_btn_android_adb.setObjectName("rd_btn_android_adb")
        self.horizontalLayout.addWidget(self.rd_btn_android_adb)
        self.layoutWidget11 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget11.setGeometry(QtCore.QRect(80, 140, 216, 25))
        self.layoutWidget11.setObjectName("layoutWidget11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.show_target_path = QtWidgets.QLineEdit(self.layoutWidget11)
        self.show_target_path.setReadOnly(True)
        self.show_target_path.setObjectName("show_target_path")
        self.horizontalLayout_4.addWidget(self.show_target_path)
        self.select_targetpic_path_btn = QtWidgets.QPushButton(self.layoutWidget11)
        self.select_targetpic_path_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_targetpic_path_btn.setObjectName("select_targetpic_path_btn")
        self.horizontalLayout_4.addWidget(self.select_targetpic_path_btn)
        self.layoutWidget12 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget12.setGeometry(QtCore.QRect(400, 90, 381, 481))
        self.layoutWidget12.setObjectName("layoutWidget12")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget12)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget12)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.run_log = QtWidgets.QTextEdit(self.layoutWidget12)
        self.run_log.setObjectName("run_log")
        self.verticalLayout.addWidget(self.run_log)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 580, 801, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(20, 600, 75, 23))
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_resume = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resume.setGeometry(QtCore.QRect(710, 600, 75, 23))
        self.btn_resume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_resume.setObjectName("btn_resume")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(629, 600, 75, 23))
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pause.setGeometry(QtCore.QRect(710, 600, 75, 23))
        self.btn_pause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(711, 600, 75, 23))
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setObjectName("btn_start")
        self.layoutWidget13 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget13.setGeometry(QtCore.QRect(400, 30, 381, 40))
        self.layoutWidget13.setObjectName("layoutWidget13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget13)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget13)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.loop_progress = QtWidgets.QProgressBar(self.layoutWidget13)
        self.loop_progress.setProperty("value", 24)
        self.loop_progress.setObjectName("loop_progress")
        self.verticalLayout_2.addWidget(self.loop_progress)
        self.btn_exit.raise_()
        self.btn_resume.raise_()
        self.btn_stop.raise_()
        self.btn_pause.raise_()
        self.btn_start.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.line.raise_()
        self.line_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.rd_btn_android_adb.clicked['bool'].connect(self.show_handle_title.setDisabled)
        self.rd_btn_windows_mod.clicked['bool'].connect(self.show_handle_title.setEnabled)
        self.rd_btn_windows_mod.clicked['bool'].connect(self.btn_select_handle.setEnabled)
        self.rd_btn_android_adb.clicked['bool'].connect(self.btn_select_handle.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "高级设置"))
        self.label_10.setText(_translate("MainWindow", "完成后："))
        self.if_end_do.setCurrentText(_translate("MainWindow", "不执行任何操作"))
        self.if_end_do.setPlaceholderText(_translate("MainWindow", "请选择功能"))
        self.if_end_do.setItemText(0, _translate("MainWindow", "不执行任何操作"))
        self.if_end_do.setItemText(1, _translate("MainWindow", "电脑关机"))
        self.if_end_do.setItemText(2, _translate("MainWindow", "关闭匹配目标窗体"))
        self.if_end_do.setItemText(3, _translate("MainWindow", "关闭脚本"))
        self.label_9.setText(_translate("MainWindow", "匹配方法："))
        self.template_matching.setText(_translate("MainWindow", "模板匹配"))
        self.sift_matching.setText(_translate("MainWindow", "特征点匹配"))
        self.label_8.setText(_translate("MainWindow", "压缩截图："))
        self.label_7.setText(_translate("MainWindow", "运行模式："))
        self.runmod_nomal.setText(_translate("MainWindow", "正常-可后台"))
        self.runmod_compatibility.setText(_translate("MainWindow", "兼容-不可后台"))
        self.label_11.setText(_translate("MainWindow", "调试模式："))
        self.debug.setText(_translate("MainWindow", "开启调试"))
        self.groupBox_2.setTitle(_translate("MainWindow", "基础设置"))
        self.label_18.setText(_translate("MainWindow", "点击坐标偏移："))
        self.label_19.setText(_translate("MainWindow", "个像素"))
        self.label_17.setText(_translate("MainWindow", "每次匹配间隔："))
        self.label_15.setText(_translate("MainWindow", "秒"))
        self.label_14.setText(_translate("MainWindow", "脚本持续运行："))
        self.label_16.setText(_translate("MainWindow", "分钟"))
        self.label_3.setText(_translate("MainWindow", "目标名称："))
        self.select_target_path_mode_combobox.setCurrentText(_translate("MainWindow", "御魂"))
        self.select_target_path_mode_combobox.setPlaceholderText(_translate("MainWindow", "请选择功能"))
        self.select_target_path_mode_combobox.setItemText(0, _translate("MainWindow", "御魂"))
        self.select_target_path_mode_combobox.setItemText(1, _translate("MainWindow", "探索"))
        self.select_target_path_mode_combobox.setItemText(2, _translate("MainWindow", "突破"))
        self.select_target_path_mode_combobox.setItemText(3, _translate("MainWindow", "活动"))
        self.select_target_path_mode_combobox.setItemText(4, _translate("MainWindow", "觉醒"))
        self.select_target_path_mode_combobox.setItemText(5, _translate("MainWindow", "自定义"))
        self.label_2.setText(_translate("MainWindow", "窗体名称："))
        self.show_handle_title.setText(_translate("MainWindow", "阴阳师-网易游戏"))
        self.show_handle_title.setPlaceholderText(_translate("MainWindow", "请输入窗体标题或选择窗体"))
        self.btn_select_handle.setText(_translate("MainWindow", "选择窗体"))
        self.label.setText(_translate("MainWindow", "匹配目标："))
        self.rd_btn_windows_mod.setText(_translate("MainWindow", "Windows程序窗体"))
        self.rd_btn_android_adb.setText(_translate("MainWindow", "Android-手机"))
        self.show_target_path.setPlaceholderText(_translate("MainWindow", "匹配目标文件夹路径…"))
        self.select_targetpic_path_btn.setText(_translate("MainWindow", "选择路径"))
        self.label_13.setText(_translate("MainWindow", "运行日志："))
        self.btn_exit.setText(_translate("MainWindow", "退出"))
        self.btn_resume.setText(_translate("MainWindow", "恢复"))
        self.btn_stop.setText(_translate("MainWindow", "停止"))
        self.btn_pause.setText(_translate("MainWindow", "暂停"))
        self.btn_start.setText(_translate("MainWindow", "开始"))
        self.label_12.setText(_translate("MainWindow", "匹配进度："))
