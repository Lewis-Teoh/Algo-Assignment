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



import re

def multiple_pattern_hashing_rabin_karp(pattern, d):
    pat = len(pattern)
    pattern_dict = {}
    for i in range(pat):
        p = 0
        word = pattern[i]
        wordsize = len(word)
        for j in range(wordsize):
            p = (d * p + ord(word[j]))
            if j == wordsize-1:
                pattern_dict[p] = word+"end"
            else:
                if p not in pattern_dict:
                    pattern_dict[p] = word[0:j+1]+"not"
    return pattern_dict

#trasforming positive word to a dict for checking
positive = open("positive.txt","r")
positive_word = positive.read().split(',') #list of positive word
positive_dict = multiple_pattern_hashing_rabin_karp(positive_word, 256)

#trasforming negative word to a dict for checking
negative = open ("negative.txt","r")
negative_word = negative.read().split(',') #list of negative word
negative_dict = multiple_pattern_hashing_rabin_karp(negative_word, 256)

#trasforming stop word to a dict for checking
file = open(r"C:\Users\ASUS\PycharmProjects\Algo-Assignment-algorithm\stop word.txt", "r")  # NEED to change directory
stop_word = []
for line in file:
    stopword = re.sub("\s{1,}", "", line)  #because reading the line, so i need to remove whitespace behind
    stop_word.append(stopword)
stop_word_dict = multiple_pattern_hashing_rabin_karp(stop_word, 256)

def multiple_pattern_matching_rabin_karp(text, pattern_dict, d):
    size = len(text)
    match_dict = {}
    t = 0
    i = 0
    while i < size:
        if t in pattern_dict:
            if text[i] == " ":
                current = pattern_dict.get(t)
                c = len(current)
                word = current[0:c-3]
                h = current[c-3:c]
                if h == "end":
                    if word in match_dict:
                        frequency = match_dict.get(word)
                        match_dict[word] = frequency + 1
                    else:
                        match_dict[word] = 1
                t = 0
            elif i == size-1:
                t = (d * t + ord(text[i]))
                current = pattern_dict.get(t)
                c = len(current)
                word = current[0:c - 3]
                h = current[c - 3:c]
                if h == "end":
                    if word in match_dict:
                        frequency = match_dict.get(word)
                        match_dict[word] = frequency + 1
                    else:
                        match_dict[word] = 1
            else:
                t = (d * t + ord(text[i]))
        elif text[i] is " ":
            t = 0
        elif t == 0:
            t = (d * t + ord(text[i]))
        else:
            while i != size:
                if text[i] != " ":
                    i+=1
                else:
                    t=0
                    break
        i += 1
    return match_dict.keys(), match_dict.values()

def remove_stopword(stopword_dict, text, d):
    s = len(text)
    start_index = 0
    match_dict = {}
    t=0
    i=0
    while True:
        s = len(text)
        if start_index >= s or i >= s:
            break;
        if i >= s - 1:
            t = (d * t + ord(text[i]))
            if t in stopword_dict:
                current = stopword_dict.get(t)
                c = len(current)
                word = current[0:c - 3]
                h = current[c - 3:c]
                if h == "end":
                    # if isMatch(text, word, i):
                    if word in match_dict:
                        frequency = match_dict.get(word)
                        match_dict[word] = frequency + 1
                    else:
                        match_dict[word] = 1
                    slice = text[0:start_index - 1]
                    start_index = s
                    text = slice
        elif t in stopword_dict:
            if text[i] == " ":
                current = stopword_dict.get(t)
                c = len(current)
                word = current[0:c - 3]
                h = current[c - 3:c]
                if h == "end":
                    # if isMatch(text, word, i):
                    if word in match_dict:
                        frequency = match_dict.get(word)
                        match_dict[word] = frequency + 1
                    else:
                        match_dict[word] = 1
                    t = 0
                    w = len(word)
                    slice = text[0:start_index] + text[start_index+w+1:s]
                    text = slice
                    i = start_index-1
            else:
                t = (d * t + ord(text[i]))
        elif text[i] is " ":
            t = 0
            start_index = i
        elif t == 0:
            t = (d * t + ord(text[i]))
        else:
            while True:
                if i >= s-1:
                    i = s+1
                    break
                elif text[i] != " ":
                    i+=1
                else:
                    start_index = i+1
                    t = 0
                    break
        i += 1
    return text, match_dict.keys(), match_dict.values()

