# Learning from https://realpython.com/primer-on-python-decorators/
# Jonathan Salazar
# Decoradores búsqueda binaria
# 2020-08-18

import time
import functools


class SlowDown(object):

	def __init__(self, funct_name):
		functools.update_wrapper(self, funct_name)
		self.function_name = funct_name

	def __call__(self, *args, **kwargs):
		self.function_name(*args, **kwargs)
		print(f"Sleeping time comes...")
		time.sleep(1)
		print(f"Waking up time...")
		return self.function_name


@SlowDown
def countdown(from_number):
	print(f"Hola {from_number}")
