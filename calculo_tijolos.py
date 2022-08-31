
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox



def mensagem_largura():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar a largura!')
        x = msg1.exec()

def mensagem_altura():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar a altura!')
        x = msg1.exec()

def mensagem_tipo_tijolo():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar o tipo de tijolo!')
        x = msg1.exec()

def calcular():

    ln1 = tela.ln_largura.text().replace(",", ".") # replace() - Se o usuário utilizar , - ex: 1,10 faz a correção para 1.10
    ln2 = tela.ln_altura.text().replace(",", ".")
    
    tijolo =  tela.cb_tijolos.currentText()

    if ln1 == "":
        mensagem_largura()

    elif ln2 == "":
        mensagem_altura()
        
    elif tijolo == "":
        mensagem_tipo_tijolo()

    else:
        largura = float(ln1)
        altura = float(ln2)

        if tijolo == "6 furos":
            # 0.0252 - medida em m2 do tijolo de 6 furos
            tela.ln_qt_tijolos.setText(f'{(largura * altura) / 0.0252:,.0f}'.replace(",", "X").replace(".", ",").replace("X", "."))

        elif tijolo == "8 furos":
            # 0.0361 - medida em m2 do tijolo de 8 furos
            tela.ln_qt_tijolos.setText(f'{(largura * altura) / 0.0361:,.0f}'.replace(",", "X").replace(".", ",").replace("X", "."))

        elif tijolo == "9 furos":
            # 0.0551 - medida em m2 do tijolo de 9 furos
            tela.ln_qt_tijolos.setText(f'{(largura * altura) / 0.0551:,.0f}'.replace(",", "X").replace(".", ",").replace("X", "."))      

        tela.ln_total_m2.setText(f'{largura * altura:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))



app = QtWidgets.QApplication([])
tela = uic.loadUi("tijolos.ui")
tela.pb_calcular.clicked.connect(calcular)

tela.show()
app.exec()