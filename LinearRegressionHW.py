from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plot
import numpy as np


def linear_regression(x, y):

    #get number of points
    n = np.size(x)

    #get mean of x and y
    mu_x = np.mean(x)
    mu_y = np.mean(y)
    exy = np.sum(x*y)
    ex2 = np.sum(np.power(x,2))
    
    #get deviation and cross-deviation about x
    sigs_xy = exy - n*mu_x*mu_y #multiplication of the means is equal to sum(x)*sum(y) / 16, so multiply by 4 to offset it
    sigs_xx = ex2 - n*mu_x*mu_x

    beta = sigs_xy / sigs_xx
    alpha = mu_y - beta*mu_x

    return (alpha, beta)

def plot_linear_regression(x, y, a, b):
    #plot the points as a scatter plot
    plot.scatter(x,y,color  = "m", marker="o", s = 30)

    y_predicate = a + b*x

    plot.plot(x, y_predicate, color="g")

    plot.xlabel("X")
    plot.ylabel("Y")

    plot.show()

def main():
    x = np.array([3,5,7,9,12,15,18])
    y = np.array([100,250,330,590,660,780,890])

    a, b = linear_regression(x,y)
    #plot_linear_regression(x, y, a, b)


    X = x
    Y = y
    XX = np.reshape(X, (-1,1))
    reg = LinearRegression().fit(XX,Y)
    
    plot_linear_regression(x,y,reg.intercept_, reg.coef_)
main()