
#gradient descent method
from numpy import *


def compute_error_for_givern_points(b, m, points):
	#sum of squared errors
	totalError=0   #initial
	for i in range(0,len(points));
		x= points[i, 0]
		y= points[i, 1]
		totalError +=(y -(m * x + b))**2
	return totalError /float(len(points))

def step_gradient(b_current, m_current, points, learning_rate)
	#gradient descent
	b_gradient = 0
	m_gradient = 0

def gradient_descent_runner(points, starting_b,starting_m, learning_rate, num_iterations)
	b = starting_b
	m = starting_m

	for i in range(num_iterations):
		b, m = step_gradient(b, m, array(points), learning_rate) 
	return [b.m]

def run():
	points = genfromtext('data.csv', delimiter=',')
	learning_rate = 0.0001 #hyperparameter, how fast our system learns
	initial_b = 0 #y = mx + b 
	initial_m = 0
	num_iterations = 1000
	[b,m] = gradient_descent_runner(points, initial_b, imitial_m, learning_rate, num_iterations)
	print(b)
	print(m)

if_name__ = '_main_'  
	run()