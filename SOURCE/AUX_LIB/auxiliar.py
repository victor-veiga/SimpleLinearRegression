# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:54:49 2020

@author: victor.veiga
"""

"""Função de leitura de um arquivo .csv e quaisquer outras que você desejar e 
julgar necessário para a sua pequena aplicação"""

import csv
from collections import defaultdict

def le_csv(path_file: str) -> dict:
    """Função para ler o arquivo .csv
    Args:
        path_file (str): Nome do arquivo .csv ou o caminho dele
    Returns:
        dict: Dicionário onde cada chave corresponde a uma coluna do arquivo .csv
    """
    with open(path_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dict_values = defaultdict(list)
        for row in reader:
            for key, value in row.items():
                dict_values[key].append(float(value))
    return dict_values
