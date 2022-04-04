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
