from string import punctuation
all_text = ''.join([c for c in reviews if c not in punctuation])
reviews = all_text.split('\n')
print(reviews[2:3])
all_text = ' '.join(reviews)
words = all_text.split()
