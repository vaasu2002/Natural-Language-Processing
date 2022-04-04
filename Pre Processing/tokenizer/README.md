# tokenizer

```ruby
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')

sentence = 'Tokenizers divide strings into lists of substrings. For example, tokenizers can be used to find the words and punctuation in a string.This particular tokenizer requires the Punkt sentence tokenization models to be installed. NLTK also provides a simpler, regular-expression based tokenizer, which splits text on whitespace and punctuation.'

sent = sent_tokenize(sentence)

for i in sent:
  print(word_tokenize(i))
  

[word_tokenize(t) for t in sent_tokenize(sentence)]

```
**LINK** -> https://www.nltk.org/api/nltk.tokenize.html
