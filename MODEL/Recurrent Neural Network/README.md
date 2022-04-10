# Recurrent Neural Network

## 1)  After CNN, why RNN is there?

The backpropagation algorithm in CNN (convolutional neural network), we know that their output only considers the influence of the previous input and does not consider
the influence of other moments of input, such as simple cats, dogs, handwritten numbers and other single objects.

However, for some related to time, such as the prediction of the next moment of the video, the prediction of the content of the previous and subsequent documents, 
etc., the performance of these algorithms is not satisfactory. Therefore, RNN should be applied and was born.

## 2) What is RNN?

RNN is a special neural network structure, which is proposed based on the view that " human cognition is based on past experience and memory ". It is different from 
DNN and CNN in that it not only considers the input of the previous moment, And it gives the network a 'memory' function of the previous content .

The reason why RNN is called recurrent neural network is that the current output of a sequence is also related to the previous output. The specific manifestation is
that the network memorizes the previous information and applies it to the current output calculation, that is, the nodes between the hidden layers are connected, and 
the input of the hidden layer includes not only the output of the input layer It also includes the output of the hidden layer from the previous moment.

## 3) What are the main application areas of RNN ?

There are many application fields of RNN. It can be said that as long as the problem of chronological order is considered, RNN can be used to solve it. Here are some
common application fields:

    ① Natural Language Processing (NLP) : There are video processing ,  text generation , language model , image processing

    ② Machine translation , machine writing novels

    ③ Speech recognition

    ④ Image description generation

    ⑤ Text similarity calculation

    ⑥ New application areas such as music recommendation , Netease koala product recommendation , Youtube video recommendation, etc.
    
### Different types of RNN

![alt](https://miro.medium.com/max/1400/0*1PKOwfxLIg_64TAO.jpeg)

#### One-to-one:

This also called as Plain/Vaniall Neural networks. It deals with Fixed size of input to Fixed size of Output where they are independent of previous information/output.

Ex: Image classification.


#### One-to-Many:

it deals with fixed size of information as input that gives sequence of data as output.

Ex:Image Captioning takes image as input and outputs a sentence of words.

![alt](https://miro.medium.com/max/1400/0*d9FisCKzVZ29SxUu.png)

#### Many-to-One:

It takes Sequence of information as input and ouputs a fixed size of output.

Ex:sentiment analysis where a given sentence is classified as expressing positive or negative sentiment.


#### Many-to-Many:

It takes a Sequence of information as input and process it recurrently outputs a Sequence of data.

Ex: Machine Translation, where an RNN reads a sentence in English and then outputs a sentence in French.
