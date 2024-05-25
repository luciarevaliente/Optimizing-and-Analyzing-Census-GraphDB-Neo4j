from neo4j import GraphDatabase
import csv

#################################################################
# Obtenció dels labels LOCALITAT
MUNICIPIS = "dades/MUNICIPIS.csv"
nom_columna = "Municipi"

# Llista per emmagatzemar els labels LOCALITAT
labels = []

# Llegim el fitxer CSV i obtenim la columna desitjada
with open(MUNICIPIS, mode='r') as file_csv:
    lector_csv = csv.DictReader(file_csv)
    for fila in lector_csv:
        labels.append(fila[nom_columna])

# Comprovem les dades llegides
print("Dades de la columna '{}':".format(nom_columna))
for label in labels:
    print(label)

#################################################################
# Creació dels nodes amb label LOCALITAT (dinàmic)
uri = "bolt://localhost:7687"
usuario = "neo4j"
contraseña = "Ojosgrandes_14"
driver = GraphDatabase.driver(uri, auth=(usuario, contraseña))

# Construim la consulta Cypher amb label dinàmic
with driver.session() as session:
    for label in labels:
        consulta_cypher = f"CREATE (n:MUNICIPI {{Municipi: '{label}'}}) SET n:{label}"
        session.run(consulta_cypher)

print("\nImportació labels dinàmics acabats!!")