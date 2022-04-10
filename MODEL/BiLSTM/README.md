# BiLSTM

## What is LSTM and BiLSTM?

LSTM stands for Long short-term memory, which is a type of **RNN(Recurrent neural network)**. Because of its design characteristics, LSTM is too useful for modeling the time series data, such as text data.BiLSTM is the abbreviation of Bi-directional Long Short-Term Memory, which is a combination of forward LSTM and backward LSTM. Both are often used to **model contextual information** in natural language processing tasks.


## Why use LSTM and BiLSTM?

Combining the representations of words into the representations of sentences, you can use the addition method, that is, add all the representations of the words, or average them, but these methods do not take into account the order of words in the sentence. Such as the sentence ***"I don't think he is good"***. The word "no" is a negation of the following "good", that is, the emotional polarity of the sentence is derogatory. The LSTM model can better capture the long-distance dependencies. Because LSTM can learn what information to remember and what information to forget through the training process.

But there is still a problem in modeling sentences with LSTM: it is impossible to encode information from back to front.In more fine-grained classification, such as the five classification tasks for strong meaning, weak meaning, neutral, weak derogation, and strong derogation, attention needs to be paid to the interaction between affective words, degree words, and negative words . For example, "This restaurant is too dirty to be good, not as good as next door". Here, "No" is a modification of the degree of "dirty". BiLSTM can better capture the two-way semantic dependency.


The thing involved in Bidirectional Recurrent neural networks(RNN) is preety starightforward.Which involves in making an exact copy of the first recurrent layer in the network then providing the input sequence as it is the input of the first layer and providing the reversed copy of a input sequence to the replicated layer. This get the better of the limitations of the traditional RNN. BRNN(Bidirectional recurrent neural network), which can be trained using all avaiable input information in the past and future of the particular time-step. Split of the state neurons in regular Recurrent neural network(RNN) is responsible for the states(which is in positive time direction) and the part of the backward states(which is in negative time direction).

In speech recognition domain a context of whole utterance is used to explain what is being said rather than the linear interpretation thus the input squence is feeded bi-directionally. To be accurate, time steps in the input sequence are processed one at a time, but the network steps through the sequence in both direction at the same time.

<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fpaperswithcode.com%2Fmethod%2Fbilstm&psig=AOvVaw0qpfSxo5gyLaT-nPYHdPbv&ust=1649666379781000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCODmmqiMifcCFQAAAAAdAAAAABAD">
