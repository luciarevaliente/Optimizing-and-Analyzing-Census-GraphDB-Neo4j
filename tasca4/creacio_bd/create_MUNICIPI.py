import csv
#########################################################################
# Lectura municipis dels HABITATGES.csv
HABITATGES = "dades/HABITATGES.csv"  # Nom del fitxer CSV a llegir
municipis = []  # Llista per emmagatzemar els municipis de la BD

# Obrim i llegim el fitxer CSV
with open(HABITATGES, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        # Accedim als valors de cada fila pel nom de la columna
        municipi = row['Municipi']
        if municipi != "null" and [municipi] not in municipis:
            municipis.append([municipi])

#########################################################################
# Creació fitxer MUNICIPIS.csv
MUNICIPIS = "dades/MUNICIPIS.csv"  # Nom del fitxer CSV a crear
capcalera = ["Municipi"]  # Capçalera de les dades a introduïr

# Escrivim dades, incloent capçaleres
with open(MUNICIPIS, mode='w', newline='') as new_file:
    escritor_csv = csv.writer(new_file)
    escritor_csv.writerow(capcalera)  # Assignem capçaleres
    for i in municipis:
        escritor_csv.writerow(i)

print("Arxiu creat!")
