import os
import sqlite3
from joblib import load
import pandas as pd
from .graficas import freq_word, get_plot_filter



def conn():
    """
    devuelve las reviews de un local de la bbdd en forma de DataFrame
    """
    try:
        dir_path = os.path.dirname(os.path.abspath(__file__)) + "/../../db.sqlite3"
        print(dir_path)
        bbdd = sqlite3.connect(dir_path, timeout=10)
        bbdd.row_factory = sqlite3.Row
        return bbdd.cursor()
    except:
        raise ("Error a conectar a la base de datos.")

    return ""

def queery(cursor, id, año):
    cursor.execute("""
                    SELECT *
                    FROM sumtravel_review
                    WHERE local_id = ? and 
                    año = ?

                    """, (id,año))
    rows = cursor.fetchall()


    lst = []
    for row in rows:
        dic = {}
        text = row[1]
        dic["frase"] = text
        dic["mes"] = row[3]
        dic["año"] = row[4]
        dic["sentimiento"] = row[2]
        lst.append(dic)

    return pd.DataFrame(lst)


def get_sum_filter(id,nlp, año):

    datos = queery(conn(), id, año)
    #lo ordeno por mes
    datos.sort_values(by=['mes'], inplace=True)

    dic = {}
    frases_positivas = datos[datos.sentimiento == "P"]
    frases_negativas = datos[datos.sentimiento == "N"]
    frases_neutras = datos[datos.sentimiento == "NEU"]
    dic["grafica_positiva"] = get_plot_filter(frases_positivas)
    dic["grafica_negativa"] = get_plot_filter(frases_negativas)
    dic["grafica_neutra"] = get_plot_filter(frases_neutras)

    id = str(id)
    dic["conteo_noun_pos"], dic["conteo_ajd_pos"] = freq_word(frases_positivas, nlp, id, "pos")

    dic["conteo_noun_neg"], dic["conteo_ajd_neg"] = freq_word(frases_negativas, nlp, id, "neg")


    return dic

