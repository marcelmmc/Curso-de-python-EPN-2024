# Esta funcion abre el archivo con los estudiantes y regresa una list de strings
def leer_informacion_estudiantes():
    nombre_archivo_datos = 'estudiantes.txt'
    lista_estudiantes = []
    # Open file
    with open(nombre_archivo_datos) as file:
        lineas = file.readlines()
        for linea in lineas:
            atributos_estudiante = linea.split(', ')
            # Eliminar character de nueva linea
            atributos_estudiante[-1] = atributos_estudiante[-1][:-1]
            lista_estudiantes.append(atributos_estudiante)
    return lista_estudiantes

class Estudiante:
    def promedio(self):
        # TODO
        # Completa esta funcion para que retorne el promedio de un estudiante
        return 10

    def __lt__(self, other):
        return self.promedio() < other.promedio()

datos_estudiantes = leer_informacion_estudiantes()
for datos_estudiante in datos_estudiantes:
    print('Datos de estudiante', datos_estudiante)


# Aqui deberas asegurarte que la lista de de estudiantes sea ordenada
# TODO

# Aqui deberas imprimir cada uno de los estudiantes
# ya que han sido ordenados
# TODO
