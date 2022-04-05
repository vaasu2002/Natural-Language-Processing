import spacy
nlp = spacy.load('en_core_web_sm')

sent1 = 'I have a Ph.D in A.I'
sent2 = "We're here to help! mail us at nks@gmail.com"
sent3 = 'A 5km ride cost $10.50'

doc1 = nlp(sent1)
doc2 = nlp(sent2)
doc3 = nlp(sent3)

for token in doc1:
    print(token)
    
for token in doc2:
    print(token)
    
for token in doc3:
    print(token)
