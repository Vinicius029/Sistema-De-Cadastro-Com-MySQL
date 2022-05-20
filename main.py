from PyQt5 import uic, QtWidgets

def autenticacao_usuario(login):

    usuario = 'admin'
    i = 0
    while i < len(login):
        if login[i] != usuario[i]:
            return False
            break
        i += 1
    return True


def autenticacao_senha(senha):
    s = 'python'
    i = 0
    while i < len(senha):
        if senha[i] != s[i]:
            return False
            break
        i += 1
    return True


def teste():

    login = formulario.login.text()
    senha = formulario.senha.text()

    login = str(login)
    senha = str(senha)

    res = autenticacao_usuario(login)
    res02 = autenticacao_senha(senha)

    if res == True and res02 == True:
        print("autenticado")
    elif res != True or res02 != True:
        print("Não autenticado")

    formulario.login.setText('')

   

app = QtWidgets.QApplication([])
formulario = uic.loadUi('telaLogin.ui')

formulario.entrar.clicked.connect(teste)



formulario.show()

app.exec()

