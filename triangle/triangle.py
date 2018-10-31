import itertools

def check_triangle(func):
	def wrapper(sides):
		if len(sides) > 3:
			raise ValueError("not a triangle!")
		elif 0 in sides:
			return False

		for x, y, z in itertools.permutations(tuple(sides), r=3):
			if x + y < z:
				return False
			elif x + y == z:
				return False
		else:
			return func(sides)

	return wrapper

@check_triangle
def is_equilateral(sides):
    return len(set(sides)) == 1



@check_triangle
def is_isosceles(sides):
 	return len(set(sides)) == 2

@check_triangle
def is_scalene(sides):
	return len(set(sides)) == 3

