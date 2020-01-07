import numpy as np
import matplotlib.pyplot as plt
from building import *

class Drawer:
	def __init__(self, building):
		booleanMap = np.array(building.grid.grid)
		self.blueprint = np.zeros(booleanMap.shape)
		
		for i in range(len(booleanMap)):
			for j in range(len(booleanMap[i])):
				self.blueprint[i][j] = 7.5
				if booleanMap[i][j]:
					self.blueprint[i][j] = 8
		for i in building.exits:
			self.blueprint[i.x][i.y] = 2
		for i in building.danger_sources:
			for j in i.danger_area:
				self.blueprint[j.x][j.y] = 3.5
		for i in building.agents:
			self.blueprint[i.x][i.y] = 10

		self.blueprint[0][0] = 0

	def draw(self):
		plt.imshow(self.blueprint, cmap = 'tab10')
		plt.show()