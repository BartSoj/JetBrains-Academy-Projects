file = open("planets.txt", "w")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets = [s + "\n" for s in planets]
file.writelines(planets)
file.close()
