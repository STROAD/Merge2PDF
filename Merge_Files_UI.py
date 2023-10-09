import os
from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QFont,
    QIcon,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QFrame,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QToolButton,
    QWidget,
)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(450, 670)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 670))
        MainWindow.setMaximumSize(QSize(450, 670))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(":/icon/Merge_Files_Icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_help.setEnabled(True)
        self.action_files = QAction(MainWindow)
        self.action_files.setObjectName("action_files")
        self.action_floder = QAction(MainWindow)
        self.action_floder.setObjectName("action_floder")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_filelist = QLabel(self.centralwidget)
        self.label_filelist.setObjectName("label_filelist")
        self.label_filelist.setGeometry(QRect(20, 10, 111, 16))
        sizePolicy.setHeightForWidth(
            self.label_filelist.sizePolicy().hasHeightForWidth()
        )
        self.label_filelist.setSizePolicy(sizePolicy)
        self.label_filelist.setFont(font)
        self.files_list = QListWidget(self.centralwidget)
        self.files_list.setObjectName("files_list")
        self.files_list.setGeometry(QRect(10, 30, 431, 320))
        sizePolicy.setHeightForWidth(self.files_list.sizePolicy().hasHeightForWidth())
        self.files_list.setSizePolicy(sizePolicy)
        self.files_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.line1 = QFrame(self.centralwidget)
        self.line1.setObjectName("line1")
        self.line1.setGeometry(QRect(10, 390, 430, 16))
        sizePolicy.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy)
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.Button_addfile = QPushButton(self.centralwidget)
        self.Button_addfile.setObjectName("Button_addfile")
        self.Button_addfile.setGeometry(QRect(245, 362, 80, 25))
        sizePolicy.setHeightForWidth(
            self.Button_addfile.sizePolicy().hasHeightForWidth()
        )
        self.Button_addfile.setSizePolicy(sizePolicy)
        self.Button_remove = QPushButton(self.centralwidget)
        self.Button_remove.setObjectName("Button_remove")
        self.Button_remove.setGeometry(QRect(340, 362, 80, 25))
        sizePolicy.setHeightForWidth(
            self.Button_remove.sizePolicy().hasHeightForWidth()
        )
        self.Button_remove.setSizePolicy(sizePolicy)
        self.label_setting = QLabel(self.centralwidget)
        self.label_setting.setObjectName("label_setting")
        self.label_setting.setGeometry(QRect(20, 420, 101, 16))
        sizePolicy.setHeightForWidth(
            self.label_setting.sizePolicy().hasHeightForWidth()
        )
        self.label_setting.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label_setting.setFont(font1)
        self.label_path = QLabel(self.centralwidget)
        self.label_path.setObjectName("label_path")
        self.label_path.setGeometry(QRect(25, 450, 81, 16))
        sizePolicy.setHeightForWidth(self.label_path.sizePolicy().hasHeightForWidth())
        self.label_path.setSizePolicy(sizePolicy)
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName("label_name")
        self.label_name.setGeometry(QRect(25, 480, 81, 16))
        self.label_format = QLabel(self.centralwidget)
        self.label_format.setObjectName("label_format")
        self.label_format.setGeometry(QRect(25, 510, 81, 16))
        self.label_resolution = QLabel(self.centralwidget)
        self.label_resolution.setObjectName("label_resolution")
        self.label_resolution.setGeometry(QRect(25, 540, 81, 16))
        sizePolicy.setHeightForWidth(
            self.label_resolution.sizePolicy().hasHeightForWidth()
        )
        self.label_resolution.setSizePolicy(sizePolicy)
        self.line2 = QFrame(self.centralwidget)
        self.line2.setObjectName("line2")
        self.line2.setGeometry(QRect(5, 570, 430, 16))
        sizePolicy.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy)
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.Button_start = QPushButton(self.centralwidget)
        self.Button_start.setObjectName("Button_start")
        self.Button_start.setGeometry(QRect(240, 590, 85, 30))
        sizePolicy.setHeightForWidth(self.Button_start.sizePolicy().hasHeightForWidth())
        self.Button_start.setSizePolicy(sizePolicy)
        self.Button_exit = QPushButton(self.centralwidget)
        self.Button_exit.setObjectName("Button_exit")
        self.Button_exit.setGeometry(QRect(340, 590, 85, 30))
        sizePolicy.setHeightForWidth(self.Button_exit.sizePolicy().hasHeightForWidth())
        self.Button_exit.setSizePolicy(sizePolicy)
        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(110, 480, 311, 20))
        sizePolicy.setHeightForWidth(
            self.lineEdit_name.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_name.setSizePolicy(sizePolicy)
        self.lineEdit_path = QLineEdit(self.centralwidget)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(110, 450, 280, 20))
        sizePolicy.setHeightForWidth(
            self.lineEdit_path.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_path.setSizePolicy(sizePolicy)
        self.toolButton_path = QToolButton(self.centralwidget)
        self.toolButton_path.setObjectName("toolButton_path")
        self.toolButton_path.setGeometry(QRect(395, 450, 27, 20))
        self.comboBox_resolution = QComboBox(self.centralwidget)
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.setObjectName("comboBox_resolution")
        self.comboBox_resolution.setGeometry(QRect(109, 540, 101, 22))
        sizePolicy.setHeightForWidth(
            self.comboBox_resolution.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_resolution.setSizePolicy(sizePolicy)
        self.comboBox_resolution.setAutoFillBackground(False)
        self.comboBox_resolution.setEditable(False)
        self.Button_addfolder = QPushButton(self.centralwidget)
        self.Button_addfolder.setObjectName("Button_addfolder")
        self.Button_addfolder.setGeometry(QRect(150, 362, 80, 25))
        sizePolicy.setHeightForWidth(
            self.Button_addfolder.sizePolicy().hasHeightForWidth()
        )
        self.Button_addfolder.setSizePolicy(sizePolicy)
        self.comboBox_format = QComboBox(self.centralwidget)
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")
        self.comboBox_format.setObjectName("comboBox_format")
        self.comboBox_format.setGeometry(QRect(109, 510, 101, 22))
        sizePolicy.setHeightForWidth(
            self.comboBox_format.sizePolicy().hasHeightForWidth()
        )
        self.comboBox_format.setSizePolicy(sizePolicy)
        self.comboBox_format.setAutoFillBackground(False)
        self.comboBox_format.setEditable(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 21))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.files_list, self.Button_addfolder)
        QWidget.setTabOrder(self.Button_addfolder, self.Button_addfile)
        QWidget.setTabOrder(self.Button_addfile, self.Button_remove)
        QWidget.setTabOrder(self.Button_remove, self.lineEdit_path)
        QWidget.setTabOrder(self.lineEdit_path, self.toolButton_path)
        QWidget.setTabOrder(self.toolButton_path, self.lineEdit_name)
        QWidget.setTabOrder(self.lineEdit_name, self.comboBox_format)
        QWidget.setTabOrder(self.comboBox_format, self.comboBox_resolution)
        QWidget.setTabOrder(self.comboBox_resolution, self.Button_start)
        QWidget.setTabOrder(self.Button_start, self.Button_exit)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_files)
        self.menu_file.addAction(self.action_floder)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_help)

        self.retranslateUi(MainWindow)
        # 임시 주석처리. 기능 추가 후 주석 해제하기.
        self.toolButton_path.clicked.connect(MainWindow.select_folder)
        self.Button_remove.clicked.connect(MainWindow.remove_file)
        self.Button_exit.clicked.connect(MainWindow.close)
        # self.action_help.triggered.connect(MainWindow.open_help)
        self.Button_addfile.clicked.connect(MainWindow.add_files)
        self.Button_addfolder.clicked.connect(MainWindow.add_folder)
        # self.Button_start.clicked.connect(MainWindow.start_merge)
        self.action_files.triggered.connect(MainWindow.add_files)
        self.action_floder.triggered.connect(MainWindow.add_folder)
        self.action_exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Merge Files", None)
        )
        self.action_help.setText(
            QCoreApplication.translate("MainWindow", "\ub3c4\uc6c0\ub9d0", None)
        )
        # if QT_CONFIG(shortcut)
        self.action_help.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+H", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.action_files.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \ucd94\uac00", None)
        )
        # if QT_CONFIG(shortcut)
        self.action_files.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.action_floder.setText(
            QCoreApplication.translate("MainWindow", "\ud3f4\ub354 \ucd94\uac00", None)
        )
        # if QT_CONFIG(shortcut)
        self.action_floder.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Shift+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.action_exit.setText(
            QCoreApplication.translate("MainWindow", "\uc885\ub8cc", None)
        )
        # if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+W", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_filelist.setText(
            QCoreApplication.translate(
                "MainWindow", "\ubcd1\ud569\ud560 \ud30c\uc77c \ubaa9\ub85d", None
            )
        )
        self.Button_addfile.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \ucd94\uac00", None)
        )
        self.Button_remove.setText(
            QCoreApplication.translate("MainWindow", "\uc81c\uac70", None)
        )
        # if QT_CONFIG(shortcut)
        self.Button_remove.setShortcut(
            QCoreApplication.translate("MainWindow", "Del", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label_setting.setText(
            QCoreApplication.translate(
                "MainWindow", "\ud30c\uc77c \ubcd1\ud569 \uc124\uc815", None
            )
        )
        self.label_path.setText(
            QCoreApplication.translate(
                "MainWindow", "\ub2e4\uc6b4\ub85c\ub4dc \uc704\uce58", None
            )
        )
        self.label_name.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \uc774\ub984", None)
        )
        self.label_format.setText(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c \ud615\uc2dd", None)
        )
        self.label_resolution.setText(
            QCoreApplication.translate("MainWindow", "\ud574\uc0c1\ub3c4", None)
        )
        self.Button_start.setText(
            QCoreApplication.translate("MainWindow", "\ubcd1\ud569 \uc2dc\uc791", None)
        )
        self.Button_exit.setText(
            QCoreApplication.translate("MainWindow", "\ub2eb\uae30", None)
        )
        self.lineEdit_path.setInputMask("")
        self.lineEdit_path.setText(
            QCoreApplication.translate(
                "MainWindow", f"{os.getenv('USERPROFILE')}\\Downloads", None
            )
        )
        self.toolButton_path.setText(
            QCoreApplication.translate("MainWindow", "...", None)
        )
        self.comboBox_resolution.setItemText(
            0,
            QCoreApplication.translate("MainWindow", "\uc6d0\ubcf8 \ud06c\uae30", None),
        )
        self.comboBox_resolution.setItemText(
            1, QCoreApplication.translate("MainWindow", "1080", None)
        )
        self.comboBox_resolution.setItemText(
            2, QCoreApplication.translate("MainWindow", "720", None)
        )
        self.comboBox_resolution.setItemText(
            3, QCoreApplication.translate("MainWindow", "480", None)
        )

        self.comboBox_resolution.setCurrentText(
            QCoreApplication.translate("MainWindow", "\uc6d0\ubcf8 \ud06c\uae30", None)
        )
        self.Button_addfolder.setText(
            QCoreApplication.translate("MainWindow", "\ud3f4\ub354 \ucd94\uac00", None)
        )
        self.comboBox_format.setItemText(
            0, QCoreApplication.translate("MainWindow", "pdf", None)
        )
        self.comboBox_format.setItemText(
            1, QCoreApplication.translate("MainWindow", "png", None)
        )
        self.comboBox_format.setItemText(
            2, QCoreApplication.translate("MainWindow", "jpg", None)
        )

        self.comboBox_format.setCurrentText(
            QCoreApplication.translate("MainWindow", "pdf", None)
        )
        self.menu_file.setTitle(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c", None)
        )
        self.menu_help.setTitle(
            QCoreApplication.translate("MainWindow", "\ub3c4\uc6c0\ub9d0", None)
        )
