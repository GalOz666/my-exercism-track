import pprint
import typing

def if_ten_non_unique(array: list):
	counter = []
	copy_list = list
	for idx, num in enumerate(array):

		if num ==10:
			counter.append(f"{num} at index {idx} equals 10")

		elif idx + 1 == len(array):
			continue

		else:
			for nextnum in copy_list[idx+1::]:
				if num + nextnum == 10:
					counter.append(f'{num} + {nextnum} = 10')


	pprint.pprint([line for line in counter])

if_ten_non_unique([1,9,3,4,10,5,6,7,8,10])