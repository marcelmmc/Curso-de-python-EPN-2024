numero_equipos = int(input('Numero de equipos: '))
equipos = []
for indice in range(numero_equipos):
    equipo = input('Ingresa el equipo numero ' + str(indice+1) + ': ')
    equipos.append(equipo)

stadisticas = {}

for equipo in equipos:
    partidos_ganados = int(input(equipo + ' - Partidos ganados: '))
    partidos_perdidos = int(input(equipo + ' - Partidos perdidos: '))
    partidos_empatados = int(input(equipo + ' - Partidos empatados: '))
    puntaje = partidos_ganados*3 + partidos_empatados*1
    stadisticas[equipo] = (partidos_ganados, partidos_perdidos, partidos_empatados, puntaje)

print('Equipo'.ljust(20) + 'P. Ganados'.ljust(15) + 'P. Perdidos'.ljust(15) + 'P. Empatados'.ljust(15) + 'Puntaje'.ljust(15))
print('*' * 80)

def comparador(tupla):
    equipo = tupla[0]
    valores = tupla[1]
    puntaje = valores[3]
    return puntaje

stadisticas = {key: value for key, value in sorted(stadisticas.items(), key=comparador, reverse=True)}

for equipo, stadistica in stadisticas.items():
    print(equipo.ljust(20), end=' ')
    for valor in stadistica:
        print(str(valor).ljust(15), end='')
    print()
