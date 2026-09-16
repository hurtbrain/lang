import math
def add(array):
  return(math.fsum(array))
def sub(array):
  result = reduce(lambda x, y: x - y, array)
  return(result)
def mul(array):
  return(math.prod(array))
def div(first, second):
  if second >= 1:
    return(first / second)
  elif second < 0:
    return(mul(first,second))
  else:
    return("I cant Divide by 0")
