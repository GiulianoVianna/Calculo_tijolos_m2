
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox



def mensagem():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar a largura, altura e o tipo de tijolo!')
        x = msg1.exec()


def calcular():
    ln1 = tela.ln_largura.text()
    ln2 = tela.ln_altura.text()
    tijolo =  tela.cb_tijolos.currentText()

    if ln1 == "" or ln2 == "" or tijolo == "":
        mensagem()
    else:
        largura = float(ln1)
        altura = float(ln2)
        if tijolo == "6 furos":
            resultado1 = (largura * altura) / 0.0252
            tela.ln_qt_tijolos.setText(f'{resultado1:,.0f}'.format(resultado1).replace(",", "X").replace(".", ",").replace("X", "."))

        elif tijolo == "8 furos":
            resultado2 = (largura * altura) / 0.0361
            tela.ln_qt_tijolos.setText(f'{resultado2:,.0f}'.format(resultado2).replace(",", "X").replace(".", ",").replace("X", "."))

        elif tijolo == "9 furos":
            resultado3 = (largura * altura) / 0.0551
            tela.ln_qt_tijolos.setText(f'{resultado3:,.0f}'.format(resultado3).replace(",", "X").replace(".", ",").replace("X", "."))
      
        m2 = largura * altura
        tela.ln_total_m2.setText(f'{m2:,.2f}'.format(m2).replace(",", "X").replace(".", ",").replace("X", "."))



app = QtWidgets.QApplication([])
tela = uic.loadUi("tijolos.ui")
tela.pb_calcular.clicked.connect(calcular)

tela.show()
app.exec()