</h1 align='center'>Siniestros Viales en CABA</h1>
Análisis de Datos de Siniestros Viales en CABA

<h2 align='center' id='intro'>Descripción</h2>

Proyecto de análisis de datos con el objetivo de generar información que permita visualizar medidas para disminuír la cantidad de víctimas fatales de los siniestros viales.

### Tabla de Contenido
1. [Introducción](#intro)
2. [Instalación y Requisitos](#requirements)
3. [Estructura del Proyecto](#struct)
4. [Uso y Ejecución](#use)
5. [Datos y Fuentes](#data)
7. [Resultados y Conclusiones](#result)
8. [Contribución y Colaboración](#colab)
9. [Licencia](#licence)

<h2 align='center' id='requirements'>Instalación y Requisitos</h2>

### Requisitos:
<ul>
    <li>Python</li>
    <li>Pandas</li>
    <li>Numpy</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
</ul>

### Pasos de Instalación:

1. Clonar el repositorio: `git clone https://github.com/DataSciGina/SiniestrosViales.git`
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4. Instalar las dependencias: `pip install -r requirements.txt`

<h2 align='center' id='struct'>Estructura del Proyecto</h2>

- `functions/`: Contiene las funciones implementadas para el proyecto.
- `notebooks/`: Contiene los Jupyter Notebooks con los análisis individuales y un análisis conjunto.
- `src/`: Contiene las subcarpetas con recursos.
    - `data/`: Contiene la data original y los distintos archivos con la data procesada.
- `reports/`: Visualizaciones.
- `README.md`: Documentación.

<h2 align='center' id='use'>Uso y Ejecución</h2>

Ejecutar los tres archivos en la carpeta `notebooks/` para el análisis.

<h2 align='center' id='data'>Datos y Fuentes</h2>

Datos del `Observatorio de Movilidad y Seguridad Vial` (OMSV), subdivisión de la <b>Secretaría de Transporte</b> del Gobierno de la Ciudad Autónoma de Buenos Aires.

<h2 align='center' id='result'>Resultados y Conclusiones</h2>

### Observaciones Tabla de Hechos:

- La mayoría de los siniestros ocurren durante la franja horaria de 5 a 7:59 horas.
- La mayoría de los accidentes ocurren en avenidas.
- La mayoría de los accidentes la mayoría de accidentes ocurren en la comuna 1.
- La mayoría de las víctimas son motos y peatones.
- La mayoría de los accidentes ocurrieron entre los años 2016 y 2018.
- Se ve una mayor concentración de accidentes en áreas específicas.
- La mayor concentración de accidentes se encuentran en las avenidas de la comuna 2.
- La mayor cantidad de acusados son pasajeros siendo las víctimas los peatones.

### Observaciones Tabla de Víctimas:

- La mayoría de los roles de las víctimas son conductor y peatón (46.03% y 37.24% respectivamente).
- La mayoría de las víctimas son Motos y Peatones (42.26% y 37.24% respectivamente).
- El sexo más frecuente de las víctimas es masculino (76.01%).
- La mayoría de las víctimas tienen entre 20 y 30 años.
- La mayoría de las víctimas fallecieron entre el año 2016 y el año 2018.
- En todos los roles, la mayoría de las víctimas son hombres.
- Entre las mujeres, la mayoría de las víctimas femeninas son peatones.
- Las víctimas masculinas tienden a tener entre 20 y 40 años.
- Las víctimas femeninas tienden a estar en un rango mayor que los hombres sin una concentración mayor en áreas específicas.
- Los peatones parecen tener una mayor distribución de edades, lo que podría indicar que personas de todas las edades están involucradas como víctimas cuando caminan.
- Los conductores y ciclistas parecen tener distribuciones de edad más concentradas, con la mayoría de las víctimas en estos roles siendo personas entre los 30 y 50 años.
- Los pasajeros/acompaniantes tienden a ser más jóvenes en promedio que los conductores, lo cual tiene sentido si consideramos que muchas veces los pasajeros pueden ser miembros de la familia o amigos más jóvenes.
- La mayoría de las víctimas masculinas fallecieron entre los años 2016 al 2018.
- La mayoría de las víctimas femeninas fallecieron entre los años 2017 y 2018.

### Observaciones Tabla Unificada:
#### Distribución de Rol y Sexo por Tipo de Calle
- La mayoría de accidentes ocurren en avenidas y las víctimas más comúnes son Conductores y Peatones.
- En el tipo de calle Gral Paz, los conductores son las principales víctimas.
- En calles, las principales víctimas son Peatones y Conductores.
- En autopistas, las principales víctimas son conductores.
- No se observan víctimas ciclistas en Autopistas ni en Gral Paz.
- La mayor cantidad de hombres y mujeres que mueren en siniestros viales, fallecen en avenidas.
- La distribución de fallecimientos en Gral Paz y en Autopistas son prácticamente iguales.

#### Distribución de Edad por Tipo de Calle
- La mayor cantidad de víctimas tienen entre 25 y 60 años tanto en calles (con una media aproximada de 40 años) como en avenidas (con una media menor a los 40 años y una mayor dispersión de datos).
- En Gral Paz, la mayor concentración de víctimas se encuentra (aproximadamente) entre un poco menos de 25 años y los 50 años (aprox) y la media se encuentra un poco por debajo que en las avenidas.
- En autopistas la mayor cantidad de víctimas se encuentran entre un poco menos de 25 años y 40 años (aprox) con una media aproximada de 25 años.
- En autopistas pueden distinguirse valores atípicos. Considerando que Gral Paz también es una autopista y que la mayoría de esos valores atípicos encajan en la distribución no se consideran un problema.
- Si bien Gral Paz es una autopista, es válido considerarla un elemento más, dado que tiene una gran cantidad de muertos.
- Se deja el valor atípico inferior en autopistas porque puede ser atípico, pero no significa que no sea real.

#### Cruce por Rol, Edad y Sexo
- La mayoría de los accidentes ocurren en cruces y la mayoría de as víctimas, en ambos casos, son conductores y peatones.
- La distribución de edad de cruces y calles no varía demasiado.

#### Distribución de Incidentes por Franja Horaria
- Los ciclistas tienden a ser víctimas en los siguientes horarios: de 3 a 4, de 5 a 10, de 11 a 13, de 16 a 18 y de 19 a 00.
- Entre las 23 y las 10 la mayoría de las víctimas son conductores, mientras que de 10 a 23 la mayoría de las víctimas son peatones.

#### Distribución de Incidentes por franja horaria y edad
- Variabilidad de la edad: A lo largo del día, se observa una variabilidad significativa en la edad de las personas involucradas en incidentes. Esto es evidente por el rango de los bigotes y la dispersión de los outliers.
- Mayor dispersión alrededor de las 10:00 y 12:00 horas: Entre las horas de la mañana (10:00 - 12:00), parece haber una mayor dispersión de la edad, ya que los bigotes y el rango intercuartílico (IQR) son más amplios en comparación con otras horas. Esto sugiere que personas de diferentes grupos de edad están involucradas durante estas horas.
- Patrón estable desde las 14:00 hasta las 20:00: Durante las horas de la tarde (14:00 - 20:00), las edades parecen ser más consistentes, con rangos intercuartílicos menos dispersos y sin demasiados outliers.
- Outliers en varias horas: A lo largo del gráfico, hay puntos fuera de los bigotes (outliers), lo que sugiere que en ciertas horas hay individuos significativamente más jóvenes o más mayores que el rango general.
- Mediana de la edad constante: A lo largo del día, la mediana de la edad (línea dentro de cada caja) no varía drásticamente. Esto indica que, en general, la edad media de las personas involucradas en incidentes es relativamente constante, alrededor de los 40-50 años, en la mayoría de las horas.
- Horas con menos variación: A partir de las 22:00 horas hasta la medianoche, la dispersión de las edades se reduce, sugiriendo que los incidentes a esas horas tienden a involucrar a un grupo de edad más homogéneo.

### Conclusiones:
- La mayoría de las víctimas mueren entre las 2 y las 13 hs.
- En diciembre, la cantidad de víctimas tiende a aumentar.
- La mayoría de los siniestros viales transcurren en cruces, principalmente entre autopistas y avenidas.
- La mayoría de las víctimas en moto tienen entre 20 y 30 años.
- La mayoría de los accidentes en autopistas son causados por camiones de carga y las principales víctimas son motos.
- La mayoría de los accidentes en autopistas se producen en cruces y se concentran a lo largo de la Av Gral Paz.
- Los accidentes en autopistas que no se producen en cruces se concentran mayormente en el interior sur de la ciudad.

<h2 align='center' id='colab'>Contribución y Colaboración</h2>

Se invita a colaboradores a contribuír en la mejora del análisis, así como a proporcionar retroalimentación sobre el proyecto.

<h2 align='center' id='licence'>Licencia</h2>

Agostina Ailén Fernández Rodríguez - Contacto: [LinkedIn](https://www.linkedin.com/in/agostina-fern%C3%A1ndez-aab4a8323/)