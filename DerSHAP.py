def DerSHAP(df):
    """
    Input: 
        df: M-by-d matrix, that contains estimated partial derivatives(in our case, approximated by finite difference method)
        M: the number of random samples
        d: dimension of the inputs
    Output: 
        norm_shap:  normalized DerSHAP values
    Parameters:
        C: d-by-d matrix, this is the gradient matrix
        shap: d-by-1 array, this is the DerSHAP values array
        norm_shap: d-by 1 array, this is the normalized DerSHAP values
    """
    C = np.dot(df.transpose(), df)
    C = abs(C)
    shap = np.zeros(len(C))
    for ii in range(len(C)):
        shap[ii] = 0.5*C[ii,ii]
        temp = 0
        for jj in range(len(C[0])):
            temp = 0.5 * C[ii,jj]
        shap[ii] += temp
    norm_shap = [shap[ii]/sum(shap) for ii in range(len(shap))]
    return norm_shap
