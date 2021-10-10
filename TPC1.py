#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:01:25 2021

@author: beatrizalvadia
"""


 

def jogadorem1():
    x=21
    b=0
    while x>1:
        a=int(input("Quantos fósforos quer tirar? "))   
        b=5-a
        x=x-a-b
        print("Jogador 1:", a)
        print ("Total de fósforos:", x)
    print("VOCÊ PERDEU ESTA PARTIDA.")
 
         
          
def jogadorem2():
    print("    ")
    x=21    
    
    
    while x>1: 
       print("Jogador 1: 1")
       x=x-1
       print("Total de fósforos:", x) 
       a=int(input("Quantos fósforos quer tirar? "))  
       x=x-a
       
       if a!=4:
           c=5-a-1
           print("Jogador 1:", c)
           x=x-c
           print("Total de fósforos:", x)
           while x>1:
              a=int(input("Quantos fósforos quer tirar? "))   
              b=5-a
              print("Jogador 1:", b)
              x=x-a-b
              print ("Total de fósforos:", x)
              
              
           print("VOCÊ PERDEU ESTA PARTIDA.")       
       elif x==1:
           print("VOCÊ GANHOU ESTA PARTIDA.")



print("     ")
print("     ")
print("Olá! Bem-vindo ao jogo 21 FÓSFOROS!")

a=int(input("Selecione 1 para ser o Jogador 1, ou 2 para ser o Jogador 2:  "))
if a==1:
    jogadorem1() 
elif a==2: 
    jogadorem2()
else: 
    print("Por favor, selecione 1 ou 2.")
    
    

