
phrase = "Bonjour tout le monde".split(' ')

def comptWordsPhrase(phrase):
    d = {}
    for word in phrase: 
        d[word] = len(word)
    
    return d
    
    print( comptWordsPhrase(phrase) )


print( dict([ (w, len(w)) for w in phrase ]))