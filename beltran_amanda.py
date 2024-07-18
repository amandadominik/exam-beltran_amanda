import random
import csv
trabajadores = ["Juan Pérez” , ”María García” , ”Carlos López” , ”Ana Martínez” , ”Pedro Rodríguez” ,”Laura Hernández” ,”Miguel Sánchez” , ”Isabel Gómez” , ”Francisco Díaz” , ”Elena Fernández"] 
sueldos={}

def asignar_sueldos_aleatorios(trabajadores):
    sueldos={trabajador:random.randint(300000,2500000)for trabajador in trabajadores}
    print("los sueldos fueron asignados aleatoriamente:")
    for trabajador ,sueldo in sueldos.items():
     print(f"{trabajador},{sueldo}")
    return sueldos

def clasificar_sueldos(sueldos):
   clasificar={"menores a $800000":[],"entre $800000 y $2000000":[],"superiores a $2000000}":[]}
   for trabajador ,sueldo in sueldos.items():
      if sueldo < 800000:
         clasificar["menor a $800000"].append((trabajador,sueldo))
      elif sueldo < 2000000:
         clasificar["entre $800000 y $2000000"].append((trabajador, sueldo))
      else:
       clasificar["superiores a $2000000"].append ((trabajador,sueldo))
      print("clasificacion por sueldos:")
      for categoria ,empleados in clasificar.items():
         print("f{categoria}- total:{len(empleados)}")
         for trabajador, sueldo in empleados:
            print(f"{trabajador}:{sueldo}")
            print()
            print(f"total sueldos:{sum(sueldos.values())}")

def ver_estadisticas(sueldos):
   sueldo_mas_alto= max(sueldos.values())
   print(f"sueldo mas alto:{sueldo_mas_alto}")

   sueldo_mas_bajo= min(sueldos.values())
   print(f"sueldo mas bajo:{sueldo_mas_bajo} ")

   promedio_sueldos=round(sum(sueldos.values())/len(sueldos),2)
   print(f"promedio de los sueldos:{promedio_sueldos}")

def reporte_sueldos(sueldos):
   with open ('sueldos.csv','w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv,delimiter=";")
   escritor_csv.writerow(['nombre empleado','sueldo base', 'descuento salud','descuento afp','sueldo liquido'])
   for trabajador ,sueldo in sueldos.items():
      descuento_salud=round(sueldo*0.07)
      descuento_afp=round(sueldo*0.12)
      sueldo_liquido=round(sueldo-descuento_salud-descuento_afp)
      escritor_csv.writerow([trabajador,round(sueldo,2),descuento_salud,descuento_afp,sueldo_liquido])


def menu():
    salir=False
    sueldos={}
   
    while not salir:
     print("menu:")
     print("1.asignar sueldos aleatorios") 
     print("2.clasificar sueldos")
     print("3.ver estadisticas")
     print("4.reporte de sueldos") 
     print("5.salir del programa")    
     
opcion=input("ingrese una opcion:")

if opcion=="1":
   sueldos=asignar_sueldos_aleatorios(trabajadores)
elif opcion=="2":
   if sueldos:
    clasificar_sueldos
   else:
      print("debe asignar sueldos aleatorios antes")
elif opcion=="3":
   if sueldos:
      ver_estadisticas
   else:
      print("debe asignar sueldos antes")
elif opcion=="4":
   if sueldos:
      reporte_sueldos
   else:
      print("debe asignar sueldos antes")
elif opcion=="5":
   salir=True
   print("saliendo del programa...")
   print("desarrollado por amanda beltran rut 21.153.726-4")
   exit()
else:
   print("opcion invalida.intentelo nuevamente")

menu()
            

