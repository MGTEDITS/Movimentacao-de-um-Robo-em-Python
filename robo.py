# Projeto
# Nome do projeto: Movimentação de um robô
# Descricao: Fazer o robô percorrer o mapa fornecido "mapa.txt" de forma manual (W/A/S/D)
# ou de forma automática (random)
# Projeto realizado por:
# Nome: Marco Bertolo
# Numero: 2023127
# Turma: Turma A Diurno
# usar o pip install keyboard para o keyboard.

#Importacoes para fazer o random, o sleep, o cls e o key sencitive
import random
import time
import os
import keyboard


#Funcao para limpar a consola
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Funcao que vai ler o nosso ficheiro mapa.txt e passar para a matriz map
def readMap(arquive):
    with open(arquive, 'r') as f:
        map = [l.strip().split() for l in f.readlines()]
    return map

#Funcao que vai imprimir a nossa matriz para a consola
def printMap(map, pos):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i, j) == pos:
                print("R", end=' ')
            else:
                print(map[i][j], end=' ')
        print()
    print()


#Funcao para mover o robot para a posicao com base no imput colocado
def moveRobot(map, pos, mov):
    x, y = pos
    if mov == 'W' and x > 0:
        nPos = (x - 1, y)
    elif mov == 'S' and x < len(map) - 1:
        nPos = (x + 1, y)
    elif mov == 'A' and y > 0:
        nPos = (x, y - 1)
    elif mov == 'D' and y < len(map[0]) - 1:
        nPos = (x, y + 1)
    else:
        print("Fora do mapa! Tenta outra direção.")  # Aviso quando sai do mapa
        return pos

    if map[nPos[0]][nPos[1]] != '#':
        return nPos
    else:
        print("Está a bater contra o obstáculo!")

    return pos

#Funcao para gerar um movimento com o uso do random para fazer o movimento automatico
def randomMovement(map, pos):
    mov = ['W', 'A', 'S', 'D']
    while pos != (9, 9):
        cls()
        mov = random.choice(mov)
        pos = moveRobot(map, pos, mov)
        printMap(map, pos)
        time.sleep(0.5)


#Funcao principal do programa
def main():
    map = readMap('mapa.txt')
    pos = (0, 0)
    printMap(map, pos)

    c = input("Escolhe 'A' para o robo se movimentar automaticamente ou 'M' para controlar o robo manualmente: ").strip().upper()
    if c == 'A':
        randomMovement(map, pos)
    elif c == 'M':
        while pos != (9, 9):
            print("Move (W/A/S/D):")
            while True:
                if keyboard.is_pressed('w'):
                    mov = 'W'
                    break
                elif keyboard.is_pressed('a'):
                    mov = 'A'
                    break
                elif keyboard.is_pressed('s'):
                    mov = 'S'
                    break
                elif keyboard.is_pressed('d'):
                    mov = 'D'
                    break
            cls()
            pos = moveRobot(map, pos, mov)
            printMap(map, pos)
            time.sleep(0.2)
    else:
        print("Tecla Invalida.")

if __name__ == "__main__":
    main()