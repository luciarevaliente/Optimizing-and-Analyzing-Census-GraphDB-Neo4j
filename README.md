# Description in English:
This repository contains a project focused on the analysis and optimization of non-relational databases using Neo4j, a graph-oriented database. The main objective is to study the socioeconomic evolution of a population based on historical census records, documents that collect personal information such as names, surnames, ages, and other demographic details.

The project is extensively outlined in the PDF document `enunciat.pdf`. The procedure is detailed in the DOCX file `memoria.docx`, along with the analysis of results. The presentation `presentacio.pptx` aesthetically summarizes the queries and conclusions of the work.

## Project Structure:
### First Part:
This phase consists of three main tasks, all performed directly in **Neo4j**. Each task corresponds to a directory in the repository:
1. `tasca1:` **Import** of the data from CSV files, adding indexes and constraints to the database to improve its performance. The executed queries can be found here.
2. `tasca2:` **Queries** on the provided database, evaluating the performance of the queries executed.
3. `tasca3:` Queries using **graph analytics**, where advanced techniques are applied to analyze the relationships and patterns in the data.

### Second Part:
In this phase of the project, we aimed to **redesign the database** to visualize the **demographic evolution** of each population more efficiently. This redesign involves creating a new structure that organizes the data based on the queries that need to be performed, allowing for a more precise reflection of the relationships between individuals, their households, and the localities in which they live.

With these modifications, the database will be able to provide a clearer understanding of the demographic data, improving the ability to perform queries that capture interactions and changes in the population over time. Additionally, we will enhance the **scalability** and **efficiency** of the database.

This part corresponds to the directory `tasca4`. In it, there is a diagram with the new database and a `README.txt` file explaining the **execution order of the files** contained in the `creacio_bd` folder. Within this last directory, we have published a .txt file to import the nodes and relationships that remain unchanged in the database. The .py files are used to iteratively add dynamic nodes and edges.


# Descripción en castellano:
Este repositorio contiene un proyecto enfocado en el análisis y optimización de bases de datos no relacionales utilizando Neo4j, una base de datos orientada a grafos. El objetivo principal es estudiar la evolución socioeconómica de una población a partir de los padrones históricos de habitantes, documentos que recogen información personal como nombres, apellidos, edades y otros detalles demográficos. 

En el documento pdf `enunciat.pdf` se plantea el proyecto de manera extensa. En el docx `memoria.docx` se expone todo el procedimiento, junto con el análisis de resultados. En la presentación `presentacio.pptx` se muestra de forma estética y resumida las querys y conclusiones del trabajo.

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
