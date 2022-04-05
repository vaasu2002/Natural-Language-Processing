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

## EMOJI
-   Remove Emoji
```ruby
import re
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
remove_emoji("Loved the movie. It was 😘😘")
remove_emoji("Lmao 😂😂")
```
-   Replace Emoji
```ruby
import emoji
print(emoji.demojize('Python is 🔥'))

print(emoji.demojize('Loved the movie. It was 😘'))
```










