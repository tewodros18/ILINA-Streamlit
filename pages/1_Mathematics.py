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




selected = st.selectbox("", ["See Fellow's Note for this section", "Sienka", "Tewodros"])

if(selected == "Tewodros"):
    with st.expander("📝Notes"):
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

        st.write('''
        - Mulitplication and Inverse Matrices 
        
        ''')
        st.image("./img/inverses.png")

        st.write('- Loss functions and partial derivatives ')
        st.image('./img/loss.png')
















st.markdown("<h3 style='text-align: left; color: black;'>Checklist</h3>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.write("Linear Algebra and Calculus")

with col2:
    st.checkbox("Linear Combinations, span, and basis vectors", value=True)
    st.checkbox("Linear transformations and matrices", value=True)
    st.checkbox("Matrix multiplication", value=True)
    st.checkbox("Inverse Matrices, column space, determinant, null space", value=True)
    st.checkbox("Chain rule", value=True)

col3, col4 = st.columns([1,1])

with col3:
    st.write("Statistics and Information Theory ")
with col4:
    st.checkbox("Measures of central tendency (mean, median, mode)", value=True)
    st.checkbox("Measures of dispersion (variance, standard deviation, range)", value=True)
    st.checkbox("Basic probability concepts (independence, conditional probability)", value=True)
    st.checkbox("Bayes' theorem", value=True)
    st.checkbox("Random variables (discrete and continuous)", value=True)
    st.checkbox("Probability distributions (normal, binomial, Poisson, etc.) [Only the normal and binomial distributions are necessary right now, the rest is optional]")
    st.checkbox("Sampling methods and sampling distributions [Optional]")
    st.checkbox("Hypothesis testing (null and alternative hypotheses, p-values, significance levels)")
    st.checkbox("Linear regression (simple and multiple) [Optional]")
    st.checkbox("Logistic regression [Optional]")
    st.checkbox("Principal Component Analysis (PCA) [Optional]")
    st.checkbox("Autoregressive models [Optional]")
    st.checkbox("Bayesian inference")
    st.checkbox("Bayesian networks")
    st.checkbox("Entropy and information content")
    st.checkbox("Kullback-Leibler divergence")
    st.checkbox("Cross-entropy")





    