haritha ={'id':8,'title':'Pythonlab'}
satya={'id':18,'working_on_lab':True}
yamini={'id':28,'email':'pyhtonlab@gmail.com'}
print("Individual dictonories")
print("haritha:{}".format(haritha))
print("satya:{}".format(satya))
print("yamini:{}".format(yamini))


#Non-pythonic procedural way
m1={}
for k in haritha:
    m1[k]=haritha[k]
for k in satya:
    m1[k]=satya[k]
for k in yamini:
        m1[k] = yamini[k]
#classic pyhtonic way
m2=haritha.copy()
m2.update(satya)
m2.update(yamini)

#via dictionary comprehensions
m3={k:v for d in[haritha,satya,yamini] for k,v in d.items()}

#python 3.5+ pythonic way
m4={**haritha,**yamini,**satya}
print(m1)
print(m2)
print(m3)
print(m4)