import polla.models
import time
import datetime
import random

def ingresardato():
	corpus = open('a.csv',encoding='utf-8').readlines()
	for i in corpus:
		a=i.split(",")[0]
		b=i.split(",")[1]
		mod=equipoideal.models.JugadorPais(nombre=a,pais=b)
		try:
			mod.save()
		except:
			print ('no se agrego'+ a +"   -   "+b)

def fixdate(fech):
	p=fech.split("/")
	y,m,d=p[2],p[1],p[0]
	return (y+"-"+m+"-"+d)

def ingresarpartidos():
	corpus = open('d.csv',encoding='utf-8').readlines()
	cont1=0
	cont2=0
	gr=['A','B','C','D','E','F','G','H']
	for i in corpus:
		m1=random.uniform( 1, 7 )
		m2=random.uniform( 1, 7 )
		m3=random.uniform( 1, 7 )
		grpo=""
		cont1=cont1+1
		if cont1==6:
			grpo=gr[cont2]
			cont1=0
			cont2=cont2+1
		else:
			grpo=gr[cont2]
		linea=i.split(",")
		eq1=linea[1];
		eq1=eq1.split(" ")[1]
		eq2=linea[3];eq2=eq2.split(" ")[1]
		dat=linea[0]
		mod=polla.models.Partido(equipo1=eq1,equipo2=eq2
		,fecha=fixdate(dat),Grupo=grpo,monto1=m1,monto2=m2,montoempate=m3)
		print ('no se agrego'+ eq1 +"   -   "+eq2+"   -   "+grpo)
		try:
			mod.save()
		except:
			print ('no se agrego'+ eq1 +"   -   "+eq2+"   -   "+grpo)
