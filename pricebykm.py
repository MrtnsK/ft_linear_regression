import matplotlib.pyplot as plt
from scipy import stats
import csv
import pandas as pd
import numpy as np

def predict(theta0, theta1, km):
	return theta0 + theta1 * km

def reading_csv():
	try:
		with open("data.csv", 'r') as csvfile:
			file = csv.DictReader(csvfile)
			km_grid = []
			price_grid = []
			for data in file:
				km_grid.append(float(data['km']))
				price_grid.append(float(data['price']))
		return km_grid, price_grid
	except:
		print("error while reading csv!")
		exit(1)

if __name__ == "__main__":
	# X, Y = reading_csv()
	data = pd.read_csv("data.csv")
	X = data['km'].values
	Y = data['price'].values

	Xmean= np.mean(X)
	Ymean= np.mean(Y)
	B1Up = 0
	B1Down = 0
	for i in range(len(X)):
		B1Up += (X[i] - Xmean) * (Y[i] - Ymean)
		B1Down += (X[i]-Xmean) ** 2
	theta1 = B1Up / B1Down
	theta0 = Ymean - theta1 * Xmean
	line = theta0 + theta1 * X
	inputkm = input("Le kilometrage de la voiture a estime : ")
	predicted = predict(theta0, theta1, inputkm)
	axes = plt.axes()
	axes.grid()
	plt.scatter(X, Y)
	plt.scatter(inputkm, predicted, c='y')
	plt.plot(X,line, c='r')
	plt.show()
