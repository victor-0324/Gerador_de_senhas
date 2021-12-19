import PySimpleGUI as sg
import secrets
import string
import uuid

#janela1
def tela_inicial():
    sg.theme('Reddit')
    layout = [
        [sg.Text('###############')],
        [sg.Text('Digite uma senha: '),sg.Text(key='entrada'),sg.InputText(key='senha',size=(10,1))],
        [sg.Button('Gerar Senha'),sg.Button('Guarda Senha')]       
    ]
    return sg.Window('Gerador de senha', layout=layout,finalize=True) 

def se_guarda():
    pass


#janela2
def gerador_senhas(Senha):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for i in range(Senha))
    
    sg.theme('Reddit')
    layout = [       
        [sg.Text(password,size=(20,1))],
        [sg.Button('Guarda senha'),sg.Button('Cancela')],
    ]

    return sg.Window('senha gerada', layout=layout,finalize=True)
    
janela1, janela2, janela3 = tela_inicial(), None , None

while True:
    window,event,value = sg.read_all_windows()
 
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    elif window == janela1 and event == 'Gerar Senha':
        janela2 = gerador_senhas(16)       
        janela1.hide()
    elif window ==janela2 and event =='Cancela':
        janela2.hide()
        janela1.un_hide()
    elif window == janela1 and event == 'Guarda Senha':
        input_text = value['senha']
        window['senha'].update(input_text)
        window['entrada'].update(input_text)
        
