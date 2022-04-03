### Stemming

From Stemming we will process of getting the root form of a word. Root or Stem is the part to which inflextional affixes(like -ed, -ize, etc) are added. We would create the stem words by removing the prefix of suffix of a word. So, stemming a word may not result in actual words.

For Example: Mangoes ---> Mango

             Boys ---> Boy
             
             going ---> go
             
             
If our sentences are not in tokens, then we need to convert it into tokens. After we converted strings of text into tokens, then we can convert those word tokens into their root form. These are the Porter stemmer, the snowball stemmer, and the Lancaster Stemmer. We usually use Porter stemmer among them.
