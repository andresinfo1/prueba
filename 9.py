from datetime import date, datetime

def comprobar_fecha(text):
    try:
        datetime.strftime(text, '%h/%m/%Y')
    except:
        return "El formato debe ser  DD/MM/YYYY"
    return datetime.strptime(text, '%h/%m/%Y')

fecha = input("Introduzca una fecha con el formato DD/MM/YYYY ")

fecha_i=comprobar_fecha(fecha)

print(fecha_i)

