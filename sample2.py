import numpy
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planet_to_initial = {planet: planet[0] for planet in planets}
print planet_to_initial

print planet_to_initial.values()



rolls = numpy.random.randint(low=1, high=6, size=10)
print rolls <= 3
