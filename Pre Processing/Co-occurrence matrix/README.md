# Co-occurrence matrix

### Generated embedding
**Consider relationship between surrounding the word**


**The co-occurrence matrix is expressed by considering the relationship between words in the corpus.**
 - A very important idea is that we think that the meaning of a word is closely related to the word next to it. This is where we can set a window (the size is generally 5 ~ 10). The size of the window below is 2, so in this window, the words that appear with rests are life, he, in, and peace. Then we use this co-occurrence relationship to generate word vectors.


![alt text](https://github.com/vaasu2002/Natural-Language-Processing/blob/main/Pre%20Processing/Co-occurrence%20matrix/concurrence.jpg)


#### I like deep learning.

#### I like NLP.

#### I enjoy flying.

As an example, **we set the window size to 1**, which means that **we only look at the word immediately surrounding a word**. At this point, you will get a symmetric matrix-co-occurrence matrix. Because in our corpus, **the number of times I and like appear as neighbors in the window at the same time is 2**, the value where I and like intersect in the table below is 2. 

In this way, the idea of turning words into vectors is done. Each row (or each column) of the co-occurrence matrix is a vector representation of the corresponding word.

![alt text](https://github.com/vaasu2002/Natural-Language-Processing/blob/main/Pre%20Processing/Co-occurrence%20matrix/concur.jpg)

>Although the Cocurrence matrix solves the relative position between words to some extent, this problem should be paid attention to. But it still faces dimensional disaster. 

>In other words, the vector representation of a word is too long. At this time, it is natural to think of some common dimensionality reduction methods such as SVD or PCA.

>The selection of the window size is the same as determining n in the n-gram. The size of the matrix will also increase when the window is enlarged, so it still has a large amount of calculation in nature, and the SVD algorithm has a large amount of calculation. If the text set is very More, it is not operable.
