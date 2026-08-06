import nltk
from nltk.tokenize import word_tokenize
patterns = [
    (r'.*ing$', 'VBG'),               
    (r'.*ed$', 'VBD'),                    
    (r'.*es$', 'VBZ'),                             
    (r'.*ould$', 'MD'),              
    (r'.*\'s$', 'POS'),                        
    (r'.*s$', 'NNS'),                      
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),                   
    (r'(the|The|a|A|an|An)$', 'DT'),              
    (r'.*able$', 'JJ'),                  
    (r'.*', 'NN')                             
]
regexp_tagger = nltk.RegexpTagger(patterns)

text = "The child is playing with 3 dogs and he would jump over a table."

words = word_tokenize(text)
tagged = regexp_tagger.tag(words)

print("Word\t\tPredicted POS Tag")

print("-" * 35)

for word, tag in tagged:
    print(f"{word:15}{tag}")