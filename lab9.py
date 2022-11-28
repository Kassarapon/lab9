def binarysearch(data, find):
    l = 0
	h = len(data) - 1

	while h - l > 1:
		mid = (h + l) // 2
		if data[mid] < find:
			l = mid + 1
		else:
			h = mid

	if data[l] == find:
        print("Binary search", find, "was found at index", l)
	elif data[h] == find:
		print("Binary search", find, "was found at index", h)
	else:
		print("Binary not found")
		
def linearsearch(data, key):
    for i in range(len(data)):
        if data[i] == key:
            return i
    return -1

data = [7, 10, 12, 14, 16, 20, 29, 37]

find = 14
binarysearch(data, find)

find = 29
binarysearch(data, find)

key  = 14
linearsearch(data, key)
index = linearsearch(data, key)
if index < 1:
    print('\nLinear search {} was not found'.format(key))
else:
    print('\nLinear search {} was found at index {}'.format(key, index)) 

key  = 29
linearsearch(data, key)
index = linearsearch(data, key)
if index < 1:
    print('Linear search {} was not found'.format(key))
else:
    print('Linear search {} was found at index {}'.format(key, index))
    
