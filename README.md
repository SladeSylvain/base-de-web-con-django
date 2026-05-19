# 🚀 Django Architecture: Routes, Views & Contexts

Este repositorio contiene un proyecto práctico en Django diseñado para entender el flujo de datos entre las solicitudes del navegador, el enrutamiento, la lógica de control y el renderizado de plantillas.

---

## 📈 Proceso de Implementación Paso a Paso

### 1. Modelado de la Lógica y Datos (`views.py`)
Se crearon funciones controladoras para procesar las peticiones de cada sección (`inicio`, `sobre_mi`, `posts`, `gatitos`). La lógica se centró en la estructura de datos nativos de Python (strings, listas y diccionarios) para enviarlos como colecciones de información dinámica a la interfaz.

### 2. Configuración del Enrutamiento (`urls.py`)
Se implementó el sistema de mapeo de URLs (`URLconf`) importando las vistas locales y registrando cada endpoint mediante la función `path()`, estableciendo una estructura de navegación limpia.

### 3. Diagnóstico y Corrección del Error 404
Al realizar las pruebas de navegación hacia `/posts/`, el servidor arrojó un fallo de coincidencia. Se detectó que la ruta interna estaba definida en singular (`post/`). Se procedió a refactorizar el código para unificar los criterios a plural.

### 4. Resolución de Conflictos con Plantillas (`TemplateDoesNotExist`)
Tras corregir la URL, el motor de Django no lograba localizar el recurso físico en el disco porque el archivo HTML mantenía el nombre en singular (`post.html`). Se renombró el archivo a `posts.html` en el directorio de templates para sincronizar el renderizador.

---

## 💡 Aprendizajes Clave (Lo que aprendí)

* **Consistencia Estricta en Django:** Comprendí que Django requiere una coincidencia exacta de caracteres entre lo que el usuario digita en el navegador, lo que busca la vista y el nombre del archivo HTML en el disco. Un solo carácter de diferencia (como una "s") rompe el flujo.
* **Estándares de la Industria (Plural vs. Singular):** Aprendí que por convención arquitectónica, las rutas que devuelven colecciones o listados de elementos siempre deben declararse en plural (`/posts/`), reservando el singular para elementos únicos mediante parámetros dinámicos.

---

## 🎯 Aplicación Profesional (Para qué me servirá)

* **Depuración Eficiente (Troubleshooting):** Ahora puedo interpretar los *tracebacks* de Django de manera autónoma. Identificar la diferencia entre un error de enrutamiento (404) y uno de localización de archivos (`TemplateDoesNotExist`) reduce drásticamente el tiempo de desarrollo.
* **Preparación para APIs y CRUDs:** Esta base es fundamental para los siguientes módulos del bootcamp. Entender cómo viaja un diccionario de contexto hacia un template me facilitará la integración con Bases de Datos (PostgreSQL/ORMs) y el consumo de endpoints en proyectos Full Stack.

---

# 🐍 Configuración de Proyecto Django

Guía paso a paso para crear y configurar un proyecto Django con una aplicación de blog.

---

## 1. Crear el entorno virtual

```bash
python -m venv venv
```

## 2. Activar el entorno virtual (Windows)

```bash
.\venv\Scripts\activate
```

## 3. Instalar Django

```bash
pip install django
```

## 4. Crear la estructura del proyecto base

> 📁 Se crea la carpeta `config` como directorio principal del proyecto.

```bash
django-admin startproject config .
```

## 5. Crear la aplicación del blog

```bash
python manage.py startapp blog
```

## 6. Crear la estructura de directorios para las plantillas (Templates)

> 📌 Se usa `mkdir -p` para estructurar el espacio de nombres (**Namespacing**).

```bash
mkdir -p blog/templates/blog
```

## 7. Crear los archivos HTML base para las vistas

```bash
touch blog/templates/blog/inicio.html
touch blog/templates/blog/sobre_mi.html
touch blog/templates/blog/posts.html
touch blog/templates/blog/gatitos.html
```

## 8. Aplicar las migraciones iniciales a la Base de Datos

```bash
python manage.py migrate
```

## 9. Crear el Superusuario administrativo

> 🔐 Permite acceder al panel de control en `/admin`.

```bash
python manage.py createsuperuser
```

## 10. Guardar las dependencias instaladas

> ✅ Buena práctica obligatoria para reproducir el entorno.

```bash
pip freeze > requirements.txt
```

## 11. Levantar el servidor de desarrollo

```bash
python manage.py runserver 8000
```
