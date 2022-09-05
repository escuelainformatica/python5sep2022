productos=[
    {"nombre":"cocacola","precio":200},
    {"nombre":"fanta","precio":400},
    {"nombre":"sprite","precio":400},
]

contador=0

for producto in productos:
    print(f"{producto['nombre']} ${producto['precio']}")
    contador=contador+producto['precio']

print(f"el total de precios es {contador}")