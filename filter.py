from nltk.stem.porter import *
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser

def filter(sentence):
    '''
    The filter() takes an email sentence and returns if the sentence indicates:
    - 'Student has shared' or
    - 'Student wants to know if can share'
    Input:
        sentence (str): 
    Output:
        notify (str): 'Student has shared'
        request (str): 'Student wants to know if can share'

        notify (str)
        request (str)
        exception (str)
        error (str)
    '''

    # sentence = input("Input an email sentence: ")
    
    stem = 'share'
    word = 'email'
    notify = 'Student has shared'
    request = 'Student wants to know if can share'
    exceptionInput = 'Student might share email'
    error = 'Match Error: This sentence does not have the required stem and word.'

    # check that the sentence input has stem and word
    stemSet = set(['sharing', 'shared', 'share'])
    stemmer = PorterStemmer()
    dictionary = defaultdict(set)

    for w in stemSet:
        dictionary[stemmer.stem(w)].add(w)  
        
    stem = dictionary[stem]
    condition = word in sentence
   #  condition2 = type(sentence) == str()
    
    # Check for question match and if sentence involves a past tense
    if all(condition for w in stem):
        
        # NLP chunking
        text = sentence.split()
        if len(text) == 1:
            print(error)
        elif len(text) == 2:
            for t in text:
                for s in stem:
                    if s != t:
                        print(error)
                        break
                break
            
            #print(error)
        else:
            tokensTag = pos_tag(text)
            patterns = '''mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}'''
            chunker = RegexpParser(patterns)
            sentenceTree = chunker.parse(tokensTag)

            leavesDump = []
            for list in sentenceTree.leaves():
                for item in list:
                    leavesDump.append(item)
        
            for leaves in leavesDump:
                
                # check is student shared email
                if 'VBD' in leavesDump and 'VBZ' and 'TO' not in leavesDump:
                    print(notify)
                    break
                # check if student requests permissin to share
                elif ('MD' and 'VB' in leavesDump) or ('VBZ' and 'VBD' in leavesDump) or ('NNP' in leavesDump):
                    print(request)
                    break
                # catch other edge cases
                elif leavesDump.count('NN') >= 2  and 'VBD' not in leavesDump or leavesDump.index('PRP') < leavesDump.index('MD') and 'MD' not in leavesDump or (leavesDump.index('PRP$') > leavesDump.index('MD')):
                    print(exceptionInput)
                    break
    else:
        print(error)
 
filter('may i share your email')