# importing nltk library
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# remove stopwords function 
def rem_stopwords(text): 
    text = rem_punct(text)
    stop_words = set(stopwords.words("english")) 
    word_tokens = word_tokenize(text) 
    filtered_text = [word for word in word_tokens if word not in stop_words] 
    return filtered_text 
  
ex_text = "Data is the new oil. A.I is the last invention"
rem_stopwords(ex_text)

# OUTPUT :- ['Data', 'new', 'oil', '.', 'A.I', 'last', 'invention']







# For Removing numbers 
def remove_num(text): 
    result = re.sub(r'\d+', '', text) 
    return result 



# importing nltk library
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# remove stopwords function 
def rem_stopwords(text): 
    text = rem_punct(text)
    stop_words = set(stopwords.words("english")) 
    word_tokens = word_tokenize(text) 
    filtered_text = [word for word in word_tokens if word not in stop_words] 
    return filtered_text 
  
ex_text = "Data is the new oil. A.I is the last invention"
rem_stopwords(ex_text)


# OUTPUT :- ['Data', 'new', 'oil', 'AI', 'last', 'invention']
