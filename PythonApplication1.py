#p=0
#for i in range(15):#i=0,1,2,3....
#	A=0
#	while type(A)!=float:
#		try:
#			A=float(input(f"Sisesta"+ str(i+1)+ "arv"))
#		except ValueError:
#			print("Oi")
#	if A==round(A):
#		p+=1
#		print(str(A)+"on täisarv")
#	else:
#		print(str(A)+"ei ole täisarv")
#print(str(p)+"Täisarvud")
#4
#Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
#for i in range(10,21):
#	print(i**2)
#7
#from random import*
#A<B
#A=randint(10,100)
#B=randint(100,1000)
#print("A="+str(A))
#print("B="+str(B))
#K=int(input("K:"))
#for i in range(A,B+1):
#	if i%K==0:print(i)
#6С клавиатуры вводятся N чисел. Составьте программу, которая определяет количество отрицательных, количество положительных и количество нулей среди введенных чисел.   Значение N вводится с клавиатуры.
from random import*
p=0
n=0
N=randint(1,10)
for i in range(N):
	Arv=int(input("Sisesta arv"))
	if Arv>0:
		p+=1
	elif Arv<0:
		n+=1
print("Neg:"+str(n))
print("Pos:"+str(p))
print("Nullid:"+strN-n-p))


