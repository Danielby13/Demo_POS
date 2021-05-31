from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QFrame, QVBoxLayout, QFormLayout,QHBoxLayout, QPushButton, QDialog
import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
import store_data, qrGen, items_codes, cashRegisterScript
from collections import Counter


class App(QMainWindow):
    def __init__(self): # initilize the gui
        super().__init__()
        self.setWindowIcon(QIcon("icon.png"))
        self.title = 'Cash Register Demo'
        self.left = 500
        self.top = 150
        self.width = 420
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        logo_label = QLabel(self)
        pixmap = QPixmap('logo.png')
        sm = pixmap.scaled(350, 350, Qt.KeepAspectRatio, Qt.FastTransformation)
        logo_label.setPixmap(sm)
        logo_label.resize(350, 100)
        logo_label.move(10, 700)

        # Store info display
        self.data_store = store_data.store_data_import()
        store_info_store_name_label = QLabel(self)
        store_info_store_name_label.setText(self.data_store['store_details']['store_name'])
        store_info_store_name_label.setStyleSheet("font-weight: bold; font-size: 18px;")
        store_info_store_name_label.move(310, 15)

        store_info_store_name_label = QLabel(self)
        store_info_store_name_label.setText(self.data_store['store_details']['store_address']+",")
        store_info_store_name_label.setStyleSheet("font-weight: bold")
        store_info_store_name_label.move(310, 30)

        store_info_store_name_label = QLabel(self)
        store_info_store_name_label.setText(self.data_store['store_details']['store_city'])
        store_info_store_name_label.setStyleSheet("font-weight: bold")
        store_info_store_name_label.move(225, 30)

        store_info_store_name_label = QLabel(self)
        store_info_store_name_label.setText(self.data_store['store_details']['store_phone'])
        store_info_store_name_label.setStyleSheet("font-weight: bold")
        store_info_store_name_label.move(340, 45)

        store_info_store_name_label = QLabel(self)
        store_info_store_name_label.setText("שם המוכר: ")
        store_info_store_name_label.setStyleSheet("font-weight: bold")
        store_info_store_name_label.move(310, 60)

        store_info_store_name_label = QLabel(self)
        store_info_store_name_label.setText(self.data_store['store_details']['seller_name'])
        store_info_store_name_label.setStyleSheet("font-weight: bold")
        store_info_store_name_label.move(250, 60)

        right_frame = QFrame(self)
        right_frame.setFrameShape(QFrame.StyledPanel)
        right_frame.resize(400, 600)
        right_frame.move(10, 100)
        right_frame.setStyleSheet("background-color: white")
        self.controls = []
        self.label_con = []
        self.butt_con = []
        self.temp = []
        self.dup_temp = []
        self.total_amount = 0
        self.item_price = 0
        button1 = QPushButton('הוספת פריט', self)
        button1.clicked.connect(self.add_field)
        button2 = QPushButton('מחיקת פריט', self)
        button2.clicked.connect(self.remove_field)
        button3 = QPushButton('סיום קנייה', self)
        button3.clicked.connect(self.addItems)

        vbox = QVBoxLayout(right_frame)
        formlayout = QFormLayout()
        vbox.addLayout(formlayout)
        hbox = QHBoxLayout()
        hbox.addWidget(button2)
        hbox.addWidget(button1)
        vbox.addLayout(hbox)
        vbox.addWidget(button3)
        self.setLayout(vbox)
        self.formlayout = formlayout
        self.add_field()
        self.show()

    def add_field(self): # add fields
        self.edit = QLineEdit(self)
        self.controls.append(self.edit)
        self.formlayout.addRow('', self.edit)
        self.pushButtonOK = QPushButton(self)
        self.butt_con.append(self.pushButtonOK)
        self.pushButtonOK.setText("הכנסת פריט")
        self.pushButtonOK.clicked.connect(self.item_detail)
        self.pushButtonOK.setAutoDefault(True)
        self.formlayout.addRow(self.pushButtonOK)

    @pyqtSlot()
    def item_detail(self): # Describes the inserted item
        self.data_search = self.edit.text()
        self.items = items_codes.items_data_import()

        try: # Count the number of times the product appears
            for value in self.items:
                if self.data_search == value['item_code']:
                    if any(d['item_code'] == self.data_search for d in self.temp):
                        count = Counter(x.text() for x in self.controls)
                        value['item_amount'] = count[self.data_search]
                        self.temp.insert(0, value)
                        self.temp.pop()
                    else:
                        self.temp.append(value)

                    self.edit.close()
                    self.pushButtonOK.close()
                    self.data_label = QLabel("", self)
                    self.label_con.append(self.data_label)
                    self.data_label.setWordWrap(True)
                    self.item_price = value['item_price']
                    self.total_amount = self.total_amount + value['item_price']
                    price = str(value['item_price'])
                    item_amount = '1' 
                    self.data_label.setText(" תיאור מוצר: "+value['item_description'] +", כמות: "+ item_amount +", מחיר: "+ price)
                    self.formlayout.addRow(self.data_label)
        except Exception as e:
            print(e)

    def remove_field(self): # remove the field 
        if len(self.controls) > 1 and len(self.label_con) > 1 and len(self.butt_con) > 1:
            edit = self.controls.pop()
            self.formlayout.removeRow(edit)
            self.formlayout.removeRow(self.label_con.pop())
            self.formlayout.removeRow(self.butt_con.pop())
            self.total_amount = self.total_amount - self.item_price
            for x in self.temp:
                if x['item_code'] == self.data_search:
                    x['item_amount'] = x['item_amount'] - 1
        else:
            edit = self.controls.pop()
            self.formlayout.removeRow(edit)
            self.formlayout.removeRow(self.butt_con.pop())

    def addItems(self): # add items to the dict
        try:
            self.items_details_dict = {}
            i = 1
            for item in self.temp:
                index = "item{0}".format(i)
                self.items_details_dict[index] = {}
                self.items_details_dict[index] = item
                i = i + 1
        except Exception as e:
            print(e)

        my_dialog = QDialog(self)
        my_dialog.setWindowTitle("iCheck Cash Register Demo")
        my_dialog.setWindowModality(Qt.ApplicationModal)
        my_dialog.setStyleSheet("background-color: white;")
        my_dialog.setGeometry(self.left, self.top, 700, 700)

        if self.items_details_dict: # check if the dict is not empty, display qr code for customer to scan
            cashRegisterScript.setInvoiceDataToDb_QR(self.data_store, round(self.total_amount, 2), self.items_details_dict, self.temp)
            logo_label = QLabel(my_dialog)
            pixmap = QPixmap('output.png')
            sm = pixmap.scaled(550, 550, Qt.KeepAspectRatio, Qt.FastTransformation)
            logo_label.setPixmap(sm)
            logo_label.move(75, 25)
        else:
            msg = "יש להכניס לפחות פריט אחד לחשבון"
            self.msgBox(msg)
            
        # insert customer phone numer to send the inovice to the app
        label_phone = QLabel(my_dialog)
        label_phone.setText("הכנס מספר פלאפון")
        label_phone.move(400, 610)
        self.textbox = QLineEdit(my_dialog)
        self.textbox.move(220, 630)
        self.textbox.resize(280, 30)
        self.buttonInsertPhoneNumber = QPushButton('אישור', my_dialog)
        self.buttonInsertPhoneNumber.setStyleSheet("background-color: None")
        self.buttonInsertPhoneNumber.resize(50, 30)
        self.buttonInsertPhoneNumber.move(220, 665)
        self.buttonInsertPhoneNumber.clicked.connect(self.sendInvoiceData)
        my_dialog.exec_()

    def msgBox(self, msg, textboxValue = ''): # Sends the user an indication of whether the process was successful or failed
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg + textboxValue)
        msgBox.setWindowTitle("iCheck Demo Register")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    @pyqtSlot()
    def sendInvoiceData(self): # send to invoice to database
        try:
            textboxValue = self.textbox.text()
            if self.items_details_dict:
                cashRegisterScript.setInvoiceDataToDB(textboxValue, self.data_store, round(self.total_amount, 2), self.items_details_dict)
                msg = "החשבונית נשלחה למספר "
                self.msgBox(msg, textboxValue)
            else:
                msg = "יש להכניס לפחות פריט אחד לחשבון"
                self.msgBox(msg)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())