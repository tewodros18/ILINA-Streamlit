import streamlit as st

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

with st.expander("Linear transformations and matrices",expanded=True):
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
with st.expander("Matrix multiplication,Chain rule",expanded=True):
    st.write('''
    - Mulitplication and Inverse Matrices 
    
    ''')
    st.image("./img/inverses.png")

    st.write('- Loss functions and partial derivatives ')
    st.image('./img/loss.png')

with st.expander("Measures of central tendency (mean, median, mode)",expanded=True):
    st.image("./img/Mean_Median_Mode.PNG")
with st.expander("Measures of dispersion (variance, standard deviation, range)", expanded=True):
    st.write('''
    - Range: 
    The simplest measure of dispersion, it's the difference between the largest and smallest values in a dataset.
    - Variance: 
    Measures how far a set of numbers is spread out from their mean. A high variance means the numbers are spread out, while a low variance
    means they're clustered together.
    - Standard Deviation: 
    The square root of the variance. It's often preferred over variance because it's in the same units as the original data.
    ''')
with st.expander("Basic probability concepts (independence, conditional probability)" , expanded=True):
    st.write('''
    - Independence: Events are independent if the occurrence of one does not affect the probability of the other. For instance, flipping a coin twice are independent events.
    - Conditional Probability: The probability of one event occurring given that another event has already occurred. For example, the probability of rain today given that it rained yesterday.
    ''')
with st.expander("Bayes' theorem"):
    st.write("Is mathematical formula used to determine the conditional probability of events")
    st.image("./img/Bayes.PNG")
with st.expander("Random variables (discrete and continuous)"):
    ""
with st.expander("Probability distributions (normal, binomial)"):
    ""
with st.expander("Sampling methods and sampling distributions [Optional]"):
    ""
with st.expander("Hypothesis testing (null and alternative hypotheses, p-values, significance levels)"):
    ""
with st.expander("Linear regression (simple and multiple) [Optional]"):
    ""
with st.expander("Logistic regression [Optional]"):
    ""
with st.expander("Principal Component Analysis (PCA) [Optional]"):
    ""
with st.expander("Autoregressive models [Optional]"):
    ""
with st.expander("Bayesian inference"):
    ""
with st.expander("Bayesian networks"):
    ""
with st.expander("Entropy and information content"):
    ""
with st.expander("Kullback-Leibler divergence"):
    ""
with st.expander("Cross-entropy"):
    ""













