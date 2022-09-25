# a = 123
# b = 1.23
# print (type(a))
# print (type(b))
# s = 'hello world'
# print(s) # вывод строки

for x in range(2):
	    for y in range(2):
	        for z in range(2):
	            if not (x == z or x <= y and z):
	                print(x, y, z)