# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:28:24 2020

@author: victor.veiga
"""


import pandas as pd
import numpy as np


def test_le_csv(path_file: str) -> dict:
    """Função para ler o arquivo .csv
    Args:
        path_file (str): Nome do arquivo .csv ou o caminho dele
    Returns:
        dict: Dicionário onde cada chave corresponde a uma coluna do arquivo .csv
    """
    arquivo = pd.read_csv(path_file)
    
    return arquivo