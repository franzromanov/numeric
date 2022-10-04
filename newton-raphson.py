#newton-raphson.py

from sympy import *
import math
from tabulate import tabulate

#
#

def nwrn(xinp,iter_,dumper,data1,datasummer):

	#initiateVarAndFunc
	count=iter_+1
	x1val=xinp
	x1=symbols("x1")
	#x2=symbols("x2")

	#ur_function
	f=x1**3-75


	#TakeTheDerivative

	#display
	#print(df)

	#calculation
	df=diff(f,x1)
	#print(df)
	m=f/df
	fx1=float(f.subs(x1,x1val))

	x2=x1val-float(m.subs(x1,x1val))
	
	#error_calc
	error1=abs(0-fx1)#respect to zero

	#iteration_stop
	dump=dumper

	if dump==fx1:
		exit()
	else:
		pass

	print(f"""							
===================================================================================
			GAP BETWEEN	{count}
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		""")

	#build_tableAndDisplay
	data1=data1
	datasum=datasummer
	data1.append(count)
	data1.append(fx1)
	data1.append(x2)
	data1.append(error1)
	datasum.append(data1)
	#print(datasum)
	header=["count","f(x)","x","error"]
	print(tabulate(datasum, headers=header, tablefmt="grid"),"\n")


	nwrn(x2,count,fx1,[],datasum)

#
#
#
#
#
#

try:
	xinp=float(input("X value:"))
	nwrn(xinp,0,0,[],[])
except:
	pass
print("DONE")