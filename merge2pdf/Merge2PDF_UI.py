from os import getenv
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 630)
        MainWindow.setMinimumSize(QSize(330, 470))
        icon = QIcon()
        icon.addFile(":/icon/Merge2PDF_Icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_files = QAction(MainWindow)
        self.action_files.setObjectName("action_files")
        self.action_folder = QAction(MainWindow)
        self.action_folder.setObjectName("action_folder")
        self.action_close = QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName("action_info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.group_saveoption = QGroupBox(self.centralwidget)
        self.group_saveoption.setObjectName("group_saveoption")
        self.group_saveoption.setFlat(False)
        self.gridLayout_6 = QGridLayout(self.group_saveoption)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 14)
        self.Layout_4 = QVBoxLayout()
        self.Layout_4.setObjectName("Layout_4")
        self.Layout_5 = QHBoxLayout()
        self.Layout_5.setObjectName("Layout_5")
        self.Layout_5.setContentsMargins(-1, 5, -1, -1)
        self.label_dir = QLabel(self.group_saveoption)
        self.label_dir.setObjectName("label_dir")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dir.sizePolicy().hasHeightForWidth())
        self.label_dir.setSizePolicy(sizePolicy)
        self.label_dir.setMinimumSize(QSize(81, 0))

        self.Layout_5.addWidget(self.label_dir)

        self.lineEdit_dir = QLineEdit(self.group_saveoption)
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.lineEdit_dir.setMinimumSize(QSize(0, 20))

        self.Layout_5.addWidget(self.lineEdit_dir)

        self.toolButton_dir = QToolButton(self.group_saveoption)
        self.toolButton_dir.setObjectName("toolButton_dir")
        self.toolButton_dir.setMinimumSize(QSize(25, 20))

        self.Layout_5.addWidget(self.toolButton_dir)

        self.Layout_4.addLayout(self.Layout_5)

        self.Layout_6 = QHBoxLayout()
        self.Layout_6.setObjectName("Layout_6")
        self.Layout_6.setContentsMargins(-1, 5, -1, -1)
        self.label_name = QLabel(self.group_saveoption)
        self.label_name.setObjectName("label_name")
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QSize(81, 0))

        self.Layout_6.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.group_saveoption)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(0, 20))

        self.Layout_6.addWidget(self.lineEdit_name)

        self.Layout_4.addLayout(self.Layout_6)

        self.Layout_7 = QHBoxLayout()
        self.Layout_7.setObjectName("Layout_7")
        self.Layout_7.setContentsMargins(-1, 5, -1, -1)
        self.label_compression = QLabel(self.group_saveoption)
        self.label_compression.setObjectName("label_compression")
        sizePolicy.setHeightForWidth(
            self.label_compression.sizePolicy().hasHeightForWidth()
        )
        self.label_compression.setSizePolicy(sizePolicy)
        self.label_compression.setMinimumSize(QSize(81, 0))

        self.Layout_7.addWidget(self.label_compression)

        self.radioButton_no = QRadioButton(self.group_saveoption)
        self.radioButton_no.setObjectName("radioButton_no")
        self.radioButton_no.setChecked(True)

        self.Layout_7.addWidget(self.radioButton_no)

        self.radioButton_yes = QRadioButton(self.group_saveoption)
        self.radioButton_yes.setObjectName("radioButton_yes")

        self.Layout_7.addWidget(self.radioButton_yes)

        self.Spacer7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Layout_7.addItem(self.Spacer7)

        self.Layout_4.addLayout(self.Layout_7)

        self.gridLayout_6.addLayout(self.Layout_4, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.group_saveoption, 5, 0, 1, 1)

        self.Layout_8 = QHBoxLayout()
        self.Layout_8.setSpacing(15)
        self.Layout_8.setObjectName("Layout_8")
        self.Layout_8.setContentsMargins(0, 5, 10, -1)
        self.Spacer8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Layout_8.addItem(self.Spacer8)

        self.Button_start = QPushButton(self.centralwidget)
        self.Button_start.setObjectName("Button_start")
        self.Button_start.setMinimumSize(QSize(85, 30))

        self.Layout_8.addWidget(self.Button_start)

        self.Button_close = QPushButton(self.centralwidget)
        self.Button_close.setObjectName("Button_close")
        self.Button_close.setMinimumSize(QSize(85, 30))

        self.Layout_8.addWidget(self.Button_close)

        self.gridLayout_2.addLayout(self.Layout_8, 7, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 6, 0, 1, 1)

        self.Layout_1 = QHBoxLayout()
        self.Layout_1.setObjectName("Layout_1")
        self.Layout_1.setContentsMargins(10, -1, -1, -1)
        self.label_filelist = QLabel(self.centralwidget)
        self.label_filelist.setObjectName("label_filelist")

        self.Layout_1.addWidget(self.label_filelist)

        self.gridLayout_2.addLayout(self.Layout_1, 0, 0, 1, 1)

        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName("line_1")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_1, 4, 0, 1, 1)

        self.Layout_2 = QGridLayout()
        self.Layout_2.setObjectName("Layout_2")
        self.files_list = QListWidget(self.centralwidget)
        self.files_list.setObjectName("files_list")

        self.Layout_2.addWidget(self.files_list, 1, 0, 1, 1)

        self.gridLayout_2.addLayout(self.Layout_2, 2, 0, 1, 1)

        self.Layout_3 = QHBoxLayout()
        self.Layout_3.setSpacing(10)
        self.Layout_3.setObjectName("Layout_3")
        self.Layout_3.setContentsMargins(0, 5, 10, 5)
        self.Spacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.Layout_3.addItem(self.Spacer3)

        self.Button_addfolder = QPushButton(self.centralwidget)
        self.Button_addfolder.setObjectName("Button_addfolder")
        self.Button_addfolder.setMinimumSize(QSize(80, 25))

        self.Layout_3.addWidget(self.Button_addfolder)

        self.Button_addfiles = QPushButton(self.centralwidget)
        self.Button_addfiles.setObjectName("Button_addfiles")
        self.Button_addfiles.setMinimumSize(QSize(80, 25))

        self.Layout_3.addWidget(self.Button_addfiles)

        self.Button_remove = QPushButton(self.centralwidget)
        self.Button_remove.setObjectName("Button_remove")
        self.Button_remove.setMinimumSize(QSize(80, 25))

        self.Layout_3.addWidget(self.Button_remove)

        self.gridLayout_2.addLayout(self.Layout_3, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 21))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.Button_addfolder, self.Button_addfiles)
        QWidget.setTabOrder(self.Button_addfiles, self.files_list)
        QWidget.setTabOrder(self.files_list, self.Button_remove)
        QWidget.setTabOrder(self.Button_remove, self.toolButton_dir)
        QWidget.setTabOrder(self.toolButton_dir, self.lineEdit_dir)
        QWidget.setTabOrder(self.lineEdit_dir, self.lineEdit_name)
        QWidget.setTabOrder(self.lineEdit_name, self.radioButton_no)
        QWidget.setTabOrder(self.radioButton_no, self.radioButton_yes)
        QWidget.setTabOrder(self.radioButton_yes, self.Button_start)
        QWidget.setTabOrder(self.Button_start, self.Button_close)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_files)
        self.menu_file.addAction(self.action_folder)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close)
        self.menu_help.addAction(self.action_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_info)

        self.retranslateUi(MainWindow)
        self.Button_addfolder.clicked.connect(MainWindow.add_folder)
        self.Button_addfiles.clicked.connect(MainWindow.add_files)
        self.Button_remove.clicked.connect(MainWindow.remove_files)
        self.toolButton_dir.clicked.connect(MainWindow.select_folder)
        self.Button_start.clicked.connect(MainWindow.start_merge)
        self.Button_close.clicked.connect(MainWindow.close)
        self.action_files.triggered.connect(MainWindow.add_files)
        self.action_folder.triggered.connect(MainWindow.add_folder)
        self.action_close.triggered.connect(MainWindow.close)
        self.action_help.triggered.connect(MainWindow.open_help)
        self.action_info.triggered.connect(MainWindow.open_info)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Merge to PDF", None)
        )
        self.action_files.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \ucd94\uac00", None)
        )
        self.action_files.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        self.action_folder.setText(
            QCoreApplication.translate("MainWindow", "\ud3f4\ub354 \ucd94\uac00", None)
        )
        self.action_folder.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Shift+O", None)
        )
        self.action_close.setText(
            QCoreApplication.translate("MainWindow", "\uc885\ub8cc", None)
        )
        self.action_close.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+W", None)
        )
        self.action_help.setText(
            QCoreApplication.translate(
                "MainWindow", "\ub3c4\uc6c0\ub9d0 \ud398\uc774\uc9c0 \uc5f4\uae30", None
            )
        )
        self.action_help.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+H", None)
        )
        self.action_info.setText(
            QCoreApplication.translate("MainWindow", "\uc815\ubcf4", None)
        )
        self.group_saveoption.setTitle(
            QCoreApplication.translate("MainWindow", "\uc800\uc7a5 \uc635\uc158", None)
        )
        self.label_dir.setText(
            QCoreApplication.translate(
                "MainWindow", "\ub2e4\uc6b4\ub85c\ub4dc \uc704\uce58", None
            )
        )
        self.lineEdit_dir.setInputMask("")
        self.lineEdit_dir.setText(
            QCoreApplication.translate(
                "MainWindow", f"{getenv('USERPROFILE')}\\Downloads", None
            )
        )
        self.toolButton_dir.setText(
            QCoreApplication.translate("MainWindow", "...", None)
        )
        self.label_name.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \uc774\ub984", None)
        )
        self.label_compression.setText(
            QCoreApplication.translate("MainWindow", "PDF \uc555\ucd95", None)
        )
        self.radioButton_no.setText(
            QCoreApplication.translate("MainWindow", "\uc555\ucd95 \uc548 \ud568", None)
        )
        self.radioButton_yes.setText(
            QCoreApplication.translate("MainWindow", "\uc555\ucd95\ud558\uae30", None)
        )
        self.Button_start.setText(
            QCoreApplication.translate("MainWindow", "\ubcd1\ud569 \uc2dc\uc791", None)
        )
        self.Button_close.setText(
            QCoreApplication.translate("MainWindow", "\ub2eb\uae30", None)
        )
        self.label_filelist.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \ubaa9\ub85d", None)
        )
        self.Button_addfolder.setText(
            QCoreApplication.translate("MainWindow", "\ud3f4\ub354 \ucd94\uac00", None)
        )
        self.Button_addfiles.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \ucd94\uac00", None)
        )
        self.Button_remove.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \uc81c\uac70", None)
        )
        self.menu_file.setTitle(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c", None)
        )
        self.menu_help.setTitle(
            QCoreApplication.translate("MainWindow", "\ub3c4\uc6c0\ub9d0", None)
        )
