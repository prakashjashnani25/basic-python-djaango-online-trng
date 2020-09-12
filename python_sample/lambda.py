people =[
	{"name":"Harry","house":"a"},
	{"name":"cho","house":"b"}
]

#Sort the people

def f(person):
	return person["name"]

#Sort by name
people.sort(key=f)

print(people)

def f1(person):
	return person["house"]

people.sort(key=f1)

print(people)

people.sort(key = lambda person: person["name"])

print(people)


