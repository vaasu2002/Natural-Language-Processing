# Natural Language Processing

#### **Course:-** [DeepLearning.AI Natural Language Processing Tensorflow](https://github.com/vaasu2002/Tensorflow/tree/main/TensorFlow%20Developer%20Certificate/Natural%20Language%20Processing%20in%20TensorFlow)


| **BOOK** | **Completion** | 
| ----- | -----|
| 1. [**LSTM With Python**](https://drive.google.com/file/d/16zxePmb3TWIxIevh2gkeaTbO-ZEVRuKi/view?usp=sharing) | No |

--------------------------------------------------------------


| **Certification** | **Platform** | 
| ----- | -----|
| 1. [**DeepLearning.AI Natural Language Processing Tensorflow**](https://www.coursera.org/account/accomplishments/certificate/RXGKSDTK9VCW) | [**DeepLearning.ai**](https://www.deeplearning.ai/) |
| 2. [**Natural Language Processing with Classification and Vector Spaces**]() | [**DeepLearning.ai**](https://www.deeplearning.ai/) |





Our text data consits of questions and corresponding labels.

You can think of a question vector as a distributed representation of a question, and is computed for every question in the training set. The question vector along with the output label is then used to train the statistical classification model. 

The intuition is that the question vector captures the semantics of the question and, as a result, can be effectively used for classification. 

To obtain question vectors, we have two alternatives that have been used for several text classification problems in NLP: 
* word-based representations and 
* context-based representations

### Context-based Representations

- **Context-based representations** may use language models to generate vectors of sentences. So, instead of learning vectors for individual words in the sentence, they compute a vector for sentences on the whole, by taking into account the order of words and the set of co-occurring words.
- Examples of deep contextualised vectors include:
  - **Embeddings from Language Models (ELMo)**: uses character-based word representations and bidirectional LSTMs. The pre-trained model computes a contextualised vector of 1024 dimensions. ELMo is available on Tensorflow Hub.
  - **Universal Sentence Encoder (USE)**: The encoder uses a Transformer  architecture that uses attention mechanism to incorporate information about the order and the collection of words. The pre-trained model of USE that returns a vector of 512 dimensions is also available on Tensorflow Hub.
  - **Neural-Net Language Model (NNLM)**: The model simultaneously learns representations of words and probability functions for word sequences, allowing it to capture semantics of a sentence. We will use a  pretrained  models available on Tensorflow Hub, that are trained on the English Google News 200B corpus, and computes a vector of 128 dimensions for the larger model and 50 dimensions for the smaller model.


### Word-based Representations

- A **word-based representation** of a question combines word embeddings of the content words in the question. We can use the average of the word embeddings of content words in the question. Average of word embeddings have been used for different NLP tasks.
- Examples of pre-trained embeddings include:
  - **Word2Vec**: These are pre-trained embeddings of words learned from a large text corpora. Word2Vec has been pre-trained on a corpus of news articles with  300 million tokens, resulting in 300-dimensional vectors.
  - **GloVe**: has been pre-trained on a corpus of tweets with 27 billion tokens, resulting in 200-dimensional vectors.


