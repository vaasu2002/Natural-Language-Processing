# forms dictionary
from collections import Counter
counts = Counter(words)
counts

#display vocabulary(unique words in alphabetical order)
sorted(counts)


from collections import Counter
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab

for i, word in enumerate(vocab, 1):
    print(i , word)
    
    
from collections import Counter
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)

# Create your dictionary that maps vocab words to integers here
vocab_to_int = {word: i for i, word in enumerate(vocab, 1)} # start from 1

# Convert the reviews to integers, same shape as reviews list, but with integers
review_ints = [] # stores review in number form(as each word has its won number)
for each in reviews:
    review_ints.append([vocab_to_int[word] for word in each.split()])

vocab_to_int = {word: i for i, word in enumerate(vocab, 1)}
vocab_to_int
 
review_lens = Counter([len(x) for x in review_ints]) # length of each review


print("Zero-length reviews: {}".format(min(review_lens)))
print("Maximum review length: {}".format(max(review_lens)))

review_ints = [review for review in review_ints if (len(review) > 0)] # filter out review with zero length

# forming dataset(padding)
seq_len = 200
features = []
for review in review_ints:
    review_len = len(review)
    len_diff = seq_len - review_len
    if len_diff <= 0:
        features.append(review[:seq_len])
        print(review[:seq_len])
    else:
        padding = [0] * len_diff
        padded_feature = padding + review
        features.append(padded_feature)
print()
features = np.asarray(features)


features.shape # 2d (number of review, length of each review(fixed after padding(200 in this case)


# splitting dataset
split_frac = 0.8
split_idx = int(len(features) * split_frac)

train_x, val_x = features[:split_idx], features[split_idx:]
train_y, val_y = labels[:split_idx], labels[:split_idx]

test_idx = int(len(val_x) * 0.5)
val_x, test_x = val_x[:test_idx], val_x[test_idx:]
val_y, test_y = val_y[:test_idx], val_y[test_idx:]

print("\t\t\tFeature Shapes:")
print("Train set: \t\t{}".format(train_x.shape), 
      "\nValidation set: \t{}".format(val_x.shape),
      "\nTest set: \t\t{}".format(test_x.shape))


train_x.shape #2d
train_y.shape #1d
# we need train_x as 3d tensor and train_y a 2d tensor

train_x = np.array(train_x).reshape((train_x.shape[0], train_x.shape[1], 1)) # make 3d
train_y = to_categorical(train_y) # make 2d (numebr of labels ,  number of categories)


# model
def vanilla_rnn():
    model = Sequential()
    model.add(SimpleRNN(50, input_shape = (200,1), return_sequences = True))
    model.add(SimpleRNN(50,return_sequences = True)) 
    model.add(SimpleRNN(50))
    model.add(Dense(46))
    model.add(Dense(46))
    model.add(Dense(46))
    model.add(Activation('sigmoid'))
    
    adam = tf.optimizers.Adam(learning_rate=0.001)
    model.compile(loss = 'sparse_categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
    
    return model

model = KerasClassifier(build_fn = vanilla_rnn, epochs = 1, batch_size = 50, verbose = 1)

model.fit(train_x, train_y)

