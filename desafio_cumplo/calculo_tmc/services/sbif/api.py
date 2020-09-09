import requests
import json
import datetime
import os



ENDPOINT_ROOT = 'https://api.sbif.cl/api-sbifv3/recursos_api/tmc'
PAYLOAD = {'apikey': os.environ['APIKEY_SBIF'], 'formato': 'json'}


def getTasaMaximaConvencional(fecha , monto , plazo , is_reajustable , is_extranjera):

    date_input =fecha
#    date_input = datetime.datetime.strptime(fecha, '%Y-%m-%d')
#    date_input = datetime.datetime(2020, 5, 15, 0, 0)
    resource_year = date_input.strftime("%Y")

    if(date_input.day < 15):
        resource_month = str(date_input.month -1)
    else:
        resource_month = str(date_input.month)

    endpoint = '/'.join([ENDPOINT_ROOT,resource_year,resource_month])

    response = requests.get(endpoint , params= PAYLOAD).text.encode('utf-8')

    response_json = json.loads(response)

    if(is_extranjera == False):

        if(is_reajustable == False):

            if(plazo < 3):
                #titulo = 'Operaciones no reajustables en moneda nacional de menos de 90 días'

                if(monto<=5000):
                    tipo = '26'
                elif(monto > 5000):
                    tipo = '25'
            
            elif(plazo >= 3):
                #titulo = 'Operaciones no reajustables en moneda nacional 90 días o más'

                if(monto<=50):
                    tipo = '45'
                elif(50 < monto <= 200 ):
                    tipo = '44'
                elif(200 < monto <= 5000):
                    tipo = '35'
                elif(monto > 5000):
                    tipo = '34'
        
        elif(is_reajustable == True):
            #titulo = 'Operaciones reajustables en moneda nacional'

            if(plazo < 12):
                tipo = '21'
            elif(plazo >= 12):

                if(monto <= 2000):
                    tipo = '24'
                elif(monto > 2000):
                    tipo = '22'
            
    elif(is_extranjera == True):
        #titulo = 'Operaciones expresadas en moneda extranjera'
        if(monto <= 2000):
            tipo = '41'
        elif(monto > 2000):
            tipo = '42'

    else:
        #subtitulo='Operaciones cuyo mecanismo de pago consista en la deducción de las respectivas cuotas directamente de la pensión del deudor'
        tipo = '43'

    for item in response_json['TMCs']:
        if (item['Tipo'] == tipo):
            return item