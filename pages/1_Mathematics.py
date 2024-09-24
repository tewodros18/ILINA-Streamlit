import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 
import statistics 



st.image("./img/upskill_stack.png")

st.markdown("<h3 style='text-align: center; color: black;'>Starting With Math</h1>", unsafe_allow_html=True)

st.write('''
The primary motivation for starting with the study plan's base layer is to build the mathematical framework for representing and manipulating data, understanding algorithms, and optimizing models. 
''')

st.write('''      
| Concept                           | Motivation for understanding how it is used in ML                                                                                                                                                                                                                                                           |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| N-dimensional Vectors             | Understanding dot product, cross-product, addition, and subtraction is not for simple rote memorization sake, but because “features” from machine learning are usually represented as N-dimensional vectors.                                                                                                |
| Matrices                          | Being able to represent our linear system as matrices is crucial to enable easier computer representation, manipulation, and use of specific hardware to accelerate the computation of the information.  - we feed our neural network input in the form of matrices, compute weights in matrices, and more. |
| EigenValues and EigenVectors, SVD | Real-life data can be quite large with a lot of features, we need methods to deal with decomposing such representative matrices into a manageable form while preserving information crucial for our models.                                                                                                 |

''')



st.markdown("<h3 style='text-align: left; color: black;'>Notes Outline</h3>", unsafe_allow_html=True)

with st.expander("Linear transformations and matrices",expanded=False):
    st.write('''
        Linear Algebra (Gilbert Strang & 3Blue1Brown): The series “Essence of linear Algebra” was an excellent introduction to prime myself in visualizing what all the concepts I was about to study represented. Understanding vector operations through the visualization lens of  “moving through space” made it easier to build intuition of determinants, span, and basis vectors.

The lectures by Gilbert Strang build foundational understanding and enable the manipulation of concepts by looking at them from various perspectives.
    \n - The Geometry of Linear Equations: 
    I understood how linear algebra can be used in solving linear equations, The three different forms of representing these systems, which include: 
                ''')
    st.write("Row Method")
    st.image("./img/row.png")
    st.write("Column  Method")
    st.image("./img/column.png")
    st.write("Matrix  Method")
    st.image("./img/Matrix.png")
with st.expander("Matrix multiplication,Chain rule",expanded=False):
    st.write('''
    - Mulitplication and Inverse Matrices 
    
    ''')
    st.image("./img/inverses.png")

    st.write('- Loss functions and partial derivatives ')
    st.image('./img/loss.png')

with st.expander("Measures of central tendency (mean, median, mode)",expanded=False):
    st.image("./img/Mean_Median_Mode.PNG")
with st.expander("Measures of dispersion (variance, standard deviation, range)", expanded=False):
    st.write('''
    - Range: 
    The simplest measure of dispersion, it's the difference between the largest and smallest values in a dataset.
    - Variance: 
    Measures how far a set of numbers is spread out from their mean. A high variance means the numbers are spread out, while a low variance
    means they're clustered together.
    - Standard Deviation: 
    The square root of the variance. It's often preferred over variance because it's in the same units as the original data.
    ''')
with st.expander("Basic probability concepts (independence, conditional probability)" , expanded=False):
    st.write('''
    - Independence: Events are independent if the occurrence of one does not affect the probability of the other. For instance, flipping a coin twice are independent events.
    - Conditional Probability: The probability of one event occurring given that another event has already occurred. For example, the probability of rain today given that it rained yesterday.
    ''')
with st.expander("Bayes' theorem", expanded=False):
    st.write("Used to determine the conditional probability of events")
    st.image("./img/Bayes.PNG")
with st.expander("Random variables (discrete and continuous)", expanded=False):
    st.write('''
    A random variable is a numerical quantity whose value is determined by chance.

    - Discrete Random Variables: Can take on a countable number of values. For example, the number of heads when flipping a coin.
    - Continuous Random Variables: Can take on any value within a given range like the height of a person.
    
    ''')
with st.expander("Probability distributions (normal, binomial)", expanded=False):

    st.write('''- Normal Distribution also called "bell curve," it's a symmetrical distribution where the majority of the data is clustered around the mean.''')

    x_axis = np.arange(-20, 20, 0.01) 
  
    # Calculating mean and standard deviation 
    mean = statistics.mean(x_axis) 
    sd = statistics.stdev(x_axis) 
    
    plt.plot(x_axis, norm.pdf(x_axis, mean, sd)) 
    plt.show() 
    st.pyplot(plt)

    st.write('''- binomial distribution is the discrete probability distribution that gives only two possible results in an experiment, either Success or Failure''')

with st.expander("Hypothesis testing (null and alternative hypotheses, p-values, significance levels)", expanded=False):
    st.write('''Used to determine if there is enough evidence to support a claim.
- Null Hypothesis: The hypothesis that there is no difference or effect.
- Alternative Hypothesis: The hypothesis that there is a difference or effect.
- P-value: The probability of observing a result as extreme as the one obtained, assuming the null hypothesis is true.
- Significance Level: A threshold used to decide whether to reject or fail to reject the null hypothesis.''')
with st.expander("Linear regression (simple and multiple) [Optional]", expanded=False):
    st.write('''
A statistical method used to model the relationship between a dependent variable and one or more independent variables.
- Best fitting line for the dataset
''')
    x = [1,2,3,4]
    y = [3,5,7,10] 

    coef = np.polyfit(x,y,1)
    poly1d_fn = np.poly1d(coef) 
    

    plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k') 

    plt.xlim(0, 5)
    plt.ylim(0, 12)

    st.pyplot(plt)
with st.expander("Logistic regression [Optional]", expanded=False):
    st.write('''- Logistic regression is used to predict the probability of a binary outcome. It's often used in classification problems.''')
    st.image("./img/logstic.PNG")
with st.expander("Regularization Techniques", expanded=False):
    st.write('''
Are used to prevent overfitting in machine learning models. They add a penalty term to the loss function.
- L1 Regularization or Lasso regression, it tends to shrink coefficients to zero, leading to feature selection.
- L2 Regularization or Ridge regression, it shrinks coefficients towards zero but doesn't set them to exactly zero.
''')
    st.image("./img/reg.PNG")
with st.expander("Principal Component Analysis (PCA) [Optional]", expanded=False):
    st.write('''A technique used to reduce the dimensionality of a dataset while preserving the most important information.''')
    st.image("./img/PCA.PNG")














