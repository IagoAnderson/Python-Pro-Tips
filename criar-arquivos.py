# Iago Anderson Pereira file

#Como criar multiplos arquivos de uma só vez em python

import os

def criar_arquivos(inicio, fim):
  for i in range(inicio, fim + 1):

    filename = f"nome_do_arquivo{i:03}.py" #Escreva o nome do arquivo aqui!, 
    # 03 significa a quantidade de caracteres ou seja 000 a 999

    with open(filename, "w") as f:
      f.write("print('Olá, mundo!')")

if __name__ == "__main__":
  criar_arquivos(1, 10) #Escreva a quantidade de arquivos que você deseja criar