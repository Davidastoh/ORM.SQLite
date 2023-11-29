import orm
from tablas.Autores import Autores
from tablas.Libros import Libros
from tablas.Usuarios import Usuarios

db=orm.SQLiteORM("db_Biblioteca")

# db.crear_tabla(Autores)
# db.crear_tabla(Libros)
# db.crear_tabla(Usuarios)

# Autor_uno={"dni":74853525,"Nombre":"Quevedo","Apellidos":"Escoja"}
# db.insertarUno("Autores",Autor_uno)

Usuarios_varios=[
    {
        "dni":71435432,
        "Nombre":"Nadinne",
        "Apellidos": "Atoccsa",
        "f_Nacimiento":"23/02/2005",
        "Estado":"Activo"  
    },
    {
        "dni":75384688,
        "Nombre":"Feliciana",
        "Apellidos": "Ccacca",
        "f_Nacimiento":"22/11/1997",
        "Estado":"Activo"  
    },
    {
        "dni":75635454,
        "Nombre":"Bichota",
        "Apellidos": "Taipe",
        "f_Nacimiento":"13/09/2004",
        "Estado":"Inactivo"  
    },
    {
        "dni":65463688,
        "Nombre":"Chamo menor",
        "Apellidos": "No jodas",
        "f_Nacimiento":"24/11/1997",
        "Estado":"Activo"  
    },
    {
        "dni":43576688,
        "Nombre":"Yadira",
        "Apellidos": "Viuda",
        "f_Nacimiento":"500 ac",
        "Estado":"Momia"  
    }   
]
# db.insertarVarios("Usuarios",Usuarios_varios)

# ##Para mostrar una lista de Tuplas
# print(db.mostrar_tabla("Usuarios"))
# ##Para mostrar como un objeto con sus campos y sus valores
# print(db.mostrar_tabla("Usuarios",type="objeto"))   
# ## Para mostrar con especificaciones (filtrados)
# print(db.mostrar("Usuarios",where="Estado='Momia'",type="objeto"))
# ##Para buscar por los campos
# print(db.mostrar("Usuarios",where="Apellidos LIKE'cha%'",type="objeto"))
# print(db.mostrar("Usuarios",where="dni=65463688",type="objeto"))
# ## print(db.mostrar("Usuarios",where="Precio >10",type="objeto"))

# db.actualizar("Usuarios",{"Estado":"Activo"},where={"Nombre":Yadira})

#db.actualizar("Usuarios",{"f_Nacimiento":"11/12/2005"},where="dni:43576688")

## Para actualizar mas campos
# # dato_actualizar={"Nombre":"Chamo","Apellidos":"Ya es salida"}
# # db.actualizar("Usuarios",dato_actualizar,where="dni:43576688")

db.eliminar("Usuarios",where="Nombre:'Bichota'")
db.eliminar("Usuarios",where="dni:43576688")


print(db.mostrar("Usuarios",type="objeto"))

