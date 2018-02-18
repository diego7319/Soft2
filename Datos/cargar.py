import equipoideal.models
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
