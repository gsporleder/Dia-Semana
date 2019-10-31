# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:28:52 2019

@author: 13106827
"""

''' Mensagem diferente para cada dia da semana
PADRÂO STRATEGY '''

class Dia:
    
    def _init_(self,dia):
        self.dia = dia
        
    def context_interface(self):
        self.dia.algoritmo_interface()
    
class Estrategia (meta=abc.abcmeta):
    
    @abc.metodoabstrato
    
    def algoritmo_interface(self):
        pass

class Seg (Estrategia):
    
    def algoritmo_interface(self):
        print ("Eh recem segunda e eu ja to cansado")

class Ter (Estrategia):
    
    def algoritmo_interface(self):
        print ("Terca! Vamo dale")

class Qua (Estrategia):
    
    def algoritmo_interface(self):
        print ("Aeee disgraca, ja tamo na quarta gracas a deus")
        
class Qui (Estrategia):
    
    def algoritmo_interface(self):
        print ("Quase la")

class Sex (Estrategia):
    
    def algoritmo_interface(self):
        print ("Sexta!!!! Vamoooooo")

def main():
    
    print ("Que dia voce quer?")
    Estrategia.algoritmo_interface = input()
    