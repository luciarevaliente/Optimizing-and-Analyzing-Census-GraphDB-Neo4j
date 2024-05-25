from neo4j import GraphDatabase
import csv

#################################################################
# Obtenció arestes ANY_VIU (dinàmiques)
VIU = "dades/VIU.csv"

# Connexió amb Neo4j
uri = "bolt://localhost:7687"
usuario = "neo4j"
contraseña = ""
driver = GraphDatabase.driver(uri, auth=(usuario, contraseña))

# Llegim el fitxer CSV i obtenim la columna desitjada
with open(VIU, mode='r') as file_csv:
    lector_csv = csv.DictReader(file_csv)
    for fila in lector_csv:
        # Hem comprovat prèvia i manualment que cap valor sigui "null"
        id_indv = fila["IND"]
        municipi = fila["Location"]
        id_llar = fila["HOUSE_ID"]
        any_viu = fila["Year"]

        # Construim la consulta Cypher amb label dinàmic
        with driver.session() as session:
            consulta_cypher = f"MATCH (i:INDIVIDUAL {{Id: '{id_indv}'}}), " \
                       f"(h:HABITATGES {{Id_Llar: '{id_llar}', Municipi: '{municipi}'}}) " \
                       f"CREATE (i)-[:{'ANY_VIU_' + any_viu}]->(h)"
            session.run(consulta_cypher)

print("\nImportació arestes dinàmiques ANY_VIU acabades!!")