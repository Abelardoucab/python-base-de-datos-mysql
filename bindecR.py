def bindec(num):
   bin=num
   e=0
   d=0
   while bin > 0:
     hh=bin/10
     p=bin-int(hh) * 10
     h=2**e
     d= d +( p * h )
     e=e+1
     bin=int(bin/10)
   return d

        
    