def announce(f):
	def wrapper():
		print("Abount To Run")
		f()
		print("Done !!!")
	return wrapper


#@announce
def hello():
	print("Hello World!!!")

announce(hello)()
