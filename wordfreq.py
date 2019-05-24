from urllib.request import urlopen
import obo 
import plotly
import plotly.plotly as py
import plotly.graph_objs as go 
import os 
import time
from shutil import copyfile
import project




def worddict(string):
    wordlist = string.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
    result = dict(set(zip(wordlist,wordfreq)))
    return result
    # for key in result:
    #     print(key)

# def wordlistotfrewdict(wordlist):
#     wordfreq = 
    
def sortdict(freqdict):
    aux = [[freqdict[key],key] for key in freqdict]
    print(type(aux)) #list
    return aux


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

def plotoffline(word,frequency,image_filename):
    img_name = image_filename
    dload = os.path.expanduser('~/Downloads')
    save_dir = '/tmp'

    data = [go.Bar(x = word, y = frequency)]
    plotly.offline.plot(data,image_filename= img_name,image = 'png')
    time.sleep(1)
    copyfile('{}/{}.png'.format(dload, img_name),
         '{}/{}.png'.format(save_dir, img_name))

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
    result = obo.checkstopword(text)
    # plotoffline(result[1],result[2],'Stopword')

    text = result[0]
    

    pdata = obo.pdata(text,obo.positive_word)
    print(pdata)
    # plotoffline(pdata[0],pdata[1],"Positive word Encountered.")

    ndata = obo.ndata(text,obo.negative_word)
    print(ndata)
    # plotoffline(ndata[0],ndata[1],"Negative word Encountered.")

    output = obo.countsentiment(text,obo.positive_word,obo.negative_word)
    print(output)
    sentiment_score = output[3]
    # plotpie(output[0],output[1],"Sentiment assesment")

    # print(obo.countsentiment(text,obo.positive_word,obo.negative_word))
 


if __name__=="__main__":

    text = "Had you any occasion to be in this part of the town, on the 6th of June in the evening? - I dined with my brother who lives opposite Mr. Akerman's house. They attacked Mr. Akerman's house precisely at seven o'clock; they were preceded by a man better dressed than the rest,\
         who went up to Mr. Akerman's door; he rapped three times, and I believe pulled the bell as often. Mr. Akerman had barrocadoed his house. When the man found that no one came, he went down the steps, made his obeisance to the mob, and pointed to the door, and then retired."


    indonesia = open("indonesia.txt","r")
    indonesia = indonesia.readlines()
    # inspect(indonesia)

    singapore = open("singapore.txt","r")
    singapore = singapore.readlines()
    # inspect(singapore)

    australia = open("australia.txt","r",)
    australia = australia.readlines()
    # inspect(australia)


    hongkong = open("hongkong.txt","r",)
    hongkong = hongkong.read()
    # inspect(hongkong)

    china = open("china.txt","r")
    china = china.read()
    inspect(china)
    

    # result = obo.checkstopword(text)
    # # plotoffline(result[1],result[2],'Stopword')

    # text = result[0]
    # test = obo.wordcounter(text,obo.positive_word)
    # print(test)

    # pdata = obo.pdata(text,obo.positive_word)
    # print(pdata)
    # # plotoffline(pdata[0],pdata[1],"Positive word Encountered.")

    # ndata = obo.ndata(text,obo.negative_word)
    # print(ndata)
    # # plotoffline(ndata[0],ndata[1],"Negative word Encountered.")

    # output = obo.countsentiment(text,obo.positive_word,obo.negative_word)
    # print(output)
    # sentiment_score = output[3]
    # plotpie(output[0],output[1],"Sentiment assesment")
    # print(obo.countsentiment(text,obo.positive_word,obo.negative_word))


    # for s in sorteddict:
        # print(str(s))
    
    # print(wordlist)
    # print(obo.countsentiment(wordlist,obo.positive_word,obo.negative_word))
    
    # temp = ['helloattack','lives','door','well','more','believe']
    # print(obo.countsentiment(temp,obo.positive_word,obo.negative_word))
    # string = ' '.join(wordlist)
    # # print(string,type(string))
    # print(project.wordcounter(string,obo.positive_word))

    # print()

    # print(type(sorteddict),len(sorteddict))
    # print(stopfound)
    # word,wordfreq  = obo.countword(wordlist)
    # counting = obo.countword(wordlist,obo.positive_word)
    # positivefound,positive_freq = counting[0],counting[1]
    # ptotal = counttotal(positive_freq)
    # negativecounting= obo.countword(wordlist,obo.negative_word)
    # negativefound,negative_freq = negativecounting[0],negativecounting[1]
    # ntotal = counttotal(negative_freq)
    # print(obo.negative_word)
  
    # print("Positive value found:",positivefound)
    # print(positive_freq,"Frequency of positive value: ",ptotal)
    # print("Negative value found:",negativefound)
    # print(negative_freq,"Frequency of negative vlaue: ",ntotal)
    # positive = open("positive.txt","r")
    # positive_word = positive.read().split(',') #list of positive word
    # negative = open ("negative.txt","r")
    # negative_word = negative.read().split(',')
    


    # plotgraph(word,wordfreq)
    # new_positive  = obo.processpositive(obo.positive)
    # new_negative = obo.processnegative(obo.negative)
    # plotoffline(word,wordfreq,'stopwordfound?')
    # a = "-what"
    # a = a.replace("-",',')
    # print(new_negative)
    # print(new_positive)