def wordcounter(text, wordlist): #CALL this method to count word(positive, negative and neutral
    word, frequency = multiple_pattern_matching_rabin_karp(text, wordlist, 256)
    word = list(word)
    frequency = list(frequency)
    return word, frequency

def check_stopword(string):
    string = re.sub("[”!@#$:.,()*&^%{}\[\]?“\"/;<>_+=`~]", " ", string)  # remove all punctuation except -
    string = re.sub("(\s+-)", " ", string)
    string = re.sub("(-\s+)", " ", string)
    string = re.sub("(^-)|(-$)", "", string)
    string = re.sub("\s{1,}", " ", string)  # replace 2 or more whitespace to 1 whitespace
    string = re.sub("^\s|\s$", "", string)
    string = string.lower()  # change the string to lowercase for comparing
    string, s, sf = remove_stopword(stop_word_dict, string, 256)
    s = list(s)
    sf = list(sf)
    return string, s, sf

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

def countsentiment(wordlist):
    positivecounting = wordcounter(wordlist,positive_dict)
    positivefound,positive_freq = positivecounting[0],positivecounting[1]
    ptotal = counttotal(positive_freq)
    negativecounting= wordcounter(wordlist,negative_dict)
    negativefound,negative_freq = negativecounting[0],negativecounting[1]
    ntotal = counttotal(negative_freq)
    total = ptotal+ntotal
    neutral = len(wordlist)-(ptotal+ntotal)
    print("Positive value found:",positivefound)
    print(positive_freq,"Frequency of positive value: ",ptotal)
    print("Negative value found:",negativefound)
    print(negative_freq,"Frequency of negative vlaue: ",ntotal)
    # print("The total word of neutral word count: ",neutral)
    positivesense = (ptotal/total)*100
    negativesense = (ntotal/total)*100*(-1)
    # neutralsense = (neutral/total)*100
    finalscore = positivesense+negativesense
    # print(positivesense,negativesense)
    typelist=['Positive word','Negative word','Neutral word']
    freq = [ptotal,ntotal,neutral,total]
    scorelist = ["POSITIVE SCORE","NEGATIVE SCORE","FINAL SCORE"]
    score = [positivesense,negativesense,finalscore]
    print(score[0],score[1])
    return score[2]
    # return positivesense,negativesense

def pie(wordlist):
    positivecounting = wordcounter(wordlist,positive_dict)
    positivefound,positive_freq = positivecounting[0],positivecounting[1]
    print(positivefound,positive_freq)
    ptotal = counttotal(positive_freq)
    negativecounting= wordcounter(wordlist,negative_dict)
    negativefound,negative_freq = negativecounting[0],negativecounting[1]
    print(negativefound, negative_freq)
    ntotal = counttotal(negative_freq)
    neutral = len(wordlist)-ptotal-ntotal
    return ptotal,ntotal,neutral


def positive(wordlist):
    positivecounting = wordcounter(wordlist, positive_dict)
    positivefound, positive_freq = positivecounting[0], positivecounting[1]
    ptotal = counttotal(positive_freq)
    negativecounting= wordcounter(wordlist,negative_dict)
    negativefound,negative_freq = negativecounting[0],negativecounting[1]
    ntotal = counttotal(negative_freq)
    return ptotal,ntotal,positivefound,positive_freq,negativefound,negative_freq

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
    

    
    
    


