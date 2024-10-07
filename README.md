# Descripción en castellano:
Este repositorio contiene un proyecto enfocado en el análisis y optimización de bases de datos no relacionales utilizando Neo4j, una base de datos orientada a grafos. El objetivo principal es estudiar la evolución socioeconómica de una población a partir de los padrones históricos de habitantes, documentos que recogen información personal como nombres, apellidos, edades y otros detalles demográficos. 

## Estructura del proyecto:
### Primera parte: 
Esta fase consta de tres tareas principales, todos realizados directamente en **Neo4j**. A cada tarea (tasca) le corresponde una directorio del repositorio:
1. `tasca1:` **Importación** de los datos desde ficheros CSV, añadiendo índices y restricciones a la base de datos para mejorar su rendimiento. Las querys ejecutadas se encuentran
2. `tasca2:` **Consultas** sobre la base de datos proporcionada, evaluando el rendimiento de las consultas realizadas.
3. `tasca3:` Consultas mediante **analítica de grafos**, donde se aplican técnicas avanzadas para analizar las relaciones y patrones en los datos.
    
### Segunda parte:
En esta fase del proyecto, nos hemos propuesto **rediseñar la base de datos** con el objetivo de visualizar de manera más eficiente la **evolución demográfica** de cada población. Este rediseño implica la creación de una nueva estructura que organiza los datos en función de las consultas que se desean realizar, lo que permite reflejar de manera más precisa las relaciones entre las personas, sus hogares y las localidades en las que viven. 

Con estas modificaciones, la base de datos será capaz de ofrecer una comprensión más clara de los datos demográficos, mejorando la capacidad para realizar consultas que capturen las interacciones y cambios en la población a lo largo del tiempo. Además, mejoraremos la **escalabilidad** y **eficiencia** de la BD.

A esta parte le corresponde el directorio `tasca4`. En él, hay un diagrama con la nueva BD y un fichero `README.txt` donde se explica el **orden de ejecución de los ficheros** contenidos en la carpeta `creacio_bd`. Dentro de este último directorio, hemos publicado el archivo .txt para importar los nodos y relaciones que no se modifican de la BD. Los archivos .py son para añadir los nodos y aristas dinámicos de forma iterativa. 
