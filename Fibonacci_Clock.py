import matplotlib.pyplot as plt 
from time import sleep
from PIL import Image
import random

def activity(red, green, blue, time, h, m):
	slices = []
	colors = []
	#Add the sequence and corresponding color with slices and colors list
	for i in range(len(red)):
		slices.append(red[i])
		colors.append('r')
	for i in range(len(green)):
		slices.append(green[i])
		colors.append('g')
	for i in range(len(blue)):
		slices.append(blue[i])
		colors.append('b')

	for i in range(len(slices)):
		for j in range(len(time)):
			if(slices[i] == time[j]):
				time[j] = 0
				break
	for i in range(len(time)):
		if(time[i] != 0):
			slices.append(time[i])
			colors.append('y')
	#Define the types of possibilities
	activities = []
	for i in range(len(slices)):
		if(colors[i] == 'r'):
			activities.append('Hour')
		elif(colors[i] == 'g'):
			activities.append('Minutes')
		elif(colors[i] == 'b'):
			activities.append('Both Hour and Minutes')
		else:
			activities.append('')
		# activities.append(str(slices[i]))
	#Create the pie chart
	plt.pie(slices, labels = activities, colors=colors, 
		startangle=90, shadow = True, explode = (0.1, 0.1, 0.1, 0.1, 0.1),
		radius = 1.2, autopct = '%1.1f%%')
	s = str(m)
	if(len(s) < 2):
		s = '0' + s
	#Show the title(i.e. Actual time)
	plt.title("Actual Time\n" + (str(h) + '.' + s))
	plt.legend()
	#Generate random file name
	file_name = str(random.randint(1,10000))
	file_name = file_name + '.png'
	#Save the image in .png format
	plt.savefig(file_name)
	img = Image.open(file_name)
	#Show image
	img.show()
	plt.figure()
	#Gives delay of 5 minutes
	sleep(3)

def Knapsack(h, time):
	DP = [[0 for val in range(h + 1)]
				for i in range(len(time) + 1)]
	#Check possibility of the hour and minutes representation
	for i in range(len(time) + 1):
		for val in range(h + 1):
			if(i == 0 or val == 0):
				DP[i][val] = 0
			elif(time[i-1] <= val):
				DP[i][val] = max(DP[i-1][val], time[i-1] + DP[i-1][val - time[i-1]])
			else:
				DP[i][val] = DP[i-1][val]

	res = DP[len(time)][h]
	arr = []
	#Find the fibbonacci numbers that can be used to represent the hour of minutes
	for i in range(len(time), 0, -1):
		if(res <= 0):
			break;
		if(res == DP[i-1][val]):
			continue
		else:
			arr.append(time[i-1])
			res = res - time[i-1]
	#Return the sequence
	return arr
	
def findColour(hour, minutes):
	red = []
	green = []
	blue = []
	p = 0
	res1 = [False for i in range(len(hour))]
	res2 = [False for i in range(len(minutes))]
	for i in range(len(hour)):
		p = 0
		if(res1[i] == False):
			for j in range(len(minutes)):
				if(res2[j] == False):
					if(hour[i] == minutes[j]):
						p = 1
						# k = j
						break;
			if(p == 0):
				red.append(hour[i])
				res1[i] = True
			else:
				blue.append(hour[i])
				res1[i] = True
				res2[j] = True
	for i in range(len(minutes)):
		if(res2[i] == False):
			green.append(minutes[i])
	#Return three color sequence for Hour and minutes
	return [red, green, blue]
#Clock representation using five fibonacci no (1, 1, 2, 3, 5) 
def main():
	#Initialization of hour
	h = 2
	#Initialization of minutes
	m = 0
	while(1):
		for i in range(100000000):
			k = i
		#First five fibbonacci number
		time = [1, 1, 2, 3, 5]
		count = m / 5
		count = int(count)
		hour = []
		minutes = []
		#Find the fibonacci number's that repesent the current hour
		hour = Knapsack(h, time)
		#Find the fibonacci number's that repesent the current minutes
		minutes = Knapsack(cnt, time)
		#Here Red denotes Hour, Green denotes minutes and Blue denotes both hour and minutes
		red, green, blue = findColour(hour, minutes)

		print("red ", red)
		print("green ", green)
		print("blue ", blue)
		#Show the fibbonaccy clock for the time instant
		activity(red,green, blue, time, h, m)
		if(m == 55):
			if(h == 12):
				h = 1
			else:
				h = h + 1
			m = 0
		else:
			m = m + 5
main()
