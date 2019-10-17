import os
import sqlite3
from joblib import load
import pandas as pd

def conn():

    try:
        dir_path = os.path.dirname(os.path.abspath(__file__)) + "/../mysite/db.sqlite3"

        bbdd = sqlite3.connect(dir_path, timeout=10)
        bbdd.row_factory = sqlite3.Row
        return bbdd.cursor()
    except:
        raise ("Error a conectar a la base de datos.")

    return ""

def queery(cursor):
    cursor.execute("""
                    SELECT *
                    FROM sumtravel_review
                    WHERE local_id = ?

                    """, (2,))
    rows = cursor.fetchall()
    clf = load('filename.joblib')

    lst = []
    for row in rows:
        dic = {}
        text = row[1]
        dic["frase"] = text

        dic["sentimiento"] = clf.predict([text])[0]
        lst.append(dic)

    return pd.DataFrame(lst)


def main():
    datos = queery(conn())
    print(datos)

print("dsfsdf")
main()
