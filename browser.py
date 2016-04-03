
import sqlite3
import datetime
import time
import sys
from PyQt4 import QtCore, QtGui, QtWebKit
import  ekle,getir,sil,kayit



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Browser(QtGui.QMainWindow):




    def __init__(self):



        QtGui.QMainWindow.__init__(self)
        self.resize(1400,800)
        self.centralwidget = QtGui.QWidget(self)
        self.setWindowTitle("Systemprogramming")

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.frame = QtGui.QFrame(self.centralwidget)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(5)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout()

        self.tb_url = QtGui.QLineEdit(self.frame)
        self.bt_back = QtGui.QPushButton(self.frame)
        self.bt_ahead = QtGui.QPushButton(self.frame)
        self.refresh=QtGui.QPushButton(self.frame)
        self.gecmis=QtGui.QPushButton(self.frame)

        self.setObjectName(_fromUtf8("Form"))
        self.resize(1010, 750)
        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(200, 30, 2011, 681))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.listWidget.hide()


        self.bt_back.setIcon(QtGui.QIcon().fromTheme("go-previous"))
        self.bt_ahead.setIcon(QtGui.QIcon().fromTheme("go-next"))
        self.refresh.setIcon(QtGui.QIcon().fromTheme("view-refresh"))
        self.gecmis.setText(_translate("MainWindow", "gecmiş", None))


        self.horizontalLayout.addWidget(self.bt_back)
        self.horizontalLayout.addWidget(self.bt_ahead)
        self.horizontalLayout.addWidget(self.refresh)
        self.horizontalLayout.addWidget(self.tb_url)
        self.horizontalLayout.addWidget(self.gecmis)
        self.horizontalLayout.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QtWebKit.QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(0, 30, 810, 551))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.hide()







        self.connect(self.tb_url, QtCore.SIGNAL("returnPressed()"), self.browse)
        self.connect(self.bt_back, QtCore.SIGNAL("clicked()"), self.html.back)
        self.connect(self.bt_ahead, QtCore.SIGNAL("clicked()"), self.html.forward)
        self.connect(self.gecmis, QtCore.SIGNAL("clicked()"), self.full)


        an = datetime.datetime.now()
        tarih = datetime.datetime.strftime(an,'%S')

        veriYil = []
        veriYil1 =[]
        gecmisListe = []
        gecmisListe = getir.getir.liste(self)


        for v in range(gecmisListe.__len__()):
            veriYil.append(datetime.datetime.strptime(gecmisListe[v][1],"%Y-%m-%d %H:%M:%S.%f"))
            #print(gecmisListe[v][1])
            #print(veriYil[v])
            for c in range(veriYil.__len__()):
                if str(datetime.datetime.strftime(veriYil[v],"%d-%B-%Y")) not in str(veriYil1):
                    print("yok")
                    veriYil1.append(datetime.datetime.strftime(veriYil[v],"%d-%B-%Y"))
                    a=str(datetime.datetime.strftime(veriYil[v],"%d-%B-%Y"))
                    b=str(datetime.datetime.strftime(veriYil[v],"%H:%M:%S"))
                    self.listWidget.addItem("                                          "+str(a))
                    self.listWidget.addItem(str(b)+"   "+gecmisListe[v][2])




                else:
                    print("var")
                    b=str(datetime.datetime.strftime(veriYil[v],"%H:%M:%S"))
                    self.listWidget.addItem(str(b)+"   "+gecmisListe[v][2])


                    break




        self.default_url = "http://google.com"
        self.tb_url.setText(self.default_url)
        self.browse()

        self.enter = QtGui.QPushButton(self)
        self.enter.resize(0,0)
        self.enter.clicked.connect(self.Enter)
        self.enter.setShortcut("Return")

        #self.listWidget.itemDoubleClicked.connect(self.gecmis_click)
        self.connect(self.listWidget, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"),self.sil_click)


    def sil_click(self):


        print("yapılacak")

        #sil.sil.liste()





    def Enter(self):

        url = self.tb_url.text()

        http = "http://"
        www = "www."

        if www in url and http not in url:
            url = http + url

        elif "." not in url:
            url = "http://www.google.com/search?q="+url

        elif http in url and www not in url:
            url = url[:7] + www + url[7:]

        elif http and www not in url:
            url = http + www + url


        self.tb_url.setText(url)

        self.browse()

    def browse(self):

        an=time.localtime()
        url = self.tb_url.text() if self.tb_url.text() else self.default_url

        an = datetime.datetime.now()
        #an=time.localtime()
        params=(an,url)
        ekle.ekle.isles(params)
        self.html.load(QtCore.QUrl(url))
        self.html.show()




    def url_changed(self, url):

      self.tb_url.setText(url.toString())

    def full(self):
        #main.showFullScreen()
        self.listWidget.show()


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    main = Browser()
    main.show()
    sys.exit(app.exec_())


