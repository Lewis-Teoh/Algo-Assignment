from plistlib import Data
from urllib.request import urlopen

from plotly.graph_objs._figure import Figure

import obo
import plotly
import plotly.plotly as py
import os 
import time
from shutil import copyfile


import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import project

# import plotly.plotly as py
# from plotly.graph_objs import *
# username ='richardho',api_key = 'Ctfxr9YqmVCdoyECqgdT'
def plotgraph(word,frequency):
    img_name = 'my-plot'
    
    py.sign_in('richardho','Ctfxr9YqmVCdoyECqgdT')
    trace1 = {
        "x":word,
        "y":frequency,
        "type":"bar",
        "uid": "b367f710-22d9-11e9-9c93-88e9fe63724a"
    }
    data = Data([trace1])
    layout ={
        "title":"Frequency of word count",
        "yaxis":{"title":"Frequency"}
    }
    fig = Figure(data=data,layout =layout)
    plot_url = py.plot(fig)


def plotlj(word,frequency,name):
    plot([go.Scatter(x=word, y=frequency)], filename=name)

def piepie(labels,frequency,name):
    plot([go.Pie(labels=labels, values=frequency)], filename=name)


def plotpie(inputtype,percentage,image_filename):
    img_name = image_filename
    dload = os.path.expanduser('~/Downloads')
    save_dir = '/tmp'
    labels = inputtype
    value = percentage

    data = [go.Pie(labels = labels,values = value)]
    plotly.offline.plot(data,image_filename= img_name,image = 'png')
    time.sleep(1)
    copyfile('{}/{}.png'.format(dload, img_name),
         '{}/{}.png'.format(save_dir, img_name))

def inspect(text):
    result = obo.check_stopword(text)
    print(result)
    # plotoffline(result[1],result[2],'Stopword')

    text = result[0]
    pdata = obo.pdata(text,obo.positive_word)
    # print(pdata)
    # plotoffline(pdata[0],pdata[1],"Positive word Encountered.")

    ndata = obo.ndata(text,obo.negative_word)
    # print(ndata)
    # plotoffline(ndata[0],ndata[1],"Negative word Encountered.")

    output = obo.countsentiment(text)
    return output
    # sentiment_score = output[2]
    # plotpie(output[0],output[1],"Sentiment assesment")

    # print(obo.countsentiment(text,obo.positive_word,obo.negative_word))

def get_nation(country):
    print("god sia")
    nation = country+".txt"
    text = open(nation, "r")
    text = text.read()
    return inspect(text)


def plotting(text):
    result = obo.checkstopword(text)
    plotoffline(result[1],result[2],'ChinaStop')

    text = result[0]
    pdata = obo.pdata(text, obo.positive_word)
    # print(pdata)
    plotoffline(pdata[0],pdata[1],"ChinaPositive")

    ndata = obo.ndata(text, obo.negative_word)
    # print(ndata)
    plotoffline(ndata[0],ndata[1],"ChinaNegative")

    output = obo.countsentiment(text, obo.positive_word, obo.negative_word)
    plotpie(output[0],output[1],"ChinaSentiment")

    # sentiment_score = output[2]
    # print(obo.countsentiment(text,obo.positive_word,obo.negative_word)

if __name__ == "__main__":

    get_nation("taiwan")
    # china = open("australia.txt","r")    #change the name
    # china = china.read()
    # result = obo.check_stopword(china)
    # freq = obo.pie(result[0])
    # piepie(['Positive Word','Negative Word','Neutral Word'],freq,'C:/Users/lewis/PycharmProjects/AlgoAssignment/graph/PieAustralia')    #change h
    # plotlj(result[1], result[2],'C:/Users/lewis/PycharmProjects/AlgoAssignment/graph/SChina')
    # positivecounting = obo.wordcounter(result[0], obo.positive_dict)
    # plotlj(positivecounting[0], positivecounting[1],'C:/Users/lewis/PycharmProjects/AlgoAssignment/graph/PChina')
    # negativecounting = obo.wordcounter(result[0],obo.negative_dict)
    # plotlj(negativecounting[0],positivecounting[1],'C:/Users/lewis/PycharmProjects/AlgoAssignment/graph/NChina')


