#bisection_algorithm
import math

#start_ui

print("""
<===>[BISECTION_METHOD]<===>


>>>TABLES<<<
""")

#casting

#const
E=0

#x_value
x1_a=float(input("x1 value:"))
x2_a=float(input("x2 value:"))


#iteration

def bisection(a,b,count,ytdump):


	x1=a
	x2=b
	ytbag=ytdump
	################~~THE FUNCTION~~#################
	#y_value
	y1=((120*math.pi)/((math.sqrt(2.2))*((x1/1.588)+1.393+(0.667*(math.log((x1/1.588)+1.44))))))-50
	y2=((120*math.pi)/((math.sqrt(2.2))*((x2/1.588)+1.393+(0.667*(math.log((x2/1.588)+1.44))))))-50
	#################################################

	#calculation

	#bisection_method
	xt=(x1+x2)/2

	################~~THE FUNCTION~~#################
	yt=((120*math.pi)/((math.sqrt(2.2))*((xt/1.588)+1.393+(0.667*(math.log((xt/1.588)+1.44))))))-50
	#################################################

	check=yt*y1
	count_a=count+1
	error=yt-E
	#display_ui


	
	if ytbag-yt!=0 :

		print(f"""

iteration_number:{count}

X1={x1}		
X2={x2}
Xt={xt}	
Y1={y1}
Y2={y2}		
Yt={yt}
error={error}
Yt*Y1={check}

			""")
		if yt*y1<0:
			x2=xt
			x1=x1

		if yt*y1>0:
			x1=xt
			x2=x2


		bisection(x1,x2,count_a,ytbag)




#run
#try:
bisection(x1_a,x2_a,0,0)
#except:
#pass

















