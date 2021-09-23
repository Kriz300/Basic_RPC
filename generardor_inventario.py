import json
import random
import string


datos = {}
datos["Inventario"] = []
for i in range(1000):
	producto1 = string.ascii_lowercase
	producto = ''.join(random.choice(producto1) for i in range(10))
	cantidad = random.randint(1,10)
	precio = random.randint(1,100)
	datos["Inventario"].append({
		'Nombre': producto,
		'Precio': precio,
		'Cantidad': cantidad
		})

with open('inventario.json', 'w') as file:
	json.dump(datos,file, indent=4)