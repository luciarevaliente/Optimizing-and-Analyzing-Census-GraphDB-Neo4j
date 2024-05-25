from neo4j import GraphDatabase
import csv

#################################################################
# Obtenció arestes ANY_PADRO (dinàmiques)
MUNICIPIS = "dades/HABITATGES.csv"

# Connexió amb Neo4j
uri = "bolt://localhost:7687"
usuario = "neo4j"
contraseña = "Ojosgrandes_14"
driver = GraphDatabase.driver(uri, auth=(usuario, contraseña))

# Llegim el fitxer CSV i obtenim la columna desitjada
with open(MUNICIPIS, mode='r') as file_csv:
    lector_csv = csv.DictReader(file_csv)
    for fila in lector_csv:
        municipi = fila["Municipi"]
        id_llar = fila["Id_Llar"]
        any_padro = fila["Any_Padro"]

        if municipi != "null":
            # Construim la consulta Cypher amb label dinàmic
            with driver.session() as session:
                consulta_cypher = f"MATCH (m:{municipi}), (h:HABITATGES {{Id_Llar: '{id_llar}'}}) CREATE (h)-[:{'ANY_PADRO_' + any_padro}]->(m)"
                session.run(consulta_cypher)

print("\nImportació arestes dinàmiques ANY_PADRO acabades!!")
