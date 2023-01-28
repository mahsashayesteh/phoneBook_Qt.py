import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Calculator")


# lblName = QInputDialog()
# lblName.setText("Name:")

# lblFamily = QLabel()
# lblName.setText("Name:")

# lblEmail = QLabel()
# lblName.setText("Name:")

# lblAddress = QLabel()
# lblName.setText("Name:")

lblName = QLabel("Name:")
lblFamily = QLabel("Family:")
lblEmail = QLabel("Email:")
lblPhoneNumber = QLabel("Phone Number:")
lblAddress = QLabel("Address:")

btnAddPhoneNum = QPushButton("Enter")
btnSaveAllData = QPushButton("Save")

nameEdite = QLineEdit()
familyEdite = QLineEdit()
emailEdite = QLineEdit()
phoneNumberEdite = QLineEdit()
addressEdite = QTextEdit()

tblPhoneNum = QTableWidget()
tblAllData = QTableWidget()

gride = QGridLayout()
gride.setSpacing(10)

gride.addWidget(lblName, 1, 0)
gride.addWidget(nameEdite, 1, 1)

gride.addWidget(lblFamily, 2, 0)
gride.addWidget(familyEdite, 2, 1)

gride.addWidget(lblEmail, 3, 0)
gride.addWidget(emailEdite, 3, 1)

gride.addWidget(lblPhoneNumber, 1, 3)
gride.addWidget(phoneNumberEdite, 1, 4)
gride.addWidget(btnAddPhoneNum, 1, 5)
gride.addWidget(btnSaveAllData, 5, 7)

gride.addWidget(lblAddress, 4, 0,)
gride.addWidget(addressEdite, 4, 1)

addressEdite.setFixedWidth(300)
addressEdite.setFixedHeight(100)

gride.addWidget(tblAllData, 11, 1, 10, 5)
gride.addWidget(tblPhoneNum, 2, 4, 3, 4 )

# setting table phone Numbers
tblPhoneNum.setColumnCount(1)
tblPhoneNum.setHorizontalHeaderLabels([ 'Phone Number'])
tblPhoneNum.setColumnWidth(0, 270)
tblPhoneNum.resize(10,10)

# setting table All Data
tblAllData.setColumnCount(5)
tblAllData.setHorizontalHeaderLabels([ 'Name', 'Family', 'Email', 'Phone Number', 'Address'])
tblAllData.setColumnWidth(4, 270)
tblAllData.resize(10,10)

def insertPhoNUm(tbl, inpPhoNum):
    
    takeInpPhoNum = inpPhoNum.text()
   
    rowPosition = tbl.rowCount()
    
    try:
      if rowPosition <= 3:
        
        tbl.insertRow(rowPosition)
        tbl.setItem(rowPosition ,0 , QTableWidgetItem(takeInpPhoNum) )
      else:
        print("you can't Insert More...")
    except:
        print(5454)

btnAddPhoneNum.clicked.connect(lambda: insertPhoNUm(tblPhoneNum, phoneNumberEdite))

def insertAllData(tbl2, inpAllData):
    
    takeInpName = nameEdite.text()
    takeInpFamily = familyEdite.text()
    takeInpEmail = emailEdite.text()
    # takeInpAddress = addressEdite.text()

    rowPosition = tbl2.rowCount()
    
    try:
      if rowPosition <100:
        tbl2.insertRow(rowPosition)
        tbl2.setItem(rowPosition ,0 ,QTableWidgetItem(takeInpName) )
        tbl2.setItem(rowPosition ,1 ,QTableWidgetItem(takeInpFamily) )
        tbl2.setItem(rowPosition ,2 ,QTableWidgetItem(takeInpEmail) )
        # tbl2.setItem(rowPosition ,4 ,QTableWidgetItem(takeInpAddress) )

    except:

        print(5454)
btnSaveAllData.clicked.connect(lambda: insertAllData(tblAllData, btnSaveAllData))



window.setLayout(gride)
window.show()
app.exec()
