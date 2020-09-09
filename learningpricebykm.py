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
options = parser.parse_args()

def theta_csv(theta0, theta1):
	with open("thetas.csv", 'r+') as fd:
		first_line = fd.readline()
		data = str(theta0) + "," + str(theta1) + "\n"
		while True: 
			line = fd.readline()
			if line == data:
				return
			if not line: 
				break
		if first_line == "theta0,theta1\n":
			fd.write(data)
		else :
			newdata = "theta0,theta1\n" + data
			fd.write(newdata)

def predict(theta0, theta1, km):
	return theta0 + theta1 * km

def learning_thetas(X, Y):
	theta0 = 0
	theta1 = 0
	Lrate = 0.1
	rng = range(len(X))
	m = float(len(X))

	for i in range(10):
		B0 = (1/m) * sum([(theta0 + theta1 * X[i]) - Y[i] for i in rng])
		B1 = (1/m) * sum([((theta0 + theta1 * X[i]) - Y[i]) * X[i] for i in rng])

		theta0 -= Lrate * B0
		theta1 -= Lrate * B1
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
		# dev purpose 
		# Xmean= np.mean(X)
		# Ymean= np.mean(Y)
		# B1Up = 0
		# B1Down = 0
		# for i in range(len(X)):
		# 	B1Up += (X[i] - Xmean) * (Y[i] - Ymean)
		# 	B1Down += (X[i]-Xmean) ** 2
		# theta1 = B1Up / B1Down
		# theta0 = Ymean - theta1 * Xmean
		# print (str(theta0) + " | " + str(theta1))
		# 
		print ("8499.599649933216 | -0.0214489635917023")
		theta0, theta1 = learning_thetas(X, Y)
		print (str(theta0) + " | " + str(theta1))
		line = theta0 + theta1 * X
		theta_csv(theta0, theta1)
		predicted = predict(theta0, theta1, int(options.mileage))
		print("The car that have " + str(options.mileage) + "km is estimated for " + str(round(predicted)) + " euro" + ("s" if predicted > 1 else ""))
		if options.graph:
			line = theta0 + theta1 * X
			axes = plt.axes()
			axes.grid()
			plt.scatter(X, Y)
			plt.scatter(int(options.mileage), predicted, c='y')
			plt.plot(X,line, c='r')
			plt.show()
