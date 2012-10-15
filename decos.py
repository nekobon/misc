def semi_singleton(cls):
	'''
	Not exactly singleton but semi-singleton decorator function.
	Unlike singleton, this allows multiple objects of the same class; however,
	this does not allow making multiple objects if parameters in init() are the same.
	Use this to decorate a class.
	'''
	objects = {}
	def get_object(*args, **kwargs):
		vals = args + tuple(kwargs.values())
		if (cls, vals) not in objects:
			objects[(cls, vals)] = cls(*args, **kwargs)
		return objects[(cls, vals)]
	return get_object

def cacher(function):
	'''
	A very simple memoizing decorator to cache outputs.
	For python 3.2+ there is a built-in fast cache: @functools.lru_cache
	'''
	cache = {}
	def cached(*args):
		try:
			return cache[args]
		except KeyError:
			cache[args] = function(*args)
			return cache[args]
	return cached
