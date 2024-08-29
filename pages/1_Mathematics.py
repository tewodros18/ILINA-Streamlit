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

with st.expander("📝Linear transformations and matrices"):
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
with st.expander("📝Matrix multiplication,Chain rule"):
    st.write('''
    - Mulitplication and Inverse Matrices 
    
    ''')
    st.image("./img/inverses.png")

    st.write('- Loss functions and partial derivatives ')
    st.image('./img/loss.png')

with st.expander("Measures of central tendency (mean, median, mode)"):
    ""
with st.expander("Measures of dispersion (variance, standard deviation, range)"):
    ""
with st.expander("Basic probability concepts (independence, conditional probability)"):
    ""
with st.expander("📝Bayes' theorem"):
    ""
with st.expander("Random variables (discrete and continuous)"):
    ""
with st.expander("Probability distributions (normal, binomial, Poisson, etc.) [Only the normal and binomial distributions are necessary right now, the rest is optional]"):
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













