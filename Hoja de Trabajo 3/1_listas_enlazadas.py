# -*- coding: utf-8 -*-
"""1. Listas enlazadas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iViu4KUFlhYN_GQjHpalUxND4KiR21et

# Listas enlazadas

definicion de la clase receta
"""

class receta:
  def __init__(self, paciente, fechaNacimiento, doctor, colegiado, fechaCita, horaCita, tipoConsulta, tratamiento): 
    self.paciente = paciente
    self.fechaNacimiento = fechaNacimiento
    self.doctor = doctor
    self.colegiado = colegiado
    self.fechaCita = fechaCita
    self.horaCita = horaCita
    self.tipoConsulta = tipoConsulta
    self.tratamiento = tratamiento

"""# Definicion de Class Nodo"""

class nodo:
  def __init__(self, receta=None, siguiente=None): 
    self.receta = receta
    self.siguiente = siguiente

"""# Definicion de la clase lista Enlazada"""

class listaEnlazada:
  def __init__(self):
    self.primero = None

  
  def insertar(self, receta):
    if self.primero == None:
      self.primero = nodo(receta = receta)
      return

      #actual es una variable que guarda a primero
    actual = self.primero
    #actual.siguiente es iugla a decir actual.siguiente != None
    while actual.siguiente:

      #actual ahora guarda el siguiente nodo, actual es un nodo que tiene datos y siguiente
      actual = actual.siguiente

    #accedemos al apuntador siguiente y le cambiamos el valor 
    #el receta de la izquierda es de la clase nodo, receta y el de la derecha es el valor de listaEnlazada
    actual.siguiente = nodo(receta = receta)



  # Recorrer para imprimir los nodos
  def recorrer(self):
    actual = self.primero

    while actual != None:
      print("Paciente: ", actual.receta.paciente, "| Fecha de Nacimiento:", actual.receta.fechaNacimiento, "| Doctor: ", actual.receta.doctor, 
            "| Colegiado: ", actual.receta.colegiado, "| Fecha de la Cita: ", actual.receta.fechaCita, "| Hora de la cita: ", actual.receta.horaCita, 
            "| Tipo de consulta: ", actual.receta.tipoConsulta, "| Tratamiento: ", actual.receta.tratamiento)

      # Nos pasamos al siguiente apuntador y asi de modo que llegue a vacio
      actual = actual.siguiente


  # Busqueda y desvinculacion de nodo
  def eliminar(self, colegiado, fechaCita, horaCita):
    actual = self.primero
    anterior = None

    while (actual != None and actual.receta.colegiado != colegiado and actual.receta.fechaCita != fechaCita and actual.receta.horaCita != horaCita):
      anterior = actual
      actual = actual.siguiente


    if anterior == None:
      self.primero = actual.siguiente
      actual.siguiente = None

    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None 


  def modificar(self, paciente, fechaCita, horaCita):
        actual = self.primero

        while actual != None:
            if actual.receta.paciente == paciente:
                actual.receta.fechaCita = fechaCita
                actual.receta.horaCita = horaCita
                return None
            actual = actual.siguiente

"""# Creacion de Objetos Receta"""

r1 = receta("Gerson L??pez", "03-10-1990", "Melvin Ortiz", 20156, "17-01-2023", "11:30", "Medicina General", "2 pildoras de acetaminofen cada 6 horas")
r2 = receta("Karen G??mez", "08-05-2000", "Jorge Merida", 8567, "31-01-2023", "09:00", "Medicina interna", "Tylenol de 20 ml cada 4 horas")
r3 = receta("Luis Garc??a", "17-09-1987", "Melvin Ortiz", 20156, "02-02-2023", "12:00", "Medicina general", "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")

"""## **Incersion**"""

lista_e = listaEnlazada()
lista_e.insertar(r1)
lista_e.insertar(r2)
lista_e.insertar(r3)

"""## **Recorrer**"""

lista_e.recorrer()

"""# **Eliminar**"""

#lista_e.eliminar(20156, "17-01-2023", "11:30")

lista_e.recorrer()

"""## **Modificar**"""

lista_e.modificar('Gerson L??pez',"20-02-2023","Hora de la cita:  14:20")

lista_e.recorrer()