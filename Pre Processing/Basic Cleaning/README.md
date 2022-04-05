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
