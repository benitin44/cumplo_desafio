
Desafío: 
En Cumplo operamos créditos. Desafortunadamente, a veces, algunos créditos no son pagados en el plazo acordado, y por tanto caen en en lo que llamamos "mora", la mora implica intereses extras. Para calcular los intereses de esa mora a pagar, nos regimos por la TMC (tasa máxima convencional). 

Tu desafío es que construyas una aplicación que a partir de las las características de un crédito (monto del crédito  y plazo del crédito), nos muestre la TMC que corresponde en X día de atraso. Dado que la TMC cambia día a día queremos poder consultar por la TMC de cualquier día en particular 

El sistema debe responder realizando lo siguiente: 
El usuario de la aplicación debe poder especificar el monto en UF, el plazo en días y la fecha en la que quieres saber la TMC
Según esos parámetros la aplicación debe entregar la TMC correspondiente al día consultado

#Para iniciar proyecto localmente 

-Python 3.8
-Dependencias: django , requests



1) Dependency

pip install -r requirements.txt

2) APIKEY setup

#Linux/MacOS X
export APIKEY_SBIF=xxxxxxxxxxxxxxxxxxxxxxxxx

#Windows 
set APIKEY_SBIF=xxxxxxxxxxxxxxxxxxxxxxxxx

3)RUN Server
python manage.py runserver


