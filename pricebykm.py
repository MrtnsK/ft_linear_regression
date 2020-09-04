import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import csv

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
	km, price = reading_csv()

	inputkm = input("Le kilometrage de la voiture a estime :\n")
	slope, intercept, r_value, p_value, std_err = stats.linregress(km, price)
	print(predict(intercept, slope, inputkm))


	#axes = plt.axes()
	#axes.grid()
	#plt.scatter(km,price)
	#plt.show()
