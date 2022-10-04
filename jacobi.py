#jacobi_iteration_method
import os,sys

try:
	from tabulate import tabulate
except:
	os.system("pip install tabulate")
	os.system("pip3 install numpy")

sys.setrecursionlimit(10**6)


def jacobi(xv,yv,zv,nv,iter_,data1,datasummer):
	#IntiationVarAndFunc
	count=iter_+1
	xval=float(xv)
	yval=float(yv)
	zval=float(zv)
	nval=float(nv)
	x= float(-8+yval-(2*zval)+nval)
	y= float((20+(2*xval)+(3*zval)-(3*nval))/(2))
	z= float(-2-xval-yval)
	n= float((4-xval+yval-(4*zval))/3)


	#buildtabelAndDisplay
	data1=data1
	datasum=datasummer
	data1.append(count)
	data1.append(x)
	data1.append(y)
	data1.append(z)
	data1.append(n)

	datasum.append(data1)
	header=["count","x","y","z","n"]
	print(tabulate(datasum, headers=header, tablefmt="grid"),"\n\n")


	#exitcondition
	if (x-abs(xval))>=0 and (y-abs(yval))>=0 and abs(z-abs(zval))>=0 and abs(n-abs(nval))>=0:
		exit()
	else:
		jacobi(x,y,z,n,count,[],datasum)



try:
	xinp=float(input("X INPUT: "))
	yinp=float(input("Y INPUT: "))
	zinp=float(input("Z INPUT: "))
	ninp=float(input("N INPUT: "))
	jacobi(xinp,yinp,zinp,ninp,0,[],[])
except:
	pass

print("JOB DONE")
