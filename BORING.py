import time

a = 0

def abc(b):
  if len(b) <= 3:
    return  b[len(b)-3:len(b)]
  else:
    c = b[len(b)-3:len(b)]
    cc = abc(b[0:len(b)-3])+" "+c
  return cc

while True:
  a += 10000
  time.sleep(10**-320) 
  print(abc(str(a)))
  