# Experimenting with different parameters for the neural network

I experimented with multiple parameters to improve the accuracy of the neural network.

The neural network primarily comprises of the following: 
1) An input layer (Input shape of IMG_WIDTH * IMG_HEIGHT * 3)
2) An image convolution layer
3) A pooling layer
4) A flattening layer
5) One (or more) hidden layers
6) Optional dropout of data with each hidden layer
7) An output layer with NUM_CATEGORIES number of nodes

Firstly, I tried with an image convolution layer of 16 filters, each of 3x3 kernel, pooling layer of 2x2 size, and no hidden layer nor dropout of data. 

I obtained a considerable accuracy:
Parameters: Layer 2) 16, (3,3), relu  3)pool_size (2,2)  7) softmax
333/333 - 0s - loss: 0.6578 - accuracy: 0.9286 - 490ms/epoch - 1ms/step
333/333 - 0s - loss: 0.6210 - accuracy: 0.9158 - 452ms/epoch - 1ms/step
Average: Accuracy: 0.922

Next, I tried to increase the number of filters of the image convolution layer to 64, keeping other factors constant.
Parameters: Layer 2) 64, (3,3), relu  3)pool_size (2,2)  7) softmax
333/333 - 1s - loss: 0.8071 - accuracy: 0.9246 - 947ms/epoch - 3ms/step
333/333 - 1s - loss: 0.7249 - accuracy: 0.9234 - 1s/epoch - 3ms/step
Average: Accuracy: 0.924 (Slight Rise in Accuracy)

Then, I increased the size of filter to 5x5 to see the effect on accuracy.
Parameters: Layer 2) 64, (5,5), relu  3)pool_size (2,2)  7) softmax
333/333 - 1s - loss: 0.6649 - accuracy: 0.9183 - 853ms/epoch - 3ms/step
333/333 - 1s - loss: 0.8154 - accuracy: 0.9211 - 910ms/epoch - 3ms/step
Average: Accuracy: 0.920 (Slight Fall in Accuracy)
The slight fall may be due to random error in the experiment.

I next maintained (3,3) kernel size and instead tried to increase pool size to (3,3).
Parameters: Layer 2) 64, (3,3), relu  3)pool_size (3,3)  7) softmax
333/333 - 1s - loss: 0.4157 - accuracy: 0.9385 - 719ms/epoch - 2ms/step
333/333 - 1s - loss: 0.4308 - accuracy: 0.9348 - 983ms/epoch - 3ms/step
Average: Accuracy: 0.937 (Rise in Accuracy)
Interestingly, increasing the pool size seems to both increase the accuracy and shorten the time-per-epoch of the neural network. Perhaps by reducing the data set size via max-pooling, trends can be observed more easily.

After that, I tried introducing a new hidden layer of 64 nodes (relu), with no dropout.
Parameters: Layer 2) 64, (3,3), relu  3)pool_size (3,3) 5) 64, relu 7) softmax
333/333 - 1s - loss: 3.5021 - accuracy: 0.0551 - 1s/epoch - 3ms/step
333/333 - 1s - loss: 0.3675 - accuracy: 0.9220 - 788ms/epoch - 2ms/step
333/333 - 1s - loss: 2.4672 - accuracy: 0.3016 - 698ms/epoch - 2ms/step
333/333 - 1s - loss: 3.4928 - accuracy: 0.0556 - 833ms/epoch - 3ms/step
333/333 - 1s - loss: 3.5015 - accuracy: 0.0561 - 1s/epoch - 3ms/step
Average: Accuracy: 0.278 (Significant Fall in Accuracy)

It's an interesting observation that the accuracy significantly falls (and generally 
stays around 0.05) when a hidden layer of 64 nodes with relu activation is added.

