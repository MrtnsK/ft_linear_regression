import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

def predict(theta0, theta1, km):
	return theta0 + theta1 * km
	
if __name__ == "__main__":
	df = pd.read_csv("data.csv")
	km = df.iloc[0:len(df),0]
	price = df.iloc[0:len(df),1] 

	inputkm = input("Le kilometrage de la voiture a estime :\n")
	slope, intercept, r_value, p_value, std_err = stats.linregress(km, price)
	print(predict(intercept, slope, inputkm))
	axes = plt.axes()
	axes.grid()
	plt.scatter(km,price)
	plt.show()
