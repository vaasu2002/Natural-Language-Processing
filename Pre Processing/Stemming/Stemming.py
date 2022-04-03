#importing nltk's porter stemmer 
from nltk.stem.porter import PorterStemmer 
from nltk.tokenize import word_tokenize 
stem1 = PorterStemmer() 
  
# stem words in the list of tokenised words 
def s_words(text): 
    word_tokens = word_tokenize(text) 
    stems = [stem1.stem(word) for word in word_tokens] 
    return stems 
  
text = 'Data is the new revolution in the World, in a day one individual would generate terabytes of data.'
s_words(text)
