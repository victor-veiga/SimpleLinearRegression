# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:06:29 2020

@author: victor.veiga
"""


"Arquivo teste"


import pandas as pd
import numpy as np


def test_minimo(lista: list) -> float:
    """Funcao para encontrar o menor valor em uma dada lista.   
    argumentos:
        arquivo(list) = lista a ser avaliada
    
    ex: minimo([1,2,3])
    retorna: 1
    """
    minimo = min(lista)
    
    return minimo

def test_maximo(lista: list) -> float:
    """Funcao para encontrar o menor valor em uma dada lista.   
    argumentos:
        arquivo(list) = lista a ser avaliada
    
    ex: maximo([1,2,3])
    retorna: 1
    """
    maximo = max(lista)
    
    return maximo


def test_n_raiz(x, n):   #E aí??
    """Função para encontrar a n-ésima raiz de um número real.
    
    argumentos:
        x(int) = Número real que se deseja encontrar a raiz.
        n(int) = Indicaçao de qual raiz se deseja calcular.
    
    ex: n_raiz(16,2)
    retorna: 4
    """
    #Sabendo que a n-ésima raiz pode ser encarada como um número elevado a (1/n)
    return x ** (1/n)
   
def test_soma_lista(lista):
    """Função para encontrar a soma de uma dada lista.
    
    argumentos:
        lista(list) = lista a ser somada.
    
    ex: soma_lista([1,2,3])
    retorna: 6
    """
    soma = sum(lista)
    
    return soma

def test_media_lista(lista):
    """Função para encontrar a média de uma dada lista.
    
    argumentos:
        lista(list) = lista para a média.
    
    ex: media_lista([1,2,3])
    retorna: 2
    """
    media = lista.mean()
    return media
   
def test_variancia(l: list) -> float:
    """Função para encontrar a variância de uma dada lista.
    Args:
        l (list): lista para se encontrar a variância.
    Returns:
        float: variância da lista inserida
    """
    var = np.var(l)     #tamanho - 1 ou apenas tamanho?
    return var   