# Learning from https://es.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
# Jonathan Salazar
# Algoritmo búsqueda binaria
# 2020-06-26

import random

def main():

	steps_number: int = random.randint(1, 4)
	stop_number: int = random.randint(4, 100)

	numbers: list[Any] = list(range(1, stop_number, steps_number))

	min_index: int = 0
	max_index: int = len(numbers) - 1
	found_it: bool = False
	movements: int = 0

	target: int = random.randint(1, len(numbers))

	print(f"numbers: {numbers}, \nmin_index: {min_index}, \nmax_index: {max_index}, \ntarget: {target}\n")

	while found_it is False:

		if max_index < min_index:
			print(f"The number is not in the list!\n")
			break

		guess = int((min_index + max_index) / 2)

		if numbers[guess] == target:
			print(f"We get the prom based on: guess = int((min_index + max_index) / 2). We found the number: {target} in index {guess}, numbers[guess] is {numbers[guess]}\n")
			found_it = True

		elif numbers[guess] < target:
			print(f"guess is {guess}. We move the min_index = guess + 1. So min_index becomes {guess + 1} and max_index still: {max_index}\n")
			min_index = guess + 1

		else:
			print(f"guess is {guess}. We move the max_index = guess -1. So max_index becomes {guess - 1}, and min_index still: {min_index}\n")
			max_index = guess - 1

		movements+=1
		print(f"movement number: {movements}\n")

	print(f"movements: {movements}, min_value: {min_index}, max_index: {max_index}, target: {target}\n")

if __name__ == "__main__": main()



