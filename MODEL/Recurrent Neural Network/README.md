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

## RNN model structure

Earlier we said that RNN has the function of "memory" of time, so how does it realize the so-called "memory"?


<center>Figure 1 RNN structure diagram </center>

As shown in Figure 1, we can see that the RNN hierarchy is simpler than CNN.It mainly consists of an input layer , a Hidden Layer , and an output layer .

And you will find that **there is an arrow in the Hidden Layer to  indicate the cyclic update of the data.This is the method to implement the time memory function.**

![alt](https://miro.medium.com/max/1400/1*xn5kA92_J5KLaKcP7BMRLA.gif)

* t — time step
* X — input
* h — hidden state
* length of X — size/dimension of input
* length of h — no. of hidden units.


<center>Figure 2 Unfolded RNN Diagram </center>

Figure 2 shows the hierarchical expansion of the Hidden Layer where

**T-1, t, t + 1 represent the time series**

**X represents the input sample**

**St represents the memory of the sample at time t, St = f (W * St -1 + U * Xt).** 

**W is the weight of the input**

**U is the weight of the input sample at the moment**

**V is the weight of the output sample.**


### Feedforward

At t = 1, the general initialization input S0 = 0, randomly initializes W, U, V, and calculates the following formula:



Among them, f and g are activation functions. Among them, f can be tanh, relu, sigmoid and other activation functions, g is usually softmax or other.

Time advances, and the state s1 at this time, as the memory state at time 1, will participate in the prediction activity at the next time, that is:



By analogy, you can get the final output value:




Note : 

1. Here W, U, V are equal at each moment ( weight sharing ).

2. The hidden state can be understood as: S = f (existing input + past memory summary )


## Back propagation through TIME of RNN

Earlier we introduced the forward propagation method of RNN, so how are the weight parameters W, U, and V of the RNN updated?

Each output will have a value Ot error value , Et the total error may be expressed as

 The loss function can use either the cross-entropy loss function or the squared error loss function .

Because the output of each step does not only depend on the network of the current step, but also the state of the previous steps, then this modified BP algorithm is called Backpropagation Through Time ( BPTT ), which is the reverse transfer of the error value at the output end. The gradient descent method is updated. 

That is, the gradient of the parameter is required:


 First we solve the update method of W. From the previous update of W, it can be seen that it is the sum of the partial derivatives of the deviations at each moment. 

Here we take time t = 3 as an example.According to the chain derivation rule, we can get the partial derivative at time t = 3 as:




At this time, according to the formula, ![alt](img/331.png) we will find that in addition to W, S3 is also related to S2 at the previous moment.

![alt](https://miro.medium.com/max/1400/0*ENwCVS8XI8cjCy55.jpg)


### Going little deeper

Let’s focus on one error term et.

You’ve calculated the cost function et, and now you want to propagate your cost function back through the network because you need to update the weights.

Essentially, every single neuron that participated in the calculation of the output, associated with this cost function, should have its weight updated in order to minimize that error. And the thing with RNNs is that it’s not just the neurons directly below this output layer that contributed but all of the neurons far back in time. So, you have to propagate all the way back through time to these neurons.

The problem relates to updating wrec (weight recurring) – the weight that is used to connect the hidden layers to themselves in the unrolled temporal loop.

For instance, to get from xt-3 to xt-2 we multiply xt-3 by wrec. Then, to get from xt-2 to xt-1 we again multiply xt-2 by wrec. So, we multiply with the same exact weight multiple times, and this is where the problem arises: when you multiply something by a small number, your value decreases very quickly.

As we know, weights are assigned at the start of the neural network with the random values, which are close to zero, and from there the network trains them up. But, when you start with wrec close to zero and multiply xt, xt-1, xt-2, xt-3, … by this value, your gradient becomes less and less with each multiplication.


### Advantages of Recurrent Neural Network

-    RNN can model sequence of data so that each sample can be assumed to be dependent on previous ones
-    Recurrent neural network are even used with convolutional layers to extend the effective pixel neighbourhood.

### Disadvantages of Recurrent Neural Network

-   Gradient vanishing and exploding problems.
-   Training an RNN is a very difficult task.
-   It cannot process very long sequences if using tanh or relu as an activation function.



