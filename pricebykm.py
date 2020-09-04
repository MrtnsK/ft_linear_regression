import matplotlib.pyplot as plt
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

	inputkm = input("Le kilometrage de la voiture a estime : ")
	slope, intercept, r_value, p_value, std_err = stats.linregress(km, price)
	predicted = predict(intercept, slope, inputkm)

	print("slope : " + str(slope) + " intercept : " + str(intercept))

	predicted_grid = [intercept + slope * i for i in km]
	axes = plt.axes()
	axes.grid()
	plt.scatter(km,price)
	plt.scatter(inputkm, predicted, c='y')
	plt.plot(km, predicted_grid, c='r')
	plt.show()
