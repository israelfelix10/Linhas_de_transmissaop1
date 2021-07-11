import math
import cmath
import os
from tkinter import* 

#função q6
def prova2():
 #convertendo uma fonte de corrente em tensão
 vs = 0.5*100
 z0 = 50
 zg = 100

 # agora encontramos a relação Beta*l

 pi = math.pi
 beta = 2*pi*2.6

 # encontrando a impedância inicial da linha

 a = (25 + (50j*math.tan(beta)))
 b = (50 + (25j*math.tan(beta)))
 zin = 50*(a / b)
 realy1 = round(zin.real,3)
 img2 = round(zin.imag,3)
 zins = complex(realy1,img2)

 # Devemos encontrar a tensão de entrada

 vin = vs*(zin/(100+zin))

 # Definir quem é a corrente de entrada I(z=0)
 i0 = vs/(zin+zg)
 print(i0)

 # Encontramos a tensão de entrada
 v0 = zin*i0
 print(v0)

 # Devemos encontrar a tensão de propagação inicial
 v0plus = (1/2)*(v0+(z0*i0))

 print(v0plus)

 # Finalmente vamos encontrar a potência absorvida (média).

 pz = (1/2)*(((v0plus)**2)/z0)*(1-(((25-50)/(25+50)))**2)
 realy = round(pz.real,3)
 img = round(pz.imag,3)
 z = complex(realy,img)
 

 #RESULTADOS
 texto = f'''
 RESULTADOS:

 Impedância de Entrada: {zins}
 Potência P(z) em Complexos: {z}
 '''
 texto_calculos ["text"] = texto

#funcao geral
def prova():
 fc = float(caixa_fcorrente.get())
 rfc = float(caixa_rcorrente.get())
 clinha = float(caixa_clinha.get())
 carga = float(caixa_carga.get())
 z0 = float(caixa_z0.get())
 zg = float(caixa_rcorrente.get())
 
  #convertendo uma fonte de corrente em tensão
 vs = fc*rfc
 

 # agora encontramos a relação Beta*l

 pi = math.pi
 beta = 2*pi*clinha

 # encontrando a impedância inicial da linha
 z1=complex(carga,z0)
 z2=complex(z0,carga)
 z11= (z1.imag*math.tan(beta))
 z21= (z2.imag*math.tan(beta))
 a = complex(carga,z11)
 b = complex(z0,z21)
 zin = z0*(a / b)
 realy1 = round(zin.real,3)
 img2 = round(zin.imag,3)
 zins = complex(realy1,img2)
 
 
 print(zin)

 # Devemos encontrar a tensão de entrada

 vin = vs*(zin/(zg+zin))

 # Definir quem é a corrente de entrada I(z=0)
 i0 = vs/(zin+zg)
 print(i0)

 # Encontramos a tensão de entrada
 v0 = zin*i0
 print(v0)

 # Devemos encontrar a tensão de propagação inicial
 v0plus = (1/2)*(v0+(z0*i0))

 print(v0plus)

 # Finalmente vamos encontrar a potência absorvida (média).

 pz = (1/2)*(((v0plus)**2)/z0)*(1-(((carga-z0)/(carga+z0)))**2)
 realy = round(pz.real,3)
 img = round(pz.imag,3)
 z = complex(realy,img)
 
 

 #RESULTADOS
 texto = f'''
 RESULTADOS:

 Impedância de Entrada: {zins}
 Potência P(z) em Complexo: {z} 
 '''

 texto_calculos ["text"] = texto

#INTERFACE

janela = Tk()
janela.title("Cáculo da Impedância de Entrada e Potência de uma L.T.")
janela.geometry("700x600")

#CABECALHO DA JANELA
txt_ori = Label(janela, text='Clique no botão para calcular a impedância de entrada e a potência da linha.')
txt_ori.grid(column=0, row=1, padx=70, pady=10)

#caixa para inserir os dados

#dados de z0
label_z0 = Label(janela, text='Insira o valor de Z0: ') 
label_z0.grid(column=0, row=2)
caixa_z0 = Entry(janela, justify="left")
caixa_z0.grid(column=1, row=2)

#dados da carga
label_carga = Label(janela, text='Insira o valor da carga (parte real): ') 
label_carga.grid(column=0, row=3)
caixa_carga = Entry(janela, justify="left")
caixa_carga.grid(column=1, row=3)

#dados de comprimento da linha
label_clinha = Label(janela, text='Insira o valor do comprimento da linha em termos de lambda (somente numero, ex: 2.6): ') 
label_clinha.grid(column=0, row=4)
caixa_clinha = Entry(janela, justify="left")
caixa_clinha.grid(column=1, row=4)

#Fonte de corrente 
label_fcorrente = Label(janela, text='Insira a parte real da fonte de corrente (ex: 0.5): ') 
label_fcorrente.grid(column=0, row=5)
caixa_fcorrente = Entry(janela, justify="left")
caixa_fcorrente.grid(column=1, row=5)

#Resistencia em paralelo com a fonte
label_rcorrente = Label(janela, text='Insira a resistencia em paraleo com a fonte de corrente: ') 
label_rcorrente.grid(column=0, row=6)
caixa_rcorrente = Entry(janela, justify="left")
caixa_rcorrente.grid(column=1, row=6)

#Botao para inserir dados
botao_d = Button(janela, text='Calcular', command=prova)
botao_d.grid(column=0, row=8, padx=10, pady=5)

botao = Button(janela, text='Calcular para o circuito base', command=prova2)
botao.grid(column=0, row=9, padx=10, pady=10)

#imprimir dados
texto_calculos = Label(janela, text='')
texto_calculos.grid(column=0, row=7, padx=10, pady=10)


#imagem na interface
txt_img = Label(janela, text='Circuito equivalente de uma linha de transmissão base para este progrma:')
txt_img.grid(column=0, row=11, padx=70, pady=10)

pastaApp = os.path.dirname(__file__)
imgo = PhotoImage(file=pastaApp+"\\q.png")
logo=Label(janela, image=imgo)
logo.grid(column=0, row=12, padx=10, pady=10)


janela.mainloop()