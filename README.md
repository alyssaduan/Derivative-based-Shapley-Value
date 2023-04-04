# Description

DerSHAP is based on the first-order partial derivatives of the underlying function. The computational complexity of the method is linear in dimension (number of features), as opposed to the exponential complexity of other Shapley value approaches in the literature. 

# Requirements and Dependencies

* [numpy](http://www.numpy.org/)
* [scipy](http://www.scipy.org/), >= 0.15.0
* [matplotlib](http://matplotlib.org/)

For the users would like to apply DerSHAP to machine learning examples, 

* [sklearn](https://scikit-learn.org/stable/)

# Usage

For detailed examples of usage and results, see the Jupyter notebooks. 

The core function is contained in the `DerSHAP.py` file. 

# Examples

We apply DerSHAP to two datasets from machine learning, Amazon stock data and Boston housing data, and compare it with SHAP and KernelSHAP. 

If you have questions or feedback, contact [Hui Duan](hd19g@fsu.edu).

