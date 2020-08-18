# Learning from https://es.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
# Jonathan Salazar
# Algoritmo búsqueda binaria
# 2020-06-26

import random

def BinarySearch():

	steps_number: int = random.randint(1, 4)
	stop_number: int = random.randint(4, 100)

	numbers: list[Any] = list(range(1, stop_number, steps_number))

	min_index: int = 0
	max_index: int = len(numbers) - 1
	found_it: bool = False
	movements: int = 0

	target: int = random.randint(1, len(numbers))

	while max_index >= min_index:

		guess = int((min_index + max_index) / 2)

		if numbers[guess] == target:
			found_it = True
			return f"target is {target}, found after {movements} movements in index {guess}. List is {numbers}."

		elif numbers[guess] < target:
			min_index = guess + 1

		else:
			max_index = guess - 1

		movements+=1

	return f"target {target} was not found, result is {-1}. List is {numbers}."

if __name__ == "__main__": BinarySearch()
