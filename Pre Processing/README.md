# NLP PRE PROCESSING

**Read Text File**
```ruby
with open('/content/drive/MyDrive/NLP/text.txt', 'r') as f:
    text = f.read()
```
-----------------------------------------------------------------------------------------------
**Read CVS data**
```ruby
# IMPORT LIBRARIES
from string import punctuation
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

# BASIC PRE PROCESSING
def basic_PreProcessing(sentence):
    removed_punctuation = all_text = ''.join([c for c in sentence if c not in punctuation]) # text is string
    lower = removed_punctuation.lower()
    words = lower.split()
    stop_words = set(stopwords.words("english"))  
    remove_stopwords = [word for word in words if word not in stop_words]

    sentence = " ".join(remove_stopwords)
    return sentence

# READ ROWS AND PRE PROCESSING
def parse_data_from_file(filename):
    sentences = []
    labels = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            # each row is a list with 3 elements(same as number of columns)
            labels.append(row[2])
            sentence = row[1] # string
            sentence = basic_PreProcessing(sentence)
            sentences.append(sentence)

    return sentences, labels
    
sentences, labels = parse_data_from_file("/kaggle/input/learn-ai-bbc/BBC News Train.csv")    
```
