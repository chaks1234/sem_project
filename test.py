#import numpy as np
import matplotlib.pyplot as plt


def graph(x,y):
	plt.axis([0, 50, -10, 10])
	plt.ion()
	plt.plot(x,y)
	plt.pause(0.05)



'''x = list()
y = list()
for i in range(50):
	if i < 50:
		x.append(i)
	if i >= 50:
		y.pop(0)
		plt.cla()
	y.append(np.random.random())
	
	




	y = np.random.random()
	plt.scatter(i, y)

graph(x,y)

while True:
    plt.pause(0.05)'''
