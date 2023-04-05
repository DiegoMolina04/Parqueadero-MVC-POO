from PyQt5 import QtWidgets
import sys
from view.login import Ui_Form
from controller.MainController import MainController

if __name__ == "__main__":
    MainController.initElements()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())