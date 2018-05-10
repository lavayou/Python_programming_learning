import matplotlib.pyplot as plt
'''
squares = [1, 4, 9, 16, 25]
input_values = [x for x in range(1,6)]

plt.plot(input_values, squares, linewidth = 5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()
'''
'''
input_values = list(range(1,1001))
squares = [x**2 for x in input_values]
plt.scatter(input_values, squares, s=3, edgecolor='none', c=squares, cmap=plt.cm.Blues)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('square_plot.png', bbox_inches = 'tight')
'''

from random import choice

class RandomWalk():
	def __init__(self, num_points=5000):
		'''随机的次数
		'''
		self.num_points = num_points
		'''初始化起始位置
		'''
		self.x_values = [0]
		self.y_values = [0]
	
	def walk(self):
		'''蚂蚁开始走动
		'''
		direction = [1, -1]
		distance = [0, 1, 2, 3, 4]
		
		while len(self.x_values) < self.num_points:
			x_direction = choice(direction)
			x_distance = choice(distance)
			x_step = x_direction * x_distance
			
			y_direction = choice(direction)
			y_distance = choice(distance)
			y_step = y_direction * y_distance
			
			if x_step ==0 and y_step ==0:
				continue
			
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)

			
for num in range(0,33): #多次调用，生成32张图片

	rw = RandomWalk(5000)
	rw.walk()

	input_values = rw.x_values
	squares = rw.y_values

	colorseq=list(range(1,5001))
	plt.scatter(input_values, squares, s=1, c=colorseq, cmap=plt.cm.GnBu) #创建散点图，并指定 colormap 为 GnBu

	plt.scatter(0, 0, c='green', edgecolor='none', s=50) #起始点设为绿色
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor = 'none', s=50) #终点为红色

	plt.title("Ant Walk Figure", fontsize=10)
	'''
	plt.xlabel("X", fontsize=14)
	plt.ylabel("Y", fontsize=14)
	plt.tick_params(axis='both', which='major', labelsize=14)
	'''
	plt.axes().spines['top'].set_visible(False)
	plt.axes().spines['right'].set_visible(False)
	plt.axes().spines['bottom'].set_visible(False)
	plt.axes().spines['left'].set_visible(False)
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False) #隐藏 Figure 边框、轴

	print('saving ' + str(num)) 
	plt.savefig('./AntWalk/AntWalk' + '-' + str(num) +'.png' ,dpi=500, bbox_inches = 'tight')  #存到 AntWalk 文件夹中
	plt.clf() #clean figure.
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		