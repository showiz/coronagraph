import io


import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg
from random import sample

from .models import Chile, Regions, Page, World

# Import Numpy
import numpy as np

# Force Integer Axis
from matplotlib.ticker import MaxNLocator

# Calling the database of Regions
from core.models import Regions

def pagedata(request):
    page = Page.objects.all()
    return render(request, "core/base.html", {'page':page})



def home(request):
    countries = World.objects.all()
    chile = Chile.objects.all()
    
    return render(request, "core/home.html", {'countries':countries, 'chile':chile,})


def plot(request):
    from core.models import ChileData
    datos = ChileData.objects.all()
    days = len(datos)
    
    # x (axis) = Days 
    x = np.arange(days)
    
    # y (axis) = Infected
    y_cl = []
    for i in datos:
         y_cl.append(i.name)
    print(y_cl)

    #x = np.linspace(1, 25, 25, endpoint=True, dtype=None) 
    #y_cl = [1,3,4,5,7,11,13,17,23,33,43,61,75,156,201,238,342,434,537,632,746,922,1142,1306,1610,1909,2139]
    #y_es = [166,228,282,401,525,674,1231,1695,2277,3146,5232,6391,7988,9942,11826,14769,18077,21571,25496,29909,35480]
    #y_it = [2502,3089,3858,4636,5883,7375,9172,10149,12462,15113,17660,21157,24747,27980,31506,35713,41035,47021,53578,59138,63927]
    
    
        

   
    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()


    # Creamos los ejes
    axes = f.add_axes([0.15, 0.15, 0.8, 0.75]) # [left, bottom, width, height]
    
    

    plt.plot(x, y_cl, 'o--', label='Chile',color='r', alpha=1)


    # Axes names
    axes.set_xlabel("Días")
    axes.set_ylabel("Contagiados")

    # axes.set_yscale('log')
    axes.set_title("Gráfico de contagios en CHILE")

    # Grids
    plt.grid(axis='x', color='0.95')
    plt.grid(axis='y', color='0.95')

    # Legend
    plt.legend(title='Parámetros:')

    '''plt.subplot(2, 1, 1)
    plt.plot(x, y_cl, 'o--', label='Chile', color='r', alpha=1)
    plt.title('Gráficos por País')
    plt.ylabel('Contagiados')

    plt.subplot(2, 1, 2)
    plt.plot(x, y_es, 'o--', label='España', color='b', alpha=1)
    plt.xlabel('días')
    plt.ylabel('Contagiados')'''

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

def regiones(request):
    regions = Regions.objects.all()
    return render(request, "core/regiones.html", {'regions':regions})

def regions(request):
    regions = Regions.objects.all()

    #AXIS
    y = []
    x = []
    for i in regions:
        y.append(i.name)
    print(y)

    for n in regions:
        x.append(n.infected)
    print(x)


    # Creamos los datos para representar en el gráfico
    #x = np.arange(21)
    
    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()


    # Creamos los ejes
    axes = f.add_axes([0.18, 0.15, 0.8, 0.75]) # [left, bottom, width, height]
    
    

    #plt.plot(x, y_val, 'o--', label='Chile',color='r', alpha=1)
    plt.barh(y, x, align='center', alpha=0.5)


    # Axes names
    axes.set_xlabel("Cantidad de contagios")
    #axes.set_ylabel("Contagiados")
    axes.set_title("Gráfico de contagios en REGIONES")

    # Grids
    plt.grid(axis='x', color='0.95')
    #plt.grid(axis='y', color='0.95')

    # Legend
    #plt.legend(title='Parámetros:')

    '''plt.subplot(2, 1, 1)
    plt.plot(x, y_cl, 'o--', label='Chile', color='r', alpha=1)
    plt.title('Gráficos por País')
    plt.ylabel('Contagiados')

    plt.subplot(2, 1, 2)
    plt.plot(x, y_es, 'o--', label='España', color='b', alpha=1)
    plt.xlabel('días')
    plt.ylabel('Contagiados')'''

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response
