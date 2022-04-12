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

Loss function convexity

In the case of the Least Squares cost function for linear regression it is easy to check that the cost function is always convex regardless of the dataset. (https://jermwatt.github.io/machine_learning_refined/notes/5_Linear_regression/5_2_Least.html)
