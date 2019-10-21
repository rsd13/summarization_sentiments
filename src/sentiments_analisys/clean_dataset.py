import os
import pandas as pd
import spacy


def clean_acentos(word):
    """
    función que limpia los acentos
    :param word:
    :return:
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word

def clean_words(col, nlp):
    """
    función que realiza tokenización, postagging y el lema de las frases
    :param col: columna texto
    :param col: constructor en españoñ de Spacy
    :return: frase limpiada
    """
    doc = nlp(col)
    newText = ""
    for token in doc:
        #me quedo con las keywords, eliminando las demas palabras que perteenecen a todas las frases
        #y dan ruido a la hora de entrenar
        text = token.text
        if "@" not in text and  "http" not in text and "#" not in text:
            if token.pos_ == "NOUN" or token.pos_ == "VERB" or \
                    token.pos_ == "ADJ" or token.pos_ == "ADV":

                newText += clean_acentos(token.lemma_.lower()) + " "

    if newText != "":
        return newText


def clean_emocion(col):
    """
    limpia la columna emoción, las columnas etiquetadas como None, pasarán a NEU
    :return: columna limpiada
    """
    if col == "NONE":
        return "NEU"
    return col

def open_dataset():
    """
    función que abre el dataset
    :return: dataset en formato DataFrame
    """
    dir_path = os.path.dirname(os.path.abspath(__file__)) + "/../datasets/global_dataset.csv"
    return pd.read_csv(dir_path)


def save_dataset(dataset):
    """
    función que guarda el dataset limpip
    :return: dataset en formato DataFrame
    """
    dir_path = os.path.dirname(os.path.abspath(__file__)) + "/../datasets/global_clean.csv"
    dataset.to_csv(dir_path, index=False)



def clean_dataset():

    dataset = open_dataset()
    dataset.drop(columns="id", axis=1, inplace=True)
    dataset.emocion = dataset.emocion.apply(clean_emocion)
    #limpio la columna 'frase' para su futuro analisis
    nlp = spacy.load('es_core_news_md')
    #nlp = spacy.load('es_core_news_sm')
    dataset.frase = dataset.frase.apply(clean_words, args=(nlp, ))
    #borro los nulos
    data_null = dataset[dataset.frase.isnull()]
    dataset = dataset.drop(data_null.index)
    save_dataset(dataset)



clean_dataset()




