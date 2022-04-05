# Cleaning of texy

### Lowercasing
```ruby
df['review'] = df['review'].str.lower()
```

### Removing HTML tags
```ruby
import re
def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)
    
# remove_html_tags(text)    
df['review'] = df['review'].apply(remove_html_tags)
```

### Removing URL
```ruby
import re
def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub(r'', text)
```

### Correct Spelling
```ruby
from textblob import TextBlob
incorrect_text = 'ceertain conditionas duriing seveal ggenerations aree moodified in the saame maner.'
textBlb = TextBlob(incorrect_text)
textBlb.correct().string
```

### Remove Stopwords
```ruby
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')

def remove_stopwords(text):
    new_text = []
    
    for word in text.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    new_text.clear()
    return " ".join(x)


df['review'].apply(remove_stopwords)
```
