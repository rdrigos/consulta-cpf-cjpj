from validate_docbr import CPF, CNPJ
import requests
from time import sleep
from tkinter import *
from tkinter import messagebox


master = Tk()
master.title("Verificação | DocBr")
master.geometry("400x214")
master.iconbitmap(default="icones\\icones.ico")


def janela_consulta_cnpj(documento):
    url = 'https://receitaws.com.br/v1/cnpj/{}'.format(documento)
    r = requests.get(url)
    dados = r.json()

    sleep(0.3)
    master1 = Tk()
    master1.geometry("900x504")
    master1.title("{}".format(dados['nome']))
    fontepadrao = ("Arial", "12", "bold")

    msg_resultados = Label(master1, text="Nome da Empresa:\n{}\nCNPJ:\n{}\nNatureza Juridica:\n{}\nData de Abertura:\n"
                                         "{}\nPonte:""\n{}\nLogadouro:\n{}\nNumero:\n{}\nCEP:\n{}\nUF:\n{}\nMunicipio:"
                                         "\n{}\nBairro:\n{}"
                           .format(dados['nome'], dados['cnpj'], dados['natureza_juridica'], dados['abertura'],
                                   dados['porte'], dados['logradouro'], dados['numero'], dados['cep'], dados['uf'],
                                   dados['municipio'], dados['bairro']))
    msg_resultados["font"] = fontepadrao
    msg_resultados.pack()


def verifica_documento():
    documento = entrada_documento.get().strip()
    if len(documento) == 11:
        cpf = CPF()
        verificacao = cpf.validate(f"{documento}")
        if verificacao == TRUE:
            cpf_formatado = cpf.mask(documento)
            messagebox.showinfo(title="CPF Válido!", message=f"O CPF: {cpf_formatado} é válido!")
        else:
            messagebox.showerror(title="Atenção!", message="O Documento Informado é inválido!")
    elif len(documento) == 14:
        cnpj = CNPJ()
        verificacao = cnpj.validate(f"{documento}")
        if verificacao == TRUE:
            janela_consulta_cnpj(documento)
        else:
            messagebox.showerror(title="Atenção!", message="O Documento Informado é inválido!")
    else:
        messagebox.showerror(title="Atenção!", message="Informe um documento válido!")


# Importando Imagens 
img_botao_veri = PhotoImage(file="imagens\\botao_buscar.png")
img_botao_sair = PhotoImage(file="imagens\\botao_sair.png")
background = PhotoImage(file="imagens\\background.png")

# Crianção de Labels
lab_background = Label(master, image=background)
lab_background.pack()

# Botões, inputs e outputs
entrada_documento = Entry(master, bd=2, font=("calibri", 16), justify=CENTER)
entrada_documento.place(width=315, height=40, x=44, y=95)
botao_verificar = Button(master, bd=0, image=img_botao_veri, command=verifica_documento)
botao_verificar.place(width=103, height=44, x=70, y=150)
botao_sair = Button(master, bd=0, image=img_botao_sair, command=master.destroy)
botao_sair.place(width=103, height=44, x=227, y=150)

master.mainloop()
