personas=[
    {"n":1,"full name":"bill gates","position":"founder","Salary":1000},
    {"n":2,"full name":"bill gates","position":"founder","Salary":1000},
    {"n":3,"full name":"bill gates","position":"founder","Salary":1000},
    {"n":4,"full name":"bill gates","position":"founder","Salary":1000},
]

print(f"{personas[0]['n']}")


contador=0
for persona in personas:
    print(f"{persona['n']}")
    contador=contador+persona['Salary']

print(f"La suma es {contador}")

