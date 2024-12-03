import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit # type: ignore
from PyQt5.QtGui import QIcon, QFont # type: ignore
from PyQt5.QtCore import QSize, QUrl #type: ignore
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView #type: ignore
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Anum Talat")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(200, 200, 900, 600)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("back.png"))
        self.backButton.setIconSize(QSize(20, 20))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)
        
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("forward.png"))
        self.forwardButton.setIconSize(QSize(20, 20))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)


        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("reload.png"))
        self.reloadButton.setIconSize(QSize(20, 20))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif", 14))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("search.png"))
        self.searchButton.setIconSize(QSize(20, 20))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)

        self.WebEngineView = QWebEngineView()
        self.setCentralWidget(self.WebEngineView)
        initialUrl = 'https://google.com'
        self.addressLineEdit.setText(initialUrl)
        self.WebEngineView.load(QUrl(initialUrl))
   
   
    def searchBtn(self):
        myUrl = self.addressLineEdit.text()
        self.WebEngineView.load(QUrl(myUrl))

    def backBtn(self):
        self.WebEngineView.back()
         
    def forwardBtn(self):
        self.WebEngineView.forward()
    
    def reloadBtn(self):
        self.WebEngineView.reload()






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())