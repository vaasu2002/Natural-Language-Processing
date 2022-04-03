# Stop Words
 A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query. 
We would not want these words to take up space in our database, or taking up valuable processing time.

```ruby
nltk.download("stopwords")
nltk.download("punkt")
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
```
