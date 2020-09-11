import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def theta_csv(theta0, theta1):
	with open("thetas.csv", 'r+') as fd:
		data = str(theta0) + "," + str(theta1) + "\n"
		newdata = ",theta0,theta1\n0," + data
		fd.write(newdata)

def scaling_data(data, scale):
    return data / scale

def learning_thetas(thetas, X, Y):
	Lrate = 1
	m = float(len(X))

	while (1):
		tmp = thetas
		thetas = thetas - Lrate * (1 / m) * (X.T @ ((X @ thetas) - Y))
		if np.array_equal(thetas, tmp):
			break
	return thetas

if __name__ == "__main__":
	try:
		data = pd.read_csv("data.csv")
		X = np.array(data['km'].values)
		X_raw = X
		X = scaling_data(X, max(X_raw))
		X = np.c_[np.ones(X.shape[0]), X]
		Y = np.array(data['price'].values)
		Y_raw = Y
		Y = scaling_data(Y, max(Y_raw))
	except:
		print("Error with the data.csv file!")
		exit (1)
	thetas = np.array([0,0])
	thetas = learning_thetas(thetas, X, Y)
	thetas[0] = thetas[0] * max(Y_raw)
	thetas[1] = thetas[1] * (max(Y_raw) / max(X_raw))
	theta_csv(thetas[0], thetas[1])
	line = thetas[0] + thetas[1] * X_raw
	plt.scatter(data['km'].values, data['price'].values)
	plt.plot(X_raw,line, c='r')
	plt.title('Estimation prix')
	plt.xlabel('Kilometrage')
	plt.ylabel('Prix')
	plt.show()
