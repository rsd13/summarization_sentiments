from nltk import FreqDist
from functools import reduce
from wordcloud import WordCloud
import os

def get_plot(datos):
    """
    función que da información sobre cuantos reviews positivas, negativas y neutras da
    :param datos: frases positivas, negativas o neutras a contar
    """
    positivas_años = datos.groupby('año').agg(['count'])
    group = positivas_años.to_dict('sentimiento')
    group = group[('frase', 'count')]

    lst = []
    for k, v in group.items():
        dic = {}
        dic["año"],dic["cantidad"] = k,v
        lst.append(dic)

    return lst


def word_cloud(corpus, name):
    dir_path = os.path.dirname(os.path.abspath(__file__)) +"/../static/sumtravel/img/worcloud/"
    dir_path += name + ".png"
    print(dir_path)
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(corpus)
    wordcloud.to_file(dir_path)


def freq_word(datos, nlp, direccion):

    """
    función que hace un conteo de palabras
    :param datos: frases a parametrizar
    :return: conteo de palabras
    """

    fdist = datos.frase.tolist()
    suma = reduce(lambda a, x: a + x, fdist)
    doc = nlp(suma)

    word_noun_str, word_adj_str  = "", ""
    word_noun, word_adj = [], []
    for token in doc:
        # me quedo con las keywords, eliminando las demas palabras que perteenecen a todas las frases
        # y dan ruido a la hora de entrenar
        if token.pos_ == "NOUN":
            word_noun.append(token.lemma_)
            word_noun_str += token.lemma_ + " "
        elif token.pos_ == "ADJ":
            word_adj.append(token.lemma_)
            word_adj_str += token.lemma_ + " "

    word_noun_top = []
    word_adj_top = []
    word_noun = FreqDist(word_noun)

    #obtengo los nombres
    for word, frequency in word_noun.most_common(20):
        dic = {}
        dic["nombre"] = word
        dic["frecuencia"] = frequency
        word_noun_top.append(dic)

    word_adj = FreqDist(word_adj)
    # obtengo los adjetivos
    for word, frequency in word_adj.most_common(20):
        dic = {}
        dic["nombre"] = word
        dic["frecuencia"] = frequency
        word_adj_top.append(dic)

    name = direccion + "noun"
    word_cloud(word_noun_str, name)
    name = direccion + "adj"
    word_cloud(word_noun_str, name)
    return (word_noun_top, word_adj_top)
