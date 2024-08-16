import streamlit as st 
from Activation_Functions import *

selected = st.selectbox("", ["See Fellow's Note for this section", "Sienka", "Tewodros"])

if(selected == "Tewodros"):
    with st.expander("📝Notes"):
        st.write('- Manual back propagation on a nuron')
        st.image('./img/Neuron.png')
        st.image('./img/backprop.png')

        st.write('- Pytorch implementation')
        st.code('''
        import torch

        x1 = torch.Tensor([2.0]).double(); x1.requires_grad = True
        x2 = torch.Tensor([0.0]).double(); x2.requires_grad = True
        w1 = torch.Tensor([-3.0]).double(); w1.requires_grad = True 
        w2 = torch.Tensor([1.0]).double(); w2.requires_grad = True
        b = torch.Tensor([6.8813735870195432]).double()

        n = x1*w1 + x2*w2 + b 

        o = torch.tanh(n)
        o.backward()
    ''', language="python")



    with st.expander("📝 Implementing Various activation functions with Python"):
        st.subheader("sigmoid")
        plt.cla()
        with st.echo():
            def sigmoid(x):
                """It transforms an input value into a range between 0 and 1."""
                return 1 / (1 + math.exp(-x))
            def plot_sigmoid():
                x = np.linspace(-10, 10, 100)
                y = 1 / (1 + np.exp(-x))
                plt.plot(x, y)
                plt.xlabel('Input')
                plt.ylabel('Output')
                plt.title('Sigmoidal Activation Function')
                plt.grid(True)
            plot_sigmoid()
            st.pyplot(plt)
        
        st.subheader("tanh")

        with st.echo():
            def tanh(x):
                """It is an extension of the sigmoid function and also maps the input to a range between -1 and 1."""
                return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
            def plot_tanh():
                x = np.linspace(-10, 10, 100)
                tanh = np.tanh(x)
                plt.plot(x, tanh)
                plt.xlabel('Input')
                plt.ylabel('Output')
                plt.title('Tanh Activation Function')
                plt.grid(True)
        
            plt.cla()
            plot_tanh()
            st.pyplot(plt)
        plt.cla()
        st.subheader("relu")

        with st.echo():
            def relu(x):
                """It applies a simple thresholding operation to the input values, transforming negative values to zero and leaving positive values unchanged."""
                return max(0,x)
            def plot_relu():
                x = np.linspace(-10, 10, 100)
                relu = np.maximum(0, x)
                plt.plot(x, relu)
                plt.xlabel('Input')
                plt.ylabel('Output')
                plt.title('ReLU Activation Function')
                plt.grid(True)
            plot_relu()
            st.pyplot(plt)

        plt.cla()
        st.subheader("leaky relu")

        with st.echo():
            def leaky_relu(x, alpha=0.1):
                """ Variation of ReLU, however, unlike ReLU, the Leaky ReLU allows a small non-zero gradient for negative inputs"""
                return max(x, alpha * x)
            def plot_leaky_relu():
                x = np.linspace(-10, 10, 100)
                def leaky_relu(x, alpha=0.1):
                    return np.where(x >= 0, x, alpha * x)
                leaky_relu_values = leaky_relu(x)
                plt.plot(x, leaky_relu_values)
                plt.xlabel('Input')
                plt.ylabel('Output')
                plt.title('Leaky ReLU Activation Function')
                plt.grid(True)
            plot_leaky_relu()
            st.pyplot(plt)

    with st.expander("📝 Implementing Micrograd"):
        st.write('''A tiny Autograd engine. Implements backpropagation (reverse-mode autodiff) over a dynamically built DAG
                 . 
                \n This includes building the data structure and operations needed to represent our neural network
    
    - Create the class value that holds information needed in our neural network
    - Define some operations
    - Define how each operation can be backpropagated
    - Define a general call back for backpropagation
                 
                 ''')
        st.code('''
        class Value:
            def __init__(self, data, _children=(), _op='', label='') -> None:
                self.data = data
                self.grad = 0.0 
                self._backward = lambda: None
                self._prev = set(_children)
                self._op = _op
                self.label = label
            def __repr__(self) -> str:
                return f"Value(data={self.data})"
            def __add__(self,other):
                other = other if isinstance(other,Value) else Value(other)
                out = Value(self.data + other.data, (self,other), '+')

                def _backward():
                    self.grad += 1.0 * out.grad
                    other.grad += 1.0 * out.grad
                out._backward = _backward

                return out
            def __mul__(self,other):
                other = other if isinstance(other,Value) else Value(other)
                out = Value(self.data * other.data, (self,other), '*')

                def _backward():
                    self.grad += out.grad * other.data
                    other.grad += out.grad * self.data 
                out._backward = _backward

                return out
            def __truediv__(self,other):
                return self * other ** -1
            def __pow__(self,other):
                assert isinstance(other, (int,float))
                out = Value(self.data ** other, (self,), f'**{other}')
                def _backward():
                    self.grad += other * (self.data ** (other - 1)) * out.grad
                out._backward = _backward 
                return out 
            #A fallback function that gets called when int * value can't be done
            def __rmul__(self,other):
                return self * other 
            #A fallback function that gets called when int + value can't be done
            def __radd__(self, other):
                return self + other
            def __neg__(self):
                return self * -1 
            def __sub__(self,other):
                return self + (-other)
            def tanh(self):
                x = self.data
                tanh = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
                out = Value(tanh, (self, ), "tanh")

                def _backward():
                    self.grad = (1 - tanh**2) * out.grad
                out._backward = _backward

                return out
            def exp(self):
                x = self.data
                out = Value(math.exp(x), (self,),'exp')

                def _backward():
                    self.grad = out.data * out.grad # d/dx of e**x
                out._backward = _backward
                return out
            
            def backward(self):
                topo = []
                visited = set()
                def build_topo(v):
                    if v not in visited:
                        visited.add(v)
                        for child in v._prev:
                            build_topo(child)
                        topo.append(v)
                build_topo(self)

                self.grad = 1.0
                for node in reversed(topo):
                    node._backward()

        ''', language="python")



col1, col2 = st.columns([1,1])

with col1:
    st.write("Supervised Learning")

with col2:
    st.checkbox("Linear regression", value=True)
    st.checkbox("Logistic regression", value=True)
    st.checkbox("Decision trees [Optional]")

col3, col4 = st.columns([1,1])

with col3:
    st.write("Unsupervised Learning")
with col4:
    st.checkbox("Clustering",value=True)
    st.checkbox("Dimensionality reduction")
    st.checkbox("Anomaly detection [Optional]")

col5, col6 = st.columns([1,1])

with col5:
    st.write("Deep Learning")
with col6:
    st.checkbox("Forward propagation and loss functions", value=True)
    st.checkbox("Backpropagation and gradient descent", value=True)
    st.checkbox("Optimizers (SGD, Adam, etc)", value=True)
    st.checkbox("Convolutional neural networks")
    st.checkbox("Recurrent neural networks")
    st.checkbox("Reinforcement Learning")
