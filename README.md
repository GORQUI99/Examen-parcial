# EmpresasSucursalesDjango
 
¡Por supuesto! Aquí tienes las instrucciones paso a paso:

### Crear un Entorno Virtual, Instalar Django y Dependencias:

1. Abre tu terminal o línea de comandos.

2. Navega al directorio donde quieres crear tu entorno virtual. Por ejemplo, si deseas crearlo en tu directorio de proyectos, puedes usar el siguiente comando:

```bash
cd /ruta/del/directorio/de/tus/proyectos
```

3. Crea el entorno virtual llamado `venv` usando el siguiente comando:

```bash
python -m venv venv
```

4. Activa el entorno virtual. La forma en que lo haces depende del sistema operativo:

   - En Windows, usa:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS y Linux, usa:

     ```bash
     source venv/bin/activate
     ```

   Después de ejecutar este comando, verás `(venv)` en el prompt, lo que indica que el entorno virtual está activo.

5. Instala Django y otras dependencias usando `pip`. En este caso, instalaremos Django y si necesitas otras dependencias, agrégales al final del comando separadas por espacios:

```bash
pip install django
```

### Crear un Proyecto Django y Aplicaciones:

6. Luego, puedes crear un nuevo proyecto de Django usando el siguiente comando:

```bash
django-admin startproject mi_proyecto
```

7. Ingresa al directorio del proyecto:

```bash
cd mi_proyecto
```

### Migraciones y Ejecución del Servidor de Desarrollo:

8. Realiza las migraciones para configurar la base de datos inicial:

```bash
python manage.py migrate
```

### Ejecutar el Servidor de Desarrollo:

9. Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Esto iniciará el servidor de desarrollo y podrás acceder a tu aplicación Django en `http://127.0.0.1:8000/`.

### Freezar Dependencias (Opcional):

10. Si deseas "freezar" las dependencias en un archivo `requirements.txt` para compartir o replicar tu entorno, puedes usar el siguiente comando:

```bash
pip freeze > requirements.txt
```
Para instalar las dependencias listadas en un archivo `requirements.txt`, simplemente utiliza el comando `pip` junto con la opción `-r` y el nombre del archivo:

```bash
pip install -r requirements.txt
```

Esto leerá el archivo `requirements.txt` y descargará e instalará todas las dependencias especificadas junto con sus versiones correspondientes. Esto es útil cuando quieres replicar el entorno de tu proyecto en otro lugar o compartirlo con otros desarrolladores.

Este comando generará un archivo `requirements.txt` con una lista de todas las dependencias y sus versiones.

### Desactivar el Entorno Virtual (Cuando Hayas Terminado):

11. Cuando hayas terminado de trabajar en tu proyecto, puedes desactivar el entorno virtual con el comando:

```bash
deactivate
```

Recuerda activar el entorno virtual cada vez que vuelvas a trabajar en tu proyecto. ¡Listo! Ahora deberías tener un entorno virtual con Django instalado y listo para desarrollar tu proyecto.