from PyQt5 import uic, QtWidgets
from autenticacao import Login
from win10toast import ToastNotifier




def fazer_login():

    login = formulario.login.text()
    senha = formulario.senha.text()

    login = str(login)
    senha = str(senha)

    res = Login.autenticacao_usuario(login)
    res02 = Login.autenticacao_senha(senha)

    toaster = ToastNotifier()

    if res == True and res02 == True:
        toaster.show_toast(
            "Autenticado",
            threaded=True,
            icon_path=None,
            duration=10)
    elif res != True or res02 != True:
         toaster.show_toast(
            "Não Autenticado, Tente Novamente!",
            threaded=True,
            icon_path=None,
            duration=10)

    formulario.login.setText('')
    formulario.senha.setText('')

   

app = QtWidgets.QApplication([])
formulario = uic.loadUi('telaLogin.ui')

formulario.entrar.clicked.connect(fazer_login)



formulario.show()

app.exec()

