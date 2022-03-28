# @some_decorator
# def simple_function():
# Do simple stuff
# return something

def Jello(name='Jose'):
	print('the Hello function has been run {}'.format(name))

	def greet():
		return " This is inside the greet()"

	def welcome():
		return " This is inside the welcome()"

	if name == 'Jose':
		return greet
	else:
		return welcome


x = Jello(name='Eduard')
print(x())


def hello():
	return ' Hi Jose'


def other(func):
	print('Some Other code')
	# Assume that func passed in is a functions!
	print(func())


other(hello)


def new_decorator(func):
	def wrap_func():
		print('cualquier cosa de la funcion')

		func()

		print(' Code here, after executing func()')

	return wrap_func

@new_decorator
def func_need_decorator():
	print('Please decorate me!!!')

# se puede llamar de igual forma un decorador asi
#func_need_decorator = new_decorator(func_need_decorator)

func_need_decorator()
