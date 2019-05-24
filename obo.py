# obo.py
from urllib.request import urlopen
import obo 
import plotly
import plotly.plotly as py
import plotly.graph_objs as go 
import os 
import time
from shutil import copyfile
import re




positive = open("positive.txt","r")
positive_word = positive.read().split(',') #list of positive word
negative = open ("negative.txt","r")
negative_word = negative.read().split(',') #list of negative word


def search(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    result = []
    if n == 0 or m > n:
        return result

    for i in range(m):  # preprocessing
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for s in range(n - m + 1):  # note the +1
        if p == t:  # check character by character
            match = True
            for i in range(m):
                if pattern[i] != text[s + i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n - m:
            t = (t - h * ord(text[s])) % q  # remove letter s
            t = (t * d + ord(text[s + m])) % q  # add letter s+m
            t = (t + q) % q  # make sure that t >= 0
    return result


def removeDash(text, list):
    s = 1
    t = len(text)
    sum = 0
    for i in range(len(list)):
        current_index = int(list[i])
        if current_index == 0:
            if text[current_index+s] == " ":
                slice = text[s+1:t]
                text = slice
                sum+=1
        elif current_index + s == len(text):
            if text[current_index-1] == " ":
                slice = text[0:current_index-1]
                text = slice
                sum+=1
        else:
            if text[current_index-1] == " " and text[current_index+s] == " ":
                slice = text[0:current_index-1] + text[current_index+s:t]
                text = slice
                sum+=1
    return text


def removeStopWord(stopword, text, list, frequency, stop_word):
    s = len(stopword)
    t = len(text)
    sum = 0
    for i in range(len(list)):
        current_index = int(list[i])
        if current_index == 0:
            if text[current_index+s] == " ":
                slice = text[s+1:t]
                text = slice
                sum+=1
        elif current_index + s == t:
            if text[current_index-1] == " ":
                slice = text[0:current_index-1]
                text = slice
                sum+=1
        else:
            if text[current_index-1] == " " and text[current_index+s] == " ":
                slice = text[0:current_index-1] + text[current_index+s:t]
                text = slice
                sum+=1
    if sum != 0:
        frequency.append(sum)
        stop_word.append(stopword)
    return text

def checkstopword(string):
    string = re.sub("[”!@#$:.,()*&^%{}\[\]?“\"/;<>_+=`~]", " ", string)  # remove all punctuation except -
    string = re.sub("(\s+-)", " ", string)
    string = re.sub("(-\s+)", " ", string)
    string = re.sub("(^-)|(-$)", "", string)
    dashList = search(string, "-", 256, 999937)  # use back search method to search for dash in string
    string = removeDash(string, dashList)  #additional remove dash method
    string = re.sub("\s{1,}", " ", string)  #replace 2 or more whitespace to 1 whitespace
    string = string.lower()  # change the string to lowercase for comparing
    file = open(r"stop word.txt", "r")  #NEED to change directory
    stop_word = []
    frequency = []
    for line in file:
        stopword = re.sub("\s{1,}", "", line)  #because reading the line, so i need to remove whitespace behind
        result = search(string, stopword, 256, 999937)  #search for the word and return list
        result.reverse()  #because removing word will cause the word index to change, so i remove the word at behind first to avoidremoving wrong word
        string = removeStopWord(stopword, string, result, frequency, stop_word)  #remove stopword
    return string, stop_word, frequency


def wordcount(word, text, list, word_list, frequency):
    s = len(word)
    t = len(text)
    sum = 0
    for i in range(len(list)):
        current_index = int(list[i])
        if current_index == 0:
            if text[current_index+s] == " ":
                sum+=1
        elif current_index + s == t:
            if text[current_index-1] == " ":
                sum+=1
        else:
            if text[current_index-1] == " " and text[current_index+s] == " ":
                sum+=1
    if sum != 0:
        frequency.append(sum)
        word_list.append(word)
    return text

def wordcounter(text, wordlist): #CALL this method to count word(positive, negative and neutral
    word = []
    frequency = []
    for i in range(len(wordlist)):
        result = search(text, wordlist[i], 256, 999937)
        wordcount(wordlist[i], text, result, word, frequency)
    return word, frequency


# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def stripNonAlphaNum(text):
    import re
    text = text.lower()
    text=re.compile(r'\W+', re.UNICODE).split(text)
    for items in text:
        if items == 's' or items == '':
            text.remove(items)

    return text


def sortdict(freqdict):
    aux = [[freqdict[key],key] for key in freqdict]
    aux.sort()
    # print(aux) #list
    return aux
    
def worddict(string):
    # wordlist = string.split()
    wordfreq = []
    for w in string:
        wordfreq.append(string.count(w))
    result = dict(set(zip(string,wordfreq)))
    return result

def removeStopword(wordlist, stopwords):
    # stopwordmet = []
    return [w for w in wordlist if w not in stopwords]
 
def countword(wordfile,wordlist):
    element = []
    count = []
    for w in wordfile:
        if w in wordlist:
            element.append(w)
            total = wordfile.count(w)
            count.append(total)
    return element ,count

def counttotal(listword):
    number = 0
    for item in listword:
        temp = int(item)
        number += temp
    return number


def pdata(text,positive_list):
    result = wordcounter(text,positive_word)    
    return result

def ndata(text,positive_list):
    result = wordcounter(text,negative_word)    
    return result

# est = project.wordcounter(text,obo.positive_word)

def countsentiment(wordlist,positive_list,negative_list):
    
    positivecounting = wordcounter(wordlist,positive_list)
    positivefound,positive_freq = positivecounting[0],positivecounting[1]
    ptotal = counttotal(positive_freq)
    negativecounting= wordcounter(wordlist,negative_list)
    negativefound,negative_freq = negativecounting[0],negativecounting[1]
    ntotal = counttotal(negative_freq)
    total = ptotal+ntotal
    neutral = len(wordlist)-(ptotal+ntotal)
    print("Positive value found:",positivefound)
    print(positive_freq,"Frequency of positive value: ",ptotal)
    print("Negative value found:",negativefound)
    print(negative_freq,"Frequency of negative vlaue: ",ntotal)
    print("The total word of neutral word count: ",neutral)
    positivesense = (ptotal/total)*100
    negativesense = (ntotal/total)*100*(-1)
    # neutralsense = (neutral/total)*100
    finalscore = positivesense+negativesense
    print(positivesense,negativesense)
    typelist=['Positive word','Negative word','Neutral word']
    freq = [ptotal,ntotal,neutral,total]
    scorelist = ["POSITIVE SCORE","NEGATIVE SCORE","FINAL SCORE"]
    score = [positivesense,negativesense,finalscore]
    
    return typelist,freq,scorelist,score

def processpositive(positive):
    sentence = positive.replace(' ','')
    sentence = ''.join(sentence.split())
    sentence = sentence.replace('–', ',').lower()
    sentence = sentence.lower().split(',')
    return sentence

def processnegative(negative):
    sentence = negative.replace(' ','')
    sentence = ''.join(sentence.split())
    sentence = sentence.lower().split(',')
    return sentence 

if __name__ == "__main__":
    a = 34.56
    b = 34
    print(type(a))
    print(type(b))
    print(a+b, type(a+b))
    

    
    
    


