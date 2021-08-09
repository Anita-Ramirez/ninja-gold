from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime,localtime

def index(request):
    return render (request,"index.html") #siempre debo poner el index del html o si n no me toma
def dinero(request):
    if not "frase" in request.session:
        request.session['frase'] = []
    if "cont" in request.session:
        if request.POST['oro'] == 'farm':
            numero_aleatorio = random.randint(10,20)
            request.session['cont'] += numero_aleatorio
            diccionario = { 'texto': f'¡Ganaste {numero_aleatorio} monedas de oro!', 'color': 'verde'}
            request.session['frase'].append(diccionario)
        if request.POST['oro'] == 'cave':
            numero_aleatorio = random.randint(5,10)
            request.session['cont'] += numero_aleatorio
            diccionario = { 'texto': f'¡Ganaste {numero_aleatorio} monedas de oro!','color': 'verde'}
            request.session['frase'].append(diccionario)
        if request.POST['oro'] == 'house':
            numero_aleatorio = random.randint(2,5)
            request.session['cont'] += numero_aleatorio
            diccionario = { 'texto': f'¡Ganaste {numero_aleatorio} monedas de oro!','color': 'verde'}
            request.session['frase'].append(diccionario)
        if request.POST['oro'] == 'casino':
            a = random.randint(1,2)
            if a == 1:
                numero_aleatorio = random.randint(50,60)
                request.session['cont'] += numero_aleatorio
                diccionario = { 'texto': f'¡¡¡Ganaste {numero_aleatorio} monedas de oro!!!', 'color': 'verde', 'date': strftime("%H:%M %p", localtime()) }
                request.session['frase'].append(diccionario)
            else:
                numero_aleatorio = random.randint(50,60)
                request.session['cont'] -= numero_aleatorio
                diccionario = { 'texto': f'¡¡¡Perdiste {numero_aleatorio} monedas de oro!!!', 'color': 'rojo', 'date': strftime("%H:%M %p", localtime()) }
                request.session['frase'].append(diccionario)
    else: 
        request.session['cont'] =0
    return redirect ("/")
def restaurar(request):
        request.session['cont'] =0
        request.session['frase'] = []
        return redirect("/")


    


