# ML_Interview_Prep_Resources
Resources to prepare for an ML interview

An overview: https://www.interviewbit.com/machine-learning-interview-questions/

Bias-Variance Tradeoff: https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229

Bayes Theorem: https://machinelearningmastery.com/bayes-theorem-for-machine-learning/

Naive Bayes: https://machinelearningmastery.com/classification-as-conditional-probability-and-the-naive-bayes-algorithm/

Kernel Density Estimation: https://jakevdp.github.io/PythonDataScienceHandbook/05.13-kernel-density-estimation.html

How does Lasso or Ridge deal with multicollinearity problem?: https://www.andreaperlato.com/mlpost/deal-multicollinearity-with-lasso-regression/
https://www.andreaperlato.com/mlpost/deal-multicollinearity-with-ridge-regression/

Variance Inflation Factor: https://www.investopedia.com/terms/v/variance-inflation-factor.asp

Regularisation in regression: https://www.datacamp.com/community/tutorials/tutorial-ridge-lasso-elastic-net


Logistic Regression: https://christophm.github.io/interpretable-ml-book/logistic.html

Decision Trees: https://machinelearningmastery.com/classification-and-regression-trees-for-machine-learning/ Code Example: https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/

Principle Component Analysis (PCA): https://builtin.com/data-science/step-step-explanation-principal-component-analysis

RNN-LSTM-GRU: https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21

Word2Vec: https://jalammar.github.io/illustrated-word2vec/

Variational Auto Encoders: https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73

Graph NN: https://theaisummer.com/graph-convolutional-networks/

Laplacian: https://mbernste.github.io/posts/laplacian_matrix/

Best tutorial on transformers and attention: Sebastian Raschka's playlist in YouTube 

Why large weights are prohibited for neural networks?

TLDR: Your weights are large, they are more sensitive to small noises in the input data. So, when a small noise is propagated through your network with large weights, it produces much different value in the output layer of the NN rather than a network with small weights. (https://datascience.stackexchange.com/questions/23287/why-large-weights-are-prohibited-in-neural-networks)
L2 regularization will help you control the weight growth. You should care not about the max values of weights, but about the weight distribution shape. Usually the weights form a Gaussian-like distribution, and if the tails are shallow, you can clip a lot of the tail without affecting accuracy. For example, the values might range from -4 to 4, but 90% of weights will be in the -2 to 2 range. In this case, it should be safe to clip all weights larger than 2, or less than -2. Plot the histogram of the weights to see what I mean.

Loss function convexity

In the case of the Least Squares cost function for linear regression it is easy to check that the cost function is always convex regardless of the dataset. (https://jermwatt.github.io/machine_learning_refined/notes/5_Linear_regression/5_2_Least.html)

NN optimization algos

https://ruder.io/optimizing-gradient-descent/index.html#fn14

Covariance versus Correlation (what happens if we use correlation matrix instead of covariance matrix for PCA computation?)

https://builtin.com/data-science/covariance-vs-correlation

CCA

https://gregorygundersen.com/blog/2018/07/17/cca/

Convolution and Correlation

http://www.dspguide.com/ch6/2.htm
