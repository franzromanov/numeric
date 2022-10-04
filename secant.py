#secant_method
from sympy import *

#
#
#
#
#
#

def secant(xinp1,xinp2,iter_):
	#initiateVarAndFunc
	count=iter_+1
	x1val=xinp1
	x2val=xinp2
	x1=symbols("x1")
	x2=symbols("x2")
	
	###################################
	#ur_function
	f1=2-5*x1+sin(x1)
	f2=2-5*x2+sin(x2)
	###################################

	#calculation
	x3=x2val-((f2.subs(x2,x2val)*(x2val-x1val)/(f2.subs(x2,x2val)-f1.subs(x1,x1val))))
	error=abs(f2.subs(x2,x2val))-0

	#range
	E=0.00000000001

	#if float(f2.subs(x2,x2val))>E:

	#InputValueTo_XAndDisplay
	
	print(f"""
----ITERATION NUMBER {count}----
| f(x1)={f1.subs(x1,x1val)}
| f(x2)={f2.subs(x2,x2val)}
| new_x={x3}
| error={error} [with respect to 0]
--------------------------------

	""")

		#break_loopsAvoidNaN
	if x3==x2val:
		exit()
	else:
		pass

	secant(x2val,x3,count)

#
#
#
#
#
#
#

try:
	x1ask=float(input("X1 VALUE:"))
	x2ask=float(input("X2 VALUE:"))
	secant(x1ask,x2ask,0)
except:
	pass

print("DONE")














