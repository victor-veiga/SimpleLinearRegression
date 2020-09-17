# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:00:09 2020

@author: victor.veiga
"""


"Todas as funções de estatísticas"

def minimo(lista: list) -> float:
    """Funcao para encontrar o menor valor em uma dada lista.   
    argumentos:
        arquivo(list) = lista a ser avaliada
    
    ex: minimo([1,2,3])
    retorna: 1
    """
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo

def maximo(lista: list) -> float:
    """Funcao para encontrar o menor valor em uma dada lista.   
    argumentos:
        arquivo(list) = lista a ser avaliada
    
    ex: maximo([1,2,3])
    retorna: 1
    """
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

def n_raiz(x, n):
    """Função para encontrar a n-ésima raiz de um número real.
    
    argumentos:
        x(int) = Número real que se deseja encontrar a raiz.
        n(int) = Indicaçao de qual raiz se deseja calcular.
    
    ex: n_raiz(16,2)
    retorna: 4
    """
    #Sabendo que a n-ésima raiz pode ser encarada como um número elevado a (1/n)
    return x ** (1/n)

def soma_lista(lista):
    """Função para encontrar a soma de uma dada lista.
    
    argumentos:
        lista(list) = lista a ser somada.
    
    ex: soma_lista([1,2,3])
    retorna: 6
    """
    soma = 0
    for item in lista:
        soma += item
    return soma

def media_lista(lista):
    """Função para encontrar a média de uma dada lista.
    
    argumentos:
        lista(list) = lista para a média.
    
    ex: media_lista([1,2,3])
    retorna: 2
    """
    media = soma_lista(lista)/len(lista)
    return media

def variancia(l: list) -> float:
    """Função para encontrar a variância de uma dada lista.
    Args:
        l (list): lista para se encontrar a variância.
    Returns:
        float: variância da lista inserida
    """
    media = media_lista(l)
    tamanho = len(l)
    
    diff_quad = [(x-media) ** 2 for x in l] 
    soma = soma_lista(diff_quad)
    var = soma / (tamanho - 1)      #tamanho - 1 ou apenas tamanho?
    return var


def cova(lista1, lista2):
    """Função para encontrar a covariancia entre duas listas.
    
    argumentos:
        lista1(list) = Primeira lista.
        lista2(list) = Segunda lista.
    
    ex: cova([1,2,3], [3,2,1])
    retorna: -1.0
    """
    #Aqui, o n do divisor será o número de elementos da lista
    n = len(lista1)
    
    media1 = media_lista(lista1)
    media2 = media_lista(lista2)
    
    #No numerador teremos o somatório da multiplicaçao entre (xi - xmed) e (yi - ymed)
    var = soma_lista([(lista1[item]-media1) * (lista2[item]-media2) for item in range(len(lista1))])
   
    #E para a covariancia da amostra, dividimos o resultado por n-1
    cov = (var/(n-1))
    return cov

def fit(x_features: list, y_target: list) -> tuple:
    """Função para realizar o ajuste linear entre 2 listas de variáveis, sendo uma feature e um target.
    Args:
         x_features (list): lista com os valores da feature utilizada para a previsão
         y_target (list): lista com os valores do target
    Returns:
        alpha(float): parâmetro alpha da regressão linear
        beta(float): parâmetro beta da regressão linear
    """
    y_media = media_lista(y_target)
    x_media = media_lista(x_features)

    beta = cova(x_features, y_target) / variancia(x_features)
    alpha = y_media - (beta*x_media)
    return alpha, beta

def pred(alpha: float, beta: float, x_features: list) -> list:
    """Função para fazer a previsão a partir de um ajuste linear
    Args:
        alpha(float): parâmetro alpha da regressão linear
        beta(float): parâmetro beta da regressão linear
        x_features (list): lista com os valores da feature utilizada para a previsão
    Returns:
        list: Lista com os valores previstos
    """
    y_hat = [alpha + (beta*x) for x in x_features]
    return y_hat

def rmse(observado, previsto):
    """Função para encontrar a raiz do erro médio quadrático entre duas listas.
    
    argumentos:
        observado(list) = lista com os valores reais(observados).
        previsto(list) =  lista com os valors previstos.
    
    ex: 
    alpha, beta = fit(dict_values['RM'], dict_values['MEDV'])   
    previsto = pred(alpha, beta, dict_values['RM'] )
    observado = dict_values['MEDV']
    rmse(observado, previsto)
    retorna: ******
    """
    #Primeiro calculo o erro quadrático, depois temos a raiz para o rmse
    erro_quadratico = (soma_lista([((observado[item]-previsto[item])**2) for item in range(len(previsto))]))/len(previsto)
    rmse = n_raiz(erro_quadratico, 2)
    return rmse