import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

parser = argparse.ArgumentParser(
    description='Predict a car\'s value with linear regression.'
)
parser.add_argument('mileage', help='car\'s mileage'
)
parser.add_argument('--graph', '-g',
    action='store_true',
    help='show graph'
)
parser.add_argument('--leastsquare', '-l',
    action='store_true',
    help='use the least square method'
)
options = parser.parse_args()

def predict(theta0, theta1, km):
	return theta0 + theta1 * km

def least_square(X, Y):
	Xmean= np.mean(X)
	Ymean= np.mean(Y)
	B1Up = 0
	B1Down = 0
	for i in range(len(X)):
		B1Up += (X[i] - Xmean) * (Y[i] - Ymean)
		B1Down += (X[i]-Xmean) ** 2
	theta1 = B1Up / B1Down
	theta0 = Ymean - theta1 * Xmean
	return theta0, theta1

if __name__ == "__main__":
	if options.mileage:
		try:
			data = pd.read_csv("data.csv")
			X = data['km'].values
			Y = data['price'].values
		except:
			print("Error with the data.csv file!")
			exit (1)
		if options.leastsquare:
			theta0, theta1 = least_square(X, Y)
		else:
			try:
				thetas = pd.read_csv("thetas.csv")
				theta0 = thetas.at[0, 'theta0']
				theta1 = thetas.at[0, 'theta1']
			except:
				print("Error with the thetas.csv file!")
				exit (1)
		line = theta0 + theta1 * X
		predicted = predict(theta0, theta1, int(options.mileage))
		print("The car that have " + str(options.mileage) + "km is estimated for " + str(round(predicted)) + " euro" + ("s" if predicted > 1 else ""))
		if options.graph:
			axes = plt.axes()
			axes.grid()
			plt.scatter(X, Y)
			plt.scatter(int(options.mileage), predicted, c='y')
			plt.plot(X,line, c='r')
			plt.title('Estimation prix')
			plt.xlabel('Kilometrage')
			plt.ylabel('Prix')
			plt.show()
