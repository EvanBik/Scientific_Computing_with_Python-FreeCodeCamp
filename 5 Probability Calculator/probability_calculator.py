import copy
import random

class Hat:
	def __init__(self, **kwargs):
		self.contents =[]
		for k, v in kwargs.items():
			for _ in range(v):
				self.contents.append(k)

	def draw(self, ball):
		if ball > len(self.contents):
			return self.contents
		remove_balls = []
		for _ in range(ball): 
			choose = random.choice(self.contents)
			remove_balls.append(choose)
			self.contents.remove(choose)
		return remove_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	hat_with_balls = copy.deepcopy(hat)
	N = 0
	M = 0
	target = []
	for i in expected_balls:
		target.append(expected_balls[i])
	for _ in range(num_experiments):
		balls_drawn = hat_with_balls.draw(num_balls_drawn)
		num_target = []
		for x in expected_balls:
			num_target.append(balls_drawn.count(x))	
		if num_target >= target:
			M += 1
	return M/num_experiments