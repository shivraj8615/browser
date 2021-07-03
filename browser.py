import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import  *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self) :
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        nav = QToolBar()            #navigation bar adding
        self.addToolBar(nav)
        back_btn = QAction('<-',self)    # adding back button
        back_btn.triggered.connect(self.browser.back)
        nav.addAction(back_btn)
        forward_btn = QAction('->',self)    # adding forward button
        forward_btn .triggered.connect(self.browser.forward)
        nav.addAction(forward_btn)
        reload_btn = QAction('@',self)  #adding reload button
        reload_btn.triggered.connect(self.browser.reload)
        nav.addAction(reload_btn)
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        nav.addAction(home_btn)
        self.url_bar =  QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
          self.browser.setUrl(QUrl('http://google.com'))
    def  navigate_to_url(self):
          url = self.url_bar.text()
          self.browser.setUrl(QUrl(url))
    def update_url(self,q) :
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Do it')
window = MainWindow()
app.exec()