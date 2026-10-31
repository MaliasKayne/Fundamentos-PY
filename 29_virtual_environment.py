#Entorno virtual python#
#me permite crear un entorno aislado, independiente, me permite evitar conflitos de dependencias entre proyectos
#ejecutar el siguiente comando en la terminal para crear el entorno virtual y darle un nombre ".venv" en este caso -> python -m venv .venv 
#-m ejecuta el modulo integrado
#venv modulo nativo, gestiona el entorno virtual
#.venv es el nombre del entorno a crear

#Activar el entorno virtual ->
#powershell: .\.venv\Scripts\Activate.ps1
#GitBash: source .venv/Scripts/activate
#CMD DOS: .\.venv\Scripts\activate.bat

#para verificar que el entorno virtual apunta a .venv
#where.exe python

#En caso de que windows bloquee el uso del script usar el siguiente comando en powershell modo admin
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -scope CurrentUser
#Cuando lo pida presionar S y despues ENTER

#para ver los paquetes instalados
# pip list
#para listar los paquetes instalados por mi, fuera de los del sistema generando un archivo
#pip freeze > requirements.txt
#para ver la informacion especifica de un paquete
#pip show (requests) <- nombre del paquete
#para desactivar el entorno virtual
#deactivate