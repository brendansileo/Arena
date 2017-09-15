import math

class bullet:

	xv = 0
	yv = 0
	x = 0
	y = 0
	time_alive = 0
	max_time = 30
	screen_w = 0
	screen_h = 0
	hopped = False

	def __init__(self, xv, yv, x, y, width, height):
		self.xv = xv
		self.yv = yv
		self.x = x
		self.y = y
		self.screen_w = width
		self.screen_h = height

	def kill(self, bullets):
		for i in range(len(bullets)):
			if bullets[i] == self:
				del bullets[i]
				break


	def tick(self, bullets):
		self.time_alive+=1
		self.x += self.xv*2
		self.y += self.yv*2

		if self.x < 0:
			if not self.hopped:
				self.x = self.screen_w
				self.hopped = True
			else:
				self.kill(bullets)
		elif self.x > self.screen_w:
			if not self.hopped:
				self.x = 0
				self.hopped = True
			else:
				self.kill(bullets)
		if self.y < 0:
			if not self.hopped:
				self.y = self.screen_h
				self.hopped = True
		elif self.y > self.screen_h:
			if not self.hopped:
				self.y = 0
				self.hopped = True
			else:
				self.kill(bullets)

		if self.time_alive >= self.max_time:
			self.kill(bullets)
			return None, None
		else:
			return self.x, self.y
