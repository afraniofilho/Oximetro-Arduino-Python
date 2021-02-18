#Importar bibliotecas

import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *

oxF = []

arduinoData = serial.Serial('com3', 115200) # cria um objeto serial (arduinoData) na porta de comunicação 'com3'
plt.ion()       #Configura o matplotlib no modo interativo para atualizar automatico
cnt = 0

def makeFig(): # Criar uma função para o gráfico
    plt.ylim(70, 100)
    plt.title('Saturação do Oxigênio %')
    plt.grid(True)
    plt.ylabel('%')
    plt.plot(oxF, 'ro-')


while True:
    arduinoString = arduinoData.readline() #ler uma linha da porta serial
    dataArray = arduinoString[:2]      #ler os 2 primeiros caracteres (valor do oxigenio)
    ox = float(dataArray)     # converte em float e guarda em ox
    oxF.append(ox)            # cria um array adicionando as leituras de ox
    drawnow(makeFig)          # chamar função do gráfico
    cnt=cnt+1
    if(cnt>20):
        oxF.pop(0)



    


