import PySimpleGUI as sg
import time
import threading
import funcoes
import db

sg.theme('Reddit')

login = sg.Window('entrar'.upper(), [
    [sg.Text('Login')],
    [sg.Input(key='-NOME-')],
    [sg.Text('Senha')],
    [sg.Input(key="-SENHA-", password_char='*')],
    [sg.Text('', key='-OUTPUT-')],
    [sg.Button('Entrar'), sg.Button('Cadastrar')]
],
    finalize=True)

regist = sg.Window('cadastrar'.upper(), [
    [sg.Text('Cadastrar'.upper(), justification='center')],
    [sg.Text('Usuário')],
    [sg.Input()],
    [sg.Text('Senha')],
    [sg.Input(password_char='*')],
    [sg.Text('Confirmar senha')],
    [sg.Input(password_char='*')],
    [sg.Text('', key='-OUTPUT-')],
    [sg.Button('Cadastrar'), sg.Button('Voltar')]
],
    finalize=True
)

logado = False
c = 0

regist.hide()
while True:
    database = db.Database()

    window, ev, vl = sg.read_all_windows(timeout=1000)

    if ev == sg.WINDOW_CLOSED:
        break

    if window == login and ev == 'Cadastrar':
        regist.un_hide()
        login['-OUTPUT-'].update('')
        login.hide()
        for item in vl.keys():
            login[item].update('')

    if window == login and ev == 'Entrar':
        users = database.verUsuarios()
        if funcoes.verif_login(vl['-NOME-'], vl['-SENHA-'], users) == True:
            login['-OUTPUT-'].update('Logado com sucesso')
            logado = True
            login.disable()

        else:
            login['-OUTPUT-'].update('Erro no login')
            
        for item in vl.keys():
            login[item].update('')

    if logado:
        c += 1
        if c == 3:
            break

    if window == regist and ev == 'Voltar':
        regist.hide()
        for item in vl.keys():
            regist[item].update('')
            
        login.un_hide()

    if window == regist and ev == 'Cadastrar':
        users = database.verUsuarios()
        if funcoes.verif_cadastro(vl[0], vl[1], vl[2], users) == True:
                database.adicionarUsuario(vl[0], vl[1])
                regist['-OUTPUT-'].update('Cadastrado com sucesso')
        else:
            regist['-OUTPUT-'].update('Não foi possível realizar o cadastro')

login.close()
regist.close()

#abrirPrograma()