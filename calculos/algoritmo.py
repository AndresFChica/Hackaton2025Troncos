import json
import math
from datetime import datetime

# Abre y lee el archivo JSON correctamente
with open("MOCK_DATA.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Cargar directamente el JSON desde el archivo
persona = 6
caso = 1

due_date_str = data[persona].get("due_date", "No disponible")
actual_date = datetime.now().strftime("%d/%m/%Y")

actual_date_obj = datetime.strptime(actual_date, "%d/%m/%Y")
due_date_obj = datetime.strptime(due_date_str, "%d/%m/%Y")

deuda = data[persona].get("credit", "No disponible")

# Alerta de 5 dias antes de entrar en mora
difference = (due_date_obj - actual_date_obj).days
if(difference == 5):
    print("Pana pague ps pobre hpta")

# Calcular la deuda 0.000875
if(difference<0):
    deuda_extra = (difference*(-0.000875)*deuda)
    print("Duda:", deuda_extra)

# Calcular las cuotas
cuotas = math.ceil(difference/30)
print("Cuotas", cuotas)

# Valor por cuota
valor_c = deuda/cuotas
print("Valor por cuota:", valor_c)

if(caso == 1):
    # Caso 1 extension plazo
    nueva_coutas = cuotas + 6
    nuevo_valor_c = deuda/nueva_coutas
    # Cambiar fecha de pago en la bd
elif(caso == 2):
        # Caso 2 Disminucion de plazo
    if(cuotas <= 2):
        print("Ya estas a punto de pagar tu credito!! si quieres cancelarlo aun mas rapido entra a este link: aqui iria un link")
    else:
        nueva_coutas = cuotas - 2
        nuevo_valor_c = deuda/nueva_coutas
else:
    # Caso 3 Periodo de gracia
    if(difference <= -3):
        nueva_fecha=difference + 3




print("Fecha actual:", actual_date)
print("Fecha pago:", due_date_str)
print("Dias restantes:", difference)

