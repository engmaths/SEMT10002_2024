def f(X):

    def g(i1, i2, X):
        tmp = X[i1]
        X[i1] = X[i2]
        X[i2] = tmp
        return X
    
    for i in range(len(X)):
        sublist = X[i:]
        im, Xm = fun(sublist)
        X = g(i, im + i, X)

    return X

L = [6, 3, 7, -3, 1, 5, 2]

def fun(X):
    im = 0
    Xm = X[im]
    
    for i in range(len(X)):
        if X[i] < Xm:
            im = i
            Xm = X[i]

    return im, Xm

print(f(L))
