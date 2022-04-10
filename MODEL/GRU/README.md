# GRU(Gated Recurrent Unit) Network

With the widespread application of LSTMs in natural language processing, especially text classification tasks, people have gradually discovered that <span style="color: red">LSTMs have</span> the disadvantages of <span style="color: red">long training time, many parameters, and complex internal calculations</span>. Cho et al. In 2014 further proposed a simpler GRU model that combines the unit state and hidden layer state of the LSTM with some other changes. The forget gate and the input gate are combined into a single update gate . It also mixes cell states and hidden states . The GRU replaces the forget gates and inputs in the LSTM with update gates. Merging the cell state and the hidden state ht, the method of calculating new information at the current moment is different from that of LSTM.

The GRU model is a model that maintains the LSTM effect, has a simpler structure, fewer parameters, and better convergence. The GRU model consists of an update gate and a reset gate.

## Update and reset gates

<span style="color: red">A moment before the output of the hidden layer of the current degree of influence on the hidden layer by updating door control, update value the greater the greater the impact of the door hidden layer output current before a timing of the hidden layer;</span>

<span style="color: red">The extent to which the hidden layer information at the previous moment is ignored is controlled by the reset gate . The smaller the value of the reset gate, the more it is ignored. GRU structure is more streamlined.</span>

One of the reasons for using LSTM is to solve the problem that the Gradient errors of the RNN Deep Network accumulate too much, so that Gradient returns to zero or becomes infinity, so the optimization cannot be continued. The construction of the GRU is simpler: it has one less gate than the LSTM, so there are fewer matrix multiplications. GRU can save a lot of time when the training data is large. GRU, which simplifies the calculation method (simplifies the calculation), and also avoids the disappearance of the gradient to optimize the LSTM.

##  GRU model

Unlike LSTM, GRU has only two gates, namely update gate and reset gate , namely $z_t$ and $r_t$ in the figure.

The update gate is used to control the degree to which the state information of the previous moment is brought into the current state. The larger the value of the update gate is, the more state information is brought into the previous moment.

The reset gate is used to control the degree of ignoring the state information of the previous moment. The smaller the value of the reset gate, the more it is ignored.

<img src="image/img311.png">

## Forward  communication

$r_t = \sigma(W_r .[h_{(t-1)}, x_t])$

$z_t = \sigma(W_z .[h_{(t-1)}, x_t])$

$\tilde{h_t}$ =$tanh(W_{\tilde h} .[r_t * h_{t-1} , x_t])$

$h_t = (1 - z_t) * h_{t-1} + z_t * \tilde {h_t}$

$y_t = \sigma(W_o . h_t)$

# The Difference in between LSTM and GRU

- GRU parameters are less than LSTM, so it is easy to converge. In the case of a large data set, the expression performance of LSTM is still better than GRU.

- The performance of GRU and LSTM is similar on general data sets.

- Structurally, the GRU has only two gates(update and reset), and the LSTM has three gates (forget, input, output). The GRU directly passes the hidden state to the next unit, and the LSTM uses the memory cell to pass the hidden state.
