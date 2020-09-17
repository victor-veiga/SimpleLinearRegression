# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:03:16 2020

@author: victor.veiga
"""

from auxiliar import le_csv
import statistics as st

def main():
    data = le_csv('dataset.csv')   #Tem que importar a pasta?
    alpha, beta = st.fit(data.RM, data.MEDV)
    previsto = st.pred(alpha, beta, data.RM)
    observado = data.MEDV
    RMSE = st.rmse(observado, previsto)

    print(f"""[RM => MEDV] 
    Root-mean-square deviation:{RMSE}
    Alpha:{alpha}
    Beta:{beta}
    Predicted Values:{previsto}
    Expected Values:{observado}
    """)





