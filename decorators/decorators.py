# Learning from 
#    https://realpython.com/primer-on-python-decorators/
#    & https://www.codementor.io/@dobristoilov/python-class-decorator-part-1-simple-without-configuration-arguments-rsjqa3qi8
#    & https://www.codementor.io/@dobristoilov/python-class-decorator-part-ii-with-configuration-arguments-rv73o8pjn
#
# Jonathan Salazar
# Decoradores
# 2020-08-18

import time
import functools

import urllib3


# Following examples are related on howto create class based decorators
# in some cases we can use functools, which easily let us create a useful 
# decorator, or we can create a more complex class based decorators which 
# lets us pass parameters as needed.

class SlowDown(object):
	"""This class based decorator uses the functools module, which is useful
	if you are planning to create a simple decorator, with no params.

	It is very important to set these two methods: constructor, and callable

	__init__ and __call__

	This is the first example
	"""

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
	"""This class based decorator uses the functools module, which is useful
	if you are planning to create a simple decorator, with no params.

	It is very important to set these two methods: constructor, and callable

	__init__ and __call__

	This is the second example
	"""

	def __init__(self, f_name):
		functools.update_wrapper(self, f_name)
		self.function_name = f_name
		self.count_calls = 0


	def __call__(self, *args, **kwargs):
		self.count_calls += 1
		print(f"Call {self.count_calls} of {self.function_name.__name__!r}")
		return self.function_name(*args, **kwargs)


class CacheCalls(object):
	"""This class based decorator uses the functools module, which is useful
	if you are planning to create a simple decorator, with no params.

	It is very important to set these two methods: constructor, and callable

	__init__ and __call__

	This is the third example

	"""

	def __init__(self, f_name):
		functools.update_wrapper(self, f_name)
		self.function_name = f_name
		self.cache_calls = {}


	def __call__(self, *args, **kwargs):
		cache_key = args + tuple(kwargs.items())
		if cache_key not in self.cache_calls:
			self.cache_calls[cache_key] = self.function_name(*args, **kwargs)
		return self.cache_calls[cache_key]


class ValidateJSON(object):
	""" Class based decorator with or without params, we prepare
	the constructor for receiving params as needed or not.

	As the examples above, this needs to set two important methods

	__init__ (to set initial config) and __call__ (last one to make this callable)

	The call method also is prepared to receive the params (through the wrapper 
	funct) coming from the decorated function, and also we can use params that 
	comes from the decorator constructor.
	"""

	def __init__(self, *args, **kwargs):
		# print('__init__', args, kwargs)
		self.args = args
		self.kwargs = kwargs

	def __call__(self, f_name):

		def wrapper(*args, **kwargs):
			# print('__call__', args, kwargs)
			print(f"Preprocessing {self.args}, {self.kwargs}")
			if args:
				print(f"wrapper: {args}")
			r = f_name(*args, **kwargs)
			print(f"Postprocessing", r)
			return r
		return wrapper


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


# Even we can create our own cache decorator (We created this just as an example)
#@CacheCalls
# It is better to use the one provided by the functools
@functools.lru_cache(maxsize=4)
#@CountCalls
def fibonacci(num):
	print(f"Calculating fibonacci({num})")
	if num < 2:
		return num
	return fibonacci(num - 1) + fibonacci(num - 2)


_REQUEST_DATA = {
	"username": "Jonas", 
	"password": "password"
}
name = "Jonas"

# So you can choose to send N params or/and keyworks
#@ValidateJSON("student_id")
# Or you just can call the decorator without params
@ValidateJSON()
def update_grade(*args, **kwargs):
	print('call my_function', args, kwargs)


