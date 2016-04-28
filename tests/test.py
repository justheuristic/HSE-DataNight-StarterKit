def test():
	result = 0
	with open("../answer.txt", "r") as f:
		result = float(f.read())
		if result > 0.5:
			return True
		else:
			return False