I suspect that the number of nodes is too small. Therefore, I increased the number
of nodes to 128 and retried with other parameters being constant.
Parameters: Layer 2) 64, (3,3), relu  3)pool_size (3,3) 5) 128, relu 7) softmax
333/333 - 1s - loss: 0.3809 - accuracy: 0.9430 - 774ms/epoch - 2ms/step
333/333 - 1s - loss: 0.4121 - accuracy: 0.9364 - 833ms/epoch - 3ms/step
Average: Accuracy: 0.940 (Rise in Accuracy)

Indeed, it can be seen that when 128 nodes are used in the hidden layer, the results
become much more stable and the neural network returns a much higher accuracy.
In fact, the accuracy has improved from the previous network without any hidden layer at all.

What about adding another hidden layer of 128 nodes?  I tried with 2 hidden layers,
each of 128 nodes and relu activation. The results are:
Parameters: Layer 2) 64, (3,3), relu  3)pool_size (3,3) 5) 128, relu; 128, relu 7) softmax
333/333 - 1s - loss: 0.4441 - accuracy: 0.9159 - 909ms/epoch - 3ms/step
333/333 - 1s - loss: 0.5120 - accuracy: 0.9108 - 1s/epoch - 3ms/step
Average: Accuracy: 0.913 (Fall in Accuracy)

To my surprise, adding another hidden layer lowers the accuracy of the neural network.
Perhaps the data provided is easy enough to classify, and adding another hidden layer results in unnecessary additional conclusions that impede the process of classifying data
into the correct categories. Besides, adding another layer further drags the whole process.

Let's try adding dropouts to see what happens. I'll stick to one hidden layer since the
results are more ideal.
Parameters: Layer 2) 64, (3,3), relu  3)pool_size (3,3) 5) 128, relu 6)dropout of 0.5 7) softmax
333/333 - 1s - loss: 3.4941 - accuracy: 0.0526 - 740ms/epoch - 2ms/step
333/333 - 1s - loss: 3.4961 - accuracy: 0.0566 - 926ms/epoch - 3ms/step
Average: Accuracy: 0.0546 (Significant Fall in Accuracy)
I seem to have forgotten that this effectively ignores half of the nodes, which explains
why the effect is similar to that with one 64 node hidden layer without dropout.

I increased the number of nodes in the hidden layer by 100% to 256.
Parameters: Layer 2) 64, (3,3), relu  3)pool_size (3,3) 5) 256, relu 6)dropout of 0.5 7) softmax
333/333 - 1s - loss: 0.4150 - accuracy: 0.8939 - 822ms/epoch - 2ms/step
333/333 - 1s - loss: 3.4961 - accuracy: 0.0555 - 996ms/epoch - 3ms/step
Average: Accuracy: 0.475 (Significant Fall in Accuracy)
Compared to the combination of 1 hidden layer of 128 nodes with 0 dropout, this seems to give a much more volatile set of results.


Lastly, what happens if I use two sets of convolution + pooling layers?
Parameters: Set 1: Layer 2) 64, (3,3), relu  3)pool_size (3,3)   Set 2:2) 64, (3,3), relu  3)pool_size (3,3)  5) 256, relu 6)dropout of 0.5 7) softmax
333/333 - 1s - loss: 0.3622 - accuracy: 0.9233 - 767ms/epoch - 2ms/step
333/333 - 1s - loss: 0.5865 - accuracy: 0.8702 - 774ms/epoch - 2ms/step
Average: Accuracy: 0.897 (Fall in Accuracy)
Compared to the accuracy of 0.940 from one set of convolution + pooling layers, it seems
the accuracy has instead dropped by adding one more set of layers.

Ultimately, the accuracy of 0.940 seems to be one of the best possible that can be achieved.
This is using one set of convolution (64 3x3 filters) + maxpooling (2x2) layers and one 
hidden layer of 128 nodes. No dropout was used.

In general, despite the varying accuracy values, one obvious trend I observed is that the accuracy increases as the number of epochs processed increases over time. Except for cases involving accuracy around 0.05 (possibly due to insufficient nodes in hidden layer)