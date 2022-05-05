'''Sfutools module:A set of simple, fast and useful functions and class that can help you programme.

*The function 'timesit' and 'timeit' should be used as decorators.*'''



__all__=['timesit', 'timeit', 'FastCreateSelf', 'const', 'Timer']


class CannotUseError(BaseException):
	
	def __init__(self,name,moduleName):
		self.__name=name
		self.__moduleName=moduleName
		
	def __str__(self):
		return 'Cannot use %s, because module %s can\'t be imported.'%(self.__name,self.__moduleName)
		

#try import modules to ensure this module won't raise ImportError.'

#When a necessary module can't be imported properly,functions or classes needing the module can't be used.
_errorImport=[]
try:
	import time as _time

except ImportError:
	_errorImport.append('time')
	
try:
	from abc import ABCMeta as _ABCMeta
	
except ImportError:
	
	_errorImport.append('abc.ABCMeta')
	
try:
	from abc import abstractmethod as _abstractmethod
	
except ImportError:
	_errorImport.append('abc.abstractmethod')
	
try:
	from os import system as _system
	
except ImportError:
	_errorImport.append('system')



def timesit(iterations):
	'''A decorator that can measure the time taken for the program to run a custom number of times.
	
	Usage:
		
		@timesit(iterations)
		def function(...):
			...
			
		print(function(...))
		
		
	e.g.
	
	@timesit(100)
	def output(char):
		print(char)
		
	print(output('a'))
	
	#result:a
	a
	a
	.
	.
	.
	a
	0.0001...s(the time the function runs 100 times takes)'''
		
		
	
	if 'time' in _errorImport:
		raise CannotUseError('timesit','time')
	
	
	
	def _timeit(func):
		
		def _timer(*args,**kwargs):
			start=_time.time()
			for _ in range(iterations):
				func(*args,**kwargs)
			time=_time.time()-start
			return time
			
		return _timer
		
	return _timeit
	
	
def timeit(func):
	'''A decorator that can measure the time taken for the program to run once.
	
	Usage:
		
		@timeit
		def function(...):
			...
		
		print(function(...))'''
		
		
	
	if 'time' in _errorImport:
		raise CannotUseError('timeit','time')
	
	
	def _timer(*args,**kwargs):
		
		start=_time.time()
		func(*args,**kwargs)
		time=_time.time()-start
		return time
		
	return _timer
	
	

class FastCreateSelf(metaclass=_ABCMeta):
	'''A class allows you transform outer variable to self.variable.
	
	*This class is an abstract class,so you can't directly instantiate it, you must create a class that inherit from this.*
	
	
	Usage:
		class NewClass(FastCreateSelf):
			
			def __init__(self,...):
				super().__init__(,whiteList=...->list,blackList=...->list,...(here we use **kwargs))
				...
			...
			
	e.g.
	a, b = 1, 2
	class C(FastCreateSelf):
		def __init__(self, **kwargs):
			super().__init__(blackList=['b'], **kwargs)
			
	c = C(a, b)
	
	#After that, print c.__dict__
	#result: {'a':1}'''
				
	
	
	if 'abc.abstractmethod' in _errorImport:
		raise CannotUseError('FastCreateSelf','abc.abstractmethod')
	
	
	@_abstractmethod
	def __init__(self,whiteList=None,blackList=None,**kwargs):
		if whiteList!=None:
			whiteList=[whiteItem for whiteItem in whiteList]
		else:
			whiteList=[]
			
		if blackList!=None:
			blackList=[blackItem for blackItem in blackList]
		else:
			blackList=[]
		
		for kwarg in kwargs.items():
			if (whiteList==[] or kwarg[0] in whiteList) and (blackList==[] or kwarg[0] not in blackList):
				self.__dict__[kwarg[0]]=kwarg[1]
		
		
		
		
class _const:
	'''*Do not use _const class, it is just a prebuild of const.Please just use 'const'.*
	
	
	Const provide a simple method to create a constant variable. The constant variable's value cannot be changed, or an error will be raised.
		
		To use the const, you should write down the form like: simpletools.const.xxx = ...
		
		After that, a constant variable will be created.If you want to delete it, just use const.delete(xxx).
		
		
		*The constant variables' names are storaged separated from the common variable, which means you can announce const.xxx and xxx at the same time. But this measure is not recommended.*'''
	
	
	def __setattr__(self,key,value):
		
		if key in self.__dict__:
			
			raise NameError('Const variable %s cannot be changed.'%key)
			
		
		self.__dict__[key]=value
		
		
	def delete(self,key):
		
		if key not in self.__dict__:
			
			raise NameError('%s does not exist.'%key)
			
		
		del self.__dict__[key]
const=_const()



class Timer():
	'''Timer is a common class for you to record time.
	
	To create a timer, use this: 
		timer = Timer()
	
	*After you create a timer, the timer will start automatically.If you want to restart it, just use timer.init(), then it will eliminate the time and start from 0s.*
	
	
	Other usage of Timer:
		
		getTime: Get the time it has recorded.
		
		stop: Stop your timer. When stopping, the timer will not record time until you use timer.resume().
		
		resume: Continue your timer. The timer will start to record time again.'''
		
	
	if 'time' in _errorImport:
		
		raise CannotUseError('Timer', 'time')
	
	
	def __init__(self):
		
		self.__start = _time.time()
		
		self.__time = 0
		
		self.__stop = False
		
		self.__previosTime = 0
		
	
	def getTime(self):
		
		if not self.__stop:
		
			self.__time = _time.time() - self.__start + self.__previosTime
			
		else:
			
			self.__time = self.__previosTime
		
		return self.__time
		
		
	def stop(self):
		
		self.__previosTime += self.getTime()
		
		self.__stop = True
		
		
		
	def resume(self):
		
		self.__start = _time.time()
		
		self.__stop = False
		
		
		
	def init(self):
		
		self.__init__()