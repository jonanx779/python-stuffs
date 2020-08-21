# Learning from https://realpython.com/primer-on-python-decorators/
# Jonathan Salazar
# Decoradores búsqueda binaria
# 2020-08-18

import time
import functools


class SlowDown(object):

	def __init__(self, f_name):
		functools.update_wrapper(self, f_name)
		self.function_name = f_name
		self.rate = 1

	def __call__(self, *args, **kwargs):
		self.function_name(*args, **kwargs)
		print(f"Sleeping time comes...{args}")
		time.sleep(1)
		print(f"Waking up time...")
		return self.function_name


class CountCalls(object):

	def __init__(self, f_name):
		functools.update_wrapper(self, f_name)
		self.function_name = f_name
		self.count_calls = 0


	def __call__(self, *args, **kwargs):
		self.count_calls += 1
		print(f"Call {self.count_calls} of {self.function_name.__name__!r}")
		return self.function_name(*args, **kwargs)


class CacheCalls(object):

	def __init__(self, f_name):
		functools.update_wrapper(self, f_name)
		self.function_name = f_name
		self.cache_calls = {}


	def __call__(self, *args, **kwargs):
		cache_key = args + tuple(kwargs.items())
		if cache_key not in self.cache_calls:
			self.cache_calls[cache_key] = self.function_name(*args, **kwargs)
		return self.cache_calls[cache_key]


# Exercise 1: delaying 1 sec a call
@SlowDown
def countdown(from_number):
	if from_number < 1:
		print("Liftoff!")
	else:
		print(f"Hola {from_number}")
		countdown(from_number - 1)

# Exercise 2: Counting how many calls a fuct receives
@CountCalls
def call_counter():
	print("Calling counter!")

#@CacheCalls
@functools.lru_cache(maxsize=4)
#@CountCalls
def fibonacci(num):
	print(f"Calculating fibonacci({num})")
	if num < 2:
		return num
	return fibonacci(num - 1) + fibonacci(num - 2)




