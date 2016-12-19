# Scrap Temperatura ARG

Ante la falta de un api del servicio meteorológico nacional ...


## Intalación

* Clonar el repo
* Crear un virtualenv `virtualenv venv` 
* Activar el entorno `source venv/bin/activate`
* Instalar las dependencias `pip install -r requirements.txt`
* correr el scrap `python scraptemp.py`


## Correr desde un crontab

Para correr desde un crontab hay que duplicar el `scrap.bash.template` en `scrap.bash` y darle permisos de ejecución `$ chmod a+x scrap.bash`

Luego solo quedaría poner los paths correspondientes en `scrap.bash` y apuntar el cron cada N tiempo a `scrap.bash`. 
