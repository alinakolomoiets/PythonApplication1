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
#from random import*
#p=0
#n=0
#N=randint(1,10)
#for i in range(N):
#	Arv=int(input("Sisesta arv"))
#	if Arv>0:
#		p+=1
#	elif Arv<0:
#		n+=1
#print("Neg:"+str(n))
#print("Pos:"+str(p))
#print("Nullid:"+str(N-n-p))
#3 Вводят 8 чисел. Найти их произведение (только положительных).
#korrutis=1
#for i in range(8):
#	arv=float(input("Arv:"))
#	if arv>0:
#		korrutis*=arv
#	print(korrutis)
#9 В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
#p=1.03
#S=int(input("Sisesta summa:"))
#N=int(input("Mitu aastat:"))
#for aasta in range(1,N+1):
#	S*=p
#	print(aasta,"aasata pärast tulemus on ",round(S,2))
#13.Найти все натуральные числа от 100 до 1000 кратные 7. И посчитать их колличество и сумму.
#from random import*
#k=0
#summa=0
#for i in range(100,1001):
#	if i % 7==0:
#		print(i)#ekraanile
#		k+=1#kogus suurendame
#		summa+=i# i-de summa, mis jagatakse 7-ga
#print("Arvude summa:",summa)
#print("Kogus:",k)
#15.Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
#0 1 2 3 4 5 6 7 8 9
#0 1 2 3 4 5 6 7 8 9
#...................
#0 1 2 3 4 5 6 7 8 9
#from random import*
#for rjady in range(10):
#	for stroka in range(10):
#		print(stroka,end=" ")
#	print()
#16.Напишите программу, печатающую столбик строк такого вида:
#1 0 0 0 0 0 0 0 0
#0 2 0 0 0 0 0 0 0
#0 0 3 0 0 0 0 0 0
#0 0 0 4 0 0 0 0 0
#0 0 0 0 5 0 0 0 0
#0 0 0 0 0 6 0 0 0
#0 0 0 0 0 0 7 0 0
#0 0 0 0 0 0 0 8 0
#0 0 0 0 0 0 0 0 9
#from random import*
#for rjady in range (1,10):
#	for stroka in range(1,10):
#		if rjady==stroka:
#			print(stroka,end=" ")
#		else:
#			print("0",end=" ")
#	print()
#29.Напишите программу, печатающую столбик строк такого вида:
#x 0 0 0 0 0 0 0 0
#x x 0 0 0 0 0 0 0
#x 0 x 0 0 0 0 0 0
#x 0 0 x 0 0 0 0 0
#x 0 0 0 x 0 0 0 0
#x 0 0 0 0 x 0 0 0
#x 0 0 0 0 0 x 0 0
#x 0 0 0 0 0 0 x 0
#x 0 0 0 0 0 0 0 x
#from random import*
#for rjady in range (1,10):
#	for stroka in range(1,10):
#		if rjady==stroka:
#			print("x",end=" ")
#		elif stroka==1:
#			print("x",end="")
#		else:
#			print("0",end=" ")
#	print()
#from random import*
#loom=input("Kupi slona!")
#while loom.title()!="Slon":#upper () ;lower()
#	loom=input("Vse govorjat"+loom+"!A ty kupi!!!")
#print("Molodets!!!")
#28Реализуйте "мини лотерею". Пусть компрьютер "задумает число", а пользователь его должен отгадать. В конце сообщив количество попыток.
#from random import*
#print("Loterii".center(50,"*"))
#count=0#число введенное пользователем 
#counte=0#счетчик попыток
#x=randint(1,70)
#int(input("Отгадай число:"))
#input("Введи свое имя :")
#while count()!=x:
#    count=int(input("Отгадай число "+"a"))
#    counte=counter+1
#    if count>x:
#        print("Число должно быть меньше")
#    elif count<x:
#        print("Число должно быть больше")
#    else:
#        print("Ты угадал число за"+str(counte)+"попыток")
from random import*
from math import*
from keyboard import*
print("Teadmiste kontroll".center(60,"*"))
tase=0
while tase not in [1,2,3]:
	try:
		tase=int(input("Vali tase(1,2,3):"))

	except ValueError :
		print("Ainult 1,2 või 3!")
	except:
		print("Noh!,Ainult 1,2 või 3")
if tase==1:
	min=2
	max=10
	tehed=["+","-"]
elif tase==2:
	min=2
	max=15
	tehed=["+","-","*"]
elif tase==3:
	min=2
	max=20
	tehed=["+","-","*","/"]
p=0
kokku=0
while True:
	v=input("Kas jätkame? esc-lõpp, space-jätkame")
	if v=="stop":
		break
	else:
		kokku+=1
		a=randint(min,max)#!=0 kui//
		b=randint(min,max)#!=0
		tehe=choice(tehed)#выбирает действие,работает вместе с random
		if tehe =="//":
			while b==0:
				try:
					b=randint(min,max)
				except:
					ValueError
		print(f"{a}{tehe}{b}=", end=" ")
		vaja=int(eval(str(a)+tehe+str(b)))#round()?
		vastus=""
		while type (vastus)!=int:
			try:
				vastus=int(input("="))#!=str
			except ValueError:
				print("Vaja int!!!")
		if vastus ==vaja:
			print("Õige vastus!")
			p+=1
		else :
			print("Mõtle veel!")
print("Kokku ülesandeid oli:",kokku)
print("Õige vastused :",p)
K=(p/kokku)*100
if K<60:
	print("Hinne 2")
elif 60<=K<=75:
	print("Hinne 3")
elif 75<=K<=90:
	print("Hinne 4")
elif K>=90:
	print("Hinne 5")