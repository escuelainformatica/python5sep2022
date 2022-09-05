import datetime


fac1={
    "numfactura":2034,
    "fecha": datetime.datetime(2018,2,21),
    "numcliente":564,
    "terminos":"pagadero al recibirse",
    "detalle":[
        {  # 0
            "descripcion":"honorario por servicios",
            "cant":1,
            "preciounitario":200,
            "monto":200
         },
        { #1
            "descripcion": "mano de obra",
            "cant": 5,
            "preciounitario": 75,
            "monto": 375
        },
        { #2
            "descripcion": "descuento",
            "cant": 0,
            "preciounitario": -50,
            "monto": -50
        },
    ]
}


print(f"Num        : {fac1['numfactura']} ")
print(f"Fecha      : {fac1['fecha']} ")
print(f"NumCliente : {fac1['numcliente']} ")
print(f"Terminos   : {fac1['terminos']} ")
print("Descripcion | cantidad | precio unit | monto")
print(f"{fac1['detalle'][0]['descripcion']} | {fac1['detalle'][0]['cant']} | {fac1['detalle'][0]['preciounitario']} | {fac1['detalle'][0]['monto']}")
print(f"{fac1['detalle'][1]['descripcion']} | {fac1['detalle'][1]['cant']} | {fac1['detalle'][1]['preciounitario']} | {fac1['detalle'][1]['monto']}")
print(f"{fac1['detalle'][2]['descripcion']} | {fac1['detalle'][2]['cant']} | {fac1['detalle'][2]['preciounitario']} | {fac1['detalle'][2]['monto']}")
# print("Num: "+str(fac1['numfactura']))  # no se puede sumar un str con un int.

# print(fac1)
