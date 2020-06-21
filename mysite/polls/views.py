# Create your views here.
from django.http import HttpResponse


zahl1 = 1
zahl2 = 10.45
zahl3 = zahl1 + zahl2

print(str(zahl3))
print("Das ist ja super hier")

style = "<style> #supertext {color: blue;}</style>"

super = "<div id='supertext'> Das ist ja super hier....... </div>"

def foo(request):
    return HttpResponse(style + "Hello World! " + str(zahl3) + " " + super.upper() + super.lower())

	
