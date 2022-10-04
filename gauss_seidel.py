#gauss_seidel
import os

try:
	import math
	from tabulate import tabulate
	from sympy import *

except:
	os.system("pip install tabulate")
	os.system("pip install sympy")
	os.system("pip3 install numpy")

def gaussseidel(xv,yv,zv,iter_,data1,datasummer):
	
	#IntiationVarAndFunc
	
	count=iter_+1
	xval=float(xv)
	yval=float(yv)
	zval=float(zv)

	x= float((220+15*zval)/20)
	y= float((20*zval)/35)
	z= float((20*y+15*x)/55)

	data1=data1
	datasum=datasummer
	data1.append(count)
	data1.append(x)
	data1.append(y)
	data1.append(z)
	datasum.append(data1)
	#print(datasum)
	header=["count","x","y","z"]
	print(tabulate(datasum, headers=header, tablefmt="grid"),"\n\n")
	
	if x==xval and y==yval and z==zval:
		exit()
	else:
		gaussseidel(x,y,z,count,[],datasum)


try:
	xinp=float(input("X INPUT: "))
	yinp=float(input("Y INPUT: "))
	zinp=float(input("Z INPUT: "))
	gaussseidel(xinp,yinp,zinp,0,[],[])
except:
	pass

print("JOB DONE")

