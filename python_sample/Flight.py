class Flight():
	def __init__(self,capacity):
		self.capacity=capacity
		self.passanger=[]
	
	def add_passanger(self, name):
		if self.open_seats()<=0:
			return False
		self.passanger.append(name)
		return True

	def open_seats(self):
		return self.capacity - len(self.passanger)
flight =  Flight(3)

people = ["Harry", "Ron", "Hrmonie","Ginnie","Test"]

for person in people:
	success = flight.add_passanger(person)
	if success:
		print(person,"Added Successfully")
	else:
		print(person,"Not added Sucessfullt")


