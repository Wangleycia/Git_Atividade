#Importanto as bibliotecas que serão usadas
import  numpy as np
from random import randint
#Criando a class Tabuleiro
class Tabuleiro:
    def __init__(self)->None:
        self.casas=np.array[[" "," "," "],[" "," "," "],[" "," "," "]]
        '''Args:
        -self.casas=np.array[[" "," "," "],[" "," "," "],[" "," "," "]]
        criando as casas
        '''
        '''Returns:
        -Retornos None
        '''
        
    def casa(self)->list:
        '''Args:
        -recebendo as casas da função __init__
        '''
        '''Returns:
        -print(f"{self.casas}"): retornando as casas
        '''
        print(f"{self.casas}")

    def pegar_tabuleiro(self)->list:
        '''Args:
        Separando a lista de lista com o método split
        '''
        self.novo=np.array_split(self.casas)
        
        '''returns:
        retornando a lista separada
        '''
        print(f"{self.novo}")

    def marcar_casa(self,linha:int,coluna:int,simbolo:str)->bool:
        '''Args:
        linha:int,coluna:int, simbolo:str
        Recebendo a linha e coluna que será adicionado o simbolo conrespondente
        '''
        if  self.casa[linha,coluna] == " ":
            self.casa[linha,coluna]==simbolo
        else:
            print("Infelizmente essa casa já esta preenchida!")
            return False
        '''Returns:
        Retornando valores bool para cada condição
        '''
        return True

    def imprimir_tabuleiro(self)->list:
        self.nova_casa=self.casas.reshape(3,3)
        '''Args:
        Redefinindo as dimensões da lista
        '''

        '''Returns:
        Retornando a lista com as novas dimensões
        '''
        print(f"{self.nova_casa}")


#Criando a class Jogador
class  Jogador:
    def __init__(self,nome:str,simbolo:str)->None:
        self.nome=nome
        self.simbolo=simbolo
        '''Args:
        (nome:str,simbolo:str)-recebendo os parâmetros e definindo eles
        '''
        
        '''Returns:
        None
        '''
        
    def fazer_jogada(self,linha:int,coluna:int)->None:
        '''Args:
        (linha:int,coluna:int)-recebendo a linha e coluna
        e usando a função marcar_casa para marcar a casa
        '''
        Tabuleiro.marcar_casa(linha,coluna,self.simbolo)
        '''Returns:
        None
        '''


#Criando a class JogadorHumano
class JogadorHumano(Jogador):
    def fazer_jogada(self)->str:
        '''Criação de um loop para pegar a jogada, caso a casa não
        esteja de acordo retornando uma mensagem de error.
        '''
        while True:
            try:
                linha=int(input("Digite a linha escolhida sendo de 0 a 2:"))
                coluna=int(input("Digite a coluna escolhida sendo de 0 a 2:"))
                if self.Tabuleiro.marcar_casa(linha, coluna,self.simbolo):
                    break
            except(ValueError,IndexError):
                print("Error, tente novamente")
                

#Criando a class JogadorComputador
class JogadorComputador(Jogador):
    def __init__(self)->None:
        '''Args:
        self.lista=[]-Lista para armazenar as estrátegias.
        '''
        self.lista=[]
        '''Returns: None
        '''
        
    def fazer_jogada(self)->None:
        '''Criando um loop e usando a estrátegia para marcar uma casa'''
        
        '''Args:
            self.estrategia=random.randint(0,2)-Definindo a estrátegia a partir de um
            loop
            linha=self.estrategia-Definindo a linha
            coluna=self.estrategia-Definindo a coluna
        '''
        while True:
            self.estrategia=random.randint(0,8)
            linha=self.estrategia
            coluna=self.estrategia
            if self.marcar_casa(tabuleiro,linha,coluna)==" ":
                self.Tabuleiro.marcar_casa(linha,coluna)==self.simbolo
                self.lista.append(self.estrategia)
                break
        '''Returns: None
        '''


#Criando a class Jogodavelha
class JogoVelha:
    def __init__(self)->None:
        '''Args:
        self.jogadores=[
            JogadorHumano("Jogador.H", "O"),
            JogadorRobo("Jogador.R","X")
        ] Criando os jogadores
        self.tabuleiro=Tabuleiro()-Definindo o tabuleiro
        self.turno=0-Criando o turno
        '''
        self.jogadores=[
            JogadorHumano("Jogador.H", "O"),
            JogadorComputador("Jogador.R","X")
        ]
        self.tabuleiro=Tabuleiro()
        self.turno=0
        '''Returns: None '''
    def checar_vitoria(self)->None:
      '''Determinando o ganhador a partir de condições'''
      for i in range(3):
          if (self.casa.array[0]==self.jogador_atual.simbolo or
          self.casa.array[1]==self.jogador_atual.simbolo or
          self.casa.array[2]==self.jogador_atual.simbolo):
              print(f"Vitória do {jogador.atual}")

          if (self.casa.array([0][0] | [0][2])==self.jogador_atual.simbolo and
          self.casa.array[1][1]==self.jogador_atual.simbolo and
          self.casa.array([2][2] | [2][0])==self.jogador_atual.simbolo):
              print(f"Vitória do {jogador.atual}")

          else:
              print("Empate!")
          '''Retornos:
           return None
          '''
          return None
      
    def jogar(self)->str:
        '''Definindo a função'''
        print("Bem-vindo ao Jogo da velha")
        self.lances=0
        '''Args:
            self.tabuleiro.imprimir_tabuleiro()-Imprimir o tabuleiro
            jogador_atual=self.jogadores[self.turno]-determinando o jogador atual
            jogada=jogador_atual.fazer_jogada()-Fazer a jogada
        '''
        while True:
            self.tabuleiro.imprimir_tabuleiro()
            jogador_atual=self.jogadores[self.turno]
            jogada=jogador_atual.fazer_jogada()
            '''Returns:
            print(f"Jogador atual {jogador_atual}:{jogada}")-Mostrar o jogador atual
            e a sua jogada
            '''
            print(f"Jogador atual {jogador_atual}:{jogada}")
            lances+=1
            if lances>=3 or lances==9 or lances==5:
                break
            self.turno=(self.turno+1)%2
            
        resultado=self.checar_vitoria()
        print(resultado)

#Teste:
jogo=JogoVelha()
jogo.jogar()
