from django.shortcuts import render
from datetime import datetime

#1ra vista del primer template
def inicio(request):
    contexto =  {
        'titulo': 'Mi blog Personal',
        'fecha': datetime.now(),
        'num_posts': 3
    }
    return render(request, 'blog/inicio.html', contexto)

# 2da vista del segundo template

def sobre_mi(request):
    contexto =  {
        'nombre': 'Miguel Brown',
        'profesion': 'Desarrollador & DevOps',
        'edad': 30,
        'habilidades': ['Python', 'Django', 'PostgreSQL', 'HTML', 'CSS', 'Ninja en S']
    }
    return render(request, 'blog/sobre_mi.html', contexto)



# 3ra vista del tercer template

def posts(request):
    contexto = {
    'posts': [
            {'titulo': 'Mi primer post en Django', 'fecha': '2026-05-16'},
            {'titulo': 'Django es increíble', 'fecha': '2026-05-15'},
            {'titulo': 'Templates explicados', 'fecha': '2026-05-14'},
            {'titulo': 'El  Problema de las Ss', 'fecha': '2026-05-18'},
        ]
    }
    return render(request, 'blog/posts.html', contexto)

def gatitos(request):
    contexto = {
        'gatito': 'miaumiau',
        'perro': 'WuauWuau'
    }
    return render(request, 'blog/gatitos.html', contexto)