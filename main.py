import pprint


#directory of words
word_collection  = dict()
english_words = dict()
# populate a list of the english words in a dictionary for faster lookup
def populate_english_words():
    print("populating english words list...")
    with open("words_alpha.txt","r", encoding="utf8") as file:
        for line in file:
            for word in line.split():
                english_words[word] = 1
    print("english word list populated!\n")
    # pprint.pprint(english_words)

def getWords(filename):
    print(f"populating {filename} frequency table...")
    with open(filename,'r', encoding="utf8") as f:
        for line in f:
            for word in line.split():
                if word.lower() in english_words:
                    if word.lower() not in word_collection:
                        word_collection[word.lower()] = 1
                    else:
                        word_collection[word.lower()] += 1
    # pprint.pprint(word_collection)
    # print(word_collection)
    print(f"{filename} frequency table populated!\n")
    # pprint.pprint(word_collection)
    return word_collection

#clean dictionary for repeated words with different punctuation
def cleanWords(wordDict):
    punctuations = "!()-[]{};:',<>./?@#$%^&*_~“”,\‘\’”"
    newDict = dict()
    for word in wordDict:
        cleaned_word = ""
        for char in word:
            if char not in punctuations:
                cleaned_word += char
        # print(f"{word}\t{cleaned_word}")

        if cleaned_word not in newDict:
            newDict[cleaned_word] = 0
        newDict[cleaned_word] += wordDict[word]

    # pprint.pprint(newDict)
    return newDict

def removeCommon(wordsDict):
    with open("commonwords.txt", 'r', encoding='utf8') as file:
        wordsList = {}
        newDict = {}
        for line in file:
            for word in line.split():
                wordsList[word] = True
        for word in wordsDict:
            if word not in wordsList:
                newDict[word] = wordsDict[word]
            else: print(f"{word} is too common. word removed")
        print("---"*20)
        print(f"A total of {len(wordsDict) - len(newDict)} words were removed for being too common.")
        print(f"A total of {len(newDict)} words were kept")
        # pprint.pprint(newDict)
        return(newDict)


"""
The idea behind the way we rank the words is by least to most
frequent, and seccondly alphabetically. we are to achieve this 
by appending a word's frequency to at the beginning of each 
word, throwing such words in a list, then sorting such list. 

however the problem with this is that 13 < 2 in the eyes of a 
array sort since it sorts by individual characters not numerical
total value. 
"""
def populate_ranked_list(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append(str(dictionary[key])+key)
    print(f"list of words to be sorted by frequency. size: {len(sorted_list)}")
    print("sorting.... this muight take a while..")
    sorted_list.sort()
    print("Done sorting the list!")
    pprint.pprint(sorted_list)


if __name__ == '__main__':
    populate_english_words()
    newDict = getWords("page1-55.txt")
    nn = removeCommon(newDict)
    populate_ranked_list(nn)
