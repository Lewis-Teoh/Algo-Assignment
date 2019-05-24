import re

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

# def main():
#     str = '[<p>PUTRAJAYA: Federal Territories Minister Khalid Samad is positive grouses expressed by traders and visitors of the Jalan Raja Ramadan Baazar will be resolved soon.</p>, <p>He said, on the issue of poor ventilation, talks were held with Kuala Lumpur Mayor Datuk Nor Hisham Ahmad Dahlan to propose for air conditioning at the bazaar.</p>, <p>"Currently, the bazaar is located in a closed (tented) area and it is quite warm inside. I have spoken to the mayor to emulate the Putrajaya Festival Bazaar here, where' \
#                  ' Putrajaya Corporation (PPj) has equipped the tents with air conditioning for the comfort of traders and' \
#                  ' people.</p>, <p>“Kuala Lumpur City Hall should consider air conditioning, if not, at the very least,' \
#                  ' improve ventilation,” he told reporters after attending a buka puasa event hosted by PPj.</p>,' \
#                  ' <p style=\'display: inline; color: rgb(179, 179, 179); font-size: 10px; background-color: transparent;' \
#                  ' font-family: "Open Sans";\'>ADVERTISEMENT</p>, <p>On the flash floods that hit the Ramadan bazaar in Jalan' \
#                  ' Raja, he said City Hall has cleared the drains in the area.</p>, <p>“Due to some construction work carried' \
#                  ' out in the area, the drainage routes were clogged, but City Hall has cleared it now,” he said.</p>, <p>Most' \
#                  ' traders, said Khalid, have said that it would have been a lot worse if they had been in Lorong Tuanku Abdul' \
#                  ' Rahman, where there were no roofs over their heads and their goods would probably get wet.</p>, <p>It was' \
#                  ' reported that heavy rain yesterday in Kuala Lumpur had resulted in flooding, with some stalls inundated' \
#                  ' in ankle-deep water.</p>, <p>On a separate matter, Khalid said the ministry has instructed property developer' \
#                  ' SP Setia Bhd to submit development plans for Federal Hill.</p>, <p>This was following recent claims by residents' \
#                  ' that SP Setia is encroaching onto their residential area even though the company does not own the land on Jalan' \
#                  ' Abdullah.</p>, <p>SP Setia is involved in a major mixed-use development on Federal Hill, which is next to Jalan' \
#                  ' Abdullah.</p>, <p>He said the Federal Hill land was given to SP Setia after it had built a health facility for' \
#                  ' the government.</p>, <p>“The land in Federal Hill next to Bangsar was given in a land swap deal when SP Setia' \
#                  ' built a health facility in Setia Alam, Shah Alam.</p>, <p>“We will honour the agreement made by the Health' \
#                  ' Ministry with them,” he added.</p>]'
#     index = str.index("<p")
#     start = -1
#     end = -1
#     p = True
#     endP = False
#     other = True
#     finalString = ""
#     while p is True or endP is True or other is True:
#         try:
#             print(index,  str[index+1:len(str)])
#             if p is True:
#                 nextClose = str.index(">", index)
#                 start = nextClose
#                 p = False
#                 index = str.index("<", nextClose+1)
#                 if str[index+1] == "/" and str[index+2] == "p":
#                     end = index
#                     endP = True
#                     other = False
#                 else:
#                     endP = False
#             if endP is True:
#                 finalString += str[start+1:end]
#                 if str[index+3] == ">" and str[index+4] == "]":
#                     break
#                 else:
#                     index = str.index("<p", index+3)
#                     p = True
#                     other = False
#             else:
#                 finalString += str[start+1:index]
#                 if str[index+1] == "b":
#                     start = index+4
#                     index = str.index("<", index+4)
#                     if str[index+1] == "/" and str[index+2] == "p":
#                         end = index
#                         endP = True
#                         other = False
#                 # elif str[index+1, index+2] == "/a":
#                 #     finalString += str[start, index]
#                 #     index = str.index("<", nextClose+1)
#                 #     if str[index+1, index+2] == "/p":
#                 #         end = index
#                 #         endP = True
#                 #         other = False
#                 # elif str[index+1] == "a":
#                 #     finalString += str[start, index]
#                 #     other = True
#                 #     nextClose = str.index(">", index)
#                 #     start = nextClose
#                 #     index = str.index("<", nextClose+1)
#                 # elif str[index+1, index+2] == "/s":
#                 #     finalString += str[start, index]
#                 #     index = str.index("<", nextClose+1)
#                 #     if str[index+1, index+2] == "/p":
#                 #         end = index
#                 #         endP = True
#                 #         other = False
#                 # elif str[index+1] == "s":
#                 #     finalString += str[start, index]
#                 #     other = True
#                 #     nextClose = str.index(">", index)
#                 #     start = nextClose
#                 #     index = str.index("<", nextClose+1)
#                 elif str[index+1] == "s" or str[index+1] == "a":
#                     # finalString += str[start, index]
#                     nextClose = str.index(">", index)
#                     start = nextClose
#                     index = str.index("<", nextClose+1)
#                 elif str[index+2] == "s" or str[index+2] == "a":
#                     # finalString += str[start, index]
#                     nextClose = str.index(">", index)
#                     start = nextClose
#                     index = str.index("<", nextClose)
#                 if str[index+1] == "/" and str[index+2] == "p":
#                     end = index
#                     endP = True
#                     other = False
#                 else:
#                     other = True
#         except ValueError:
#             print()
#     string, stop_word, frequency = checkstopword(finalString)  #method to check and remove stop words
#     print(string)
#     print(stop_word)
#     print(frequency)
#     p, pf = wordcounter(s, wordlist)  #method to run positive and negative word



# if __name__ == '__main__':
#         main()