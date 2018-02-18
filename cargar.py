import equipoideal.models
import time
import datetime

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
		mod=equipoideal.models.Partido(equipo1=eq1,equipo2=eq2
		,fecha=fixdate(dat),Grupo=grpo)
		print ('no se agrego'+ eq1 +"   -   "+eq2+"   -   "+grpo)
		try:
			mod.save()
		except:
			print ('no se agrego'+ eq1 +"   -   "+eq2+"   -   "+grpo)
