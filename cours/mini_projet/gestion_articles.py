# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import xml.etree.ElementTree as xml
from os.path import exists
import lxml
from lxml import etree
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.gridLayout = QtWidgets.QGridLayout(self.mainframe)
        self.gridLayout.setObjectName("gridLayout")
        self.add_and_filter = QtWidgets.QFrame(self.mainframe)
        self.add_and_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_and_filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_and_filter.setObjectName("add_and_filter")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.add_and_filter)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add = QtWidgets.QWidget(self.add_and_filter)
        self.add.setObjectName("add")
        self.add_article = QtWidgets.QLabel(self.add)
        self.add_article.setGeometry(QtCore.QRect(240, 0, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_article.setFont(font)
        self.add_article.setLineWidth(3)
        self.add_article.setTextFormat(QtCore.Qt.AutoText)
        self.add_article.setObjectName("add_article")
        self.add_title = QtWidgets.QLabel(self.add)
        self.add_title.setGeometry(QtCore.QRect(10, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_title.setFont(font)
        self.add_title.setObjectName("add_title")
        self._add_title = QtWidgets.QLineEdit(self.add)
        self._add_title.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self._add_title.setObjectName("_add_title")
        self.add_authors = QtWidgets.QLabel(self.add)
        self.add_authors.setGeometry(QtCore.QRect(150, 30, 47, 13))
        self.add_authors.setObjectName("add_authors")
        self._add_auteurs = QtWidgets.QLineEdit(self.add)
        self._add_auteurs.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self._add_auteurs.setObjectName("_add_auteurs")
        self.add_nb_page = QtWidgets.QLabel(self.add)
        self.add_nb_page.setGeometry(QtCore.QRect(430, 30, 81, 16))
        self.add_nb_page.setObjectName("add_nb_page")
        self._add_nb_page = QtWidgets.QSpinBox(self.add)
        self._add_nb_page.setGeometry(QtCore.QRect(430, 50, 42, 22))
        self._add_nb_page.setMaximum(9999)
        self._add_nb_page.setObjectName("_add_nb_page")
        self._add_button = QtWidgets.QPushButton(self.add)
        self._add_button.setGeometry(QtCore.QRect(540, 40, 75, 31))
        self._add_button.setObjectName("_add_button")
        self._add_button.clicked.connect(self.save_data_to_xml)
        self._add_date = QtWidgets.QDateEdit(self.add)
        self._add_date.setGeometry(QtCore.QRect(290, 50, 110, 22))
        self._add_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self._add_date.setCalendarPopup(True)
        self._add_date.setObjectName("_add_date")
        self.add_date = QtWidgets.QLabel(self.add)
        self.add_date.setGeometry(QtCore.QRect(290, 30, 47, 13))
        self.add_date.setObjectName("add_date")
        self.verticalLayout_3.addWidget(self.add)
        self.filter = QtWidgets.QWidget(self.add_and_filter)
        self.filter.setObjectName("filter")
        self.filter_recherche = QtWidgets.QLabel(self.filter)
        self.filter_recherche.setGeometry(QtCore.QRect(240, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.filter_recherche.setFont(font)
        self.filter_recherche.setLineWidth(3)
        self.filter_recherche.setTextFormat(QtCore.Qt.AutoText)
        self.filter_recherche.setObjectName("filter_recherche")
        self.filter_auteurs = QtWidgets.QLabel(self.filter)
        self.filter_auteurs.setGeometry(QtCore.QRect(240, 30, 47, 13))
        self.filter_auteurs.setObjectName("filter_auteurs")
        self.filter_title = QtWidgets.QLabel(self.filter)
        self.filter_title.setGeometry(QtCore.QRect(100, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.filter_title.setFont(font)
        self.filter_title.setObjectName("filter_title")
        self._filter_authors = QtWidgets.QLineEdit(self.filter)
        self._filter_authors.setGeometry(QtCore.QRect(240, 50, 113, 20))
        self._filter_authors.setObjectName("_filter_authors")
        self._filter_authors.textChanged[str].connect(self.filter_articles)
        self._filter_title = QtWidgets.QLineEdit(self.filter)
        self._filter_title.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self._filter_title.setObjectName("_filter_title")
        self._filter_title.textChanged[str].connect(self.filter_articles)
        self._filter_date = QtWidgets.QDateEdit(self.filter)
        self._filter_date.setGeometry(QtCore.QRect(380, 50, 110, 22))
        self._filter_date.setReadOnly(True)
        self._filter_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self._filter_date.setCalendarPopup(True)
        self._filter_date.setObjectName("_filter_date")
        self._filter_date.dateChanged.connect(self.filter_articles)
        self._filter_date_check = QtWidgets.QCheckBox(self.filter)
        self._filter_date_check.setGeometry(QtCore.QRect(380, 30, 70, 21))
        self._filter_date_check.setObjectName("_filter_date_check")
        self._filter_date_check.stateChanged.connect(self.toggle_filter_date)
        self.verticalLayout_3.addWidget(self.filter)
        self.gridLayout.addWidget(self.add_and_filter, 0, 0, 1, 1)
        self.output = QtWidgets.QFrame(self.mainframe)
        self.output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output.setObjectName("output")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.output)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_and_count = QtWidgets.QWidget(self.output)
        self.list_and_count.setObjectName("list_and_count")
        self.articles = QtWidgets.QListWidget(self.list_and_count)
        self.articles.setGeometry(QtCore.QRect(0, 0, 631, 181))
        self.articles.setObjectName("articles")
        self.total = QtWidgets.QLCDNumber(self.list_and_count)
        self.total.setGeometry(QtCore.QRect(560, 0, 51, 23))
        self.total.setSmallDecimalPoint(False)
        self.total.setDigitCount(3)
        self.total.setProperty("value", 0.0)
        self.total.setObjectName("total")
        self.total.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.horizontalLayout.addWidget(self.list_and_count)
        self.gridLayout.addWidget(self.output, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.mainframe)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_data("","","")
    def toggle_filter_date(self):
        self._filter_date.setReadOnly(not self._filter_date_check.isChecked())
        
    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Gestion Articles"))
        self.add_article.setText(self._translate("MainWindow", "Ajouter un article"))
        self.add_title.setText(self._translate("MainWindow", "Titre"))
        self.add_authors.setText(self._translate("MainWindow", "Auteurs"))
        self.add_nb_page.setText(self._translate("MainWindow", "Nombre pages"))
        self._add_button.setText(self._translate("MainWindow", "Ajouter"))
        self.add_date.setText(self._translate("MainWindow", "Date"))
        self.filter_recherche.setText(self._translate("MainWindow", "Recherche"))
        self.filter_auteurs.setText(self._translate("MainWindow", "Auteurs"))
        self.filter_title.setText(self._translate("MainWindow", "Titre"))
        self._filter_date_check.setText(self._translate("MainWindow", "Date"))
        
    def save_data_to_xml(self):
        if(exists("articles.xml") == True):
            articles=xml.parse("articles.xml").getroot()
        if(exists("articles.xml") == False):
            articles = xml.Element("articles")
        article = xml.SubElement(articles,"article")
        # authors = xml.SubElement(article,"authors")
        authors_list = self._add_auteurs.text()
        author = xml.SubElement(article,"author")
        author.text=authors_list
        # for a in authors_list:
        #     author = xml.SubElement(article,"author")
        #     author.text=a
        date = xml.SubElement(article,"date")
        date.text = self._add_date.text()
        titre = xml.SubElement(article,"titre")
        titre.text = self._add_title.text()
        nbpage = xml.SubElement(article,"nbpage")
        nbpage.text = self._add_nb_page.text()
            
        tree = xml.ElementTree(articles)
        with open("articles.xml","wb") as file:
            tree.write(file_or_filename=file)
        self.actualiser()
    def actualiser(self):
        self.load_data("","","")
    def filter_articles(self):
        if(self._filter_date_check.isChecked()):
            self.load_data(auteur=self._filter_authors.text(),date=self._filter_date.text(),title=self._filter_title.text())
        else:
            self.load_data(auteur=self._filter_authors.text(),date="",title=self._filter_title.text())
            
    def load_data(self,auteur,date,title):
        self.articles.clear()
        if(exists("articles.xml") == True):
            # if self.auteur.text != "":
            articles = xml.parse("articles.xml").getroot()
            articles2= etree.parse("articles.xml")
            data = articles2.xpath(f"./article[contains(author/text(),'{auteur}')and starts-with(titre,'{title}')and starts-with(date,'{date}')]")
            i=-1
            for article in data:
                print(article.find("author").text)
                item = QtWidgets.QListWidgetItem()
                self.articles.addItem(item)
                ch=""
                i+=1
                item = self.articles.item(i)
                ch="Titre : "
                
                ch+=article.find("titre").text+" "
                ch+="\nAuteurs : "
                authors=article.findall("author")
                for author in authors:
                    ch+=author.text+", "
                
                ch+="\nDate : "
                ch+=article.find("date").text
                ch+="\nPages : "
                
                ch+=article.find("nbpage").text
                # print(ch)
                item.setText(self._translate("Articles",ch))
            self.total.display(str(i+1))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
