from triangle import triangle

def test_invalid():
	assert triangle(-1, 0, 0) == -1

def test_invalid2():
	assert triangle(1, 1, 2) == -1
