# HUMAN DATATHON 2022

[![banner](https://user-images.githubusercontent.com/113708256/192362109-207e0ae2-55be-46f9-84c2-0344e26fb013.png)](https://humandatathon.rgaba.com/prerelease)

## Introducción

Te invitamos a participar de la primera edición de [Human Datathon](https://humandatathon.rgaba.com/prerelease), un espacio en donde tanto especialistas en datos como en educación, nos pondremos al servicio de la Educación Digital.

> La unión hace la fuerza

Cuando diseñamos este Human Datathon lo hicimos con miras de abordar una problemática real: la educación digital. Como ya sabrás, la realidad siempre es compleja y requiere múltiples actores para entenderla y modificarla.

Por esto, proponemos la resolución de un desafío compartido invitando tanto a expertos en datos como en educación, para trabajar en conjunto a partir de una mirada multidisciplinaria.

En este evento no sólo pondrás a prueba tus capacidades técnicas para analizar datos o desarrollar un modelo de machine learning, sino también tu habilidad paragenerar insights y contar la historia que se esconde detrás de los datos.


## Data

Los datos corresponden a registros históricos de empleabilidad recolectados por [Sysarmy](https://sysarmy.com/blog/) disponibilizados en formato tabular.

Las bases incluyen edad, género, lenguajes de programación, sueldo, entre muchas variables. Para facilitar el proceso de entrenamiento del modelo predictivo, la data ya se encuentra dividida en dos carpetas (`Train` y `Test`). Tené en cuenta que sólo podrás acceder a la misma el día de la competencia.

La data de `Test` consistirá solamente en features para que puedas construir el modelo. La información correspondiente a la variable *target* no estará disponible para el dataset de prueba. El jurado utilizará la data real para evaluar el rendimiento de los modelos entrenados por los equipos. La performance será evaluada utilizando [RMSE](https://es.wikipedia.org/wiki/Ra%C3%ADz_del_error_cuadr%C3%A1tico_medio).

Ten en cuenta que podrás acceder de forma previa a la fecha del evento a un diccionario de datos (`Data_Schema.xlsx`) en donde encontrarán los nombres de los campos disponibles y una breve definición de los mismos. 

## Entregables

Esta competencia contará con 3 entregables:

Visualizaciones.
CSV con predicciones.
Presentación en Google Slides.

Cada equipo deberá presentar el resultado final de su trabajo en una presentación en formato *elevator pitch* o [reporte de resultados](https://www.inboundcycle.com/blog-de-inbound-marketing/como-elaborar-informe-para-presentar-resultados-estrategia).

Esta presentación estará dividida en dos partes:

-   La primera, mostrando la exploración de datos realizada, detectando qué variables tienen incidencia sobre la variable *target*, el tipo de modelo usado y las principales transformaciones aplicadas y las features elegidas o desarrolladas para construir el modelo.

-   La segunda parte consistirá en la exploración de una problemática relacionada con el área educativa utilizando los datos compartidos y otras **fuentes externas que puedan ser relevantes**. En esta parte se hará hincapié en la detección de inequidades en el ámbito educativo, formulación de hipótesis y recomendaciones.

### Detalles de cada entregable

#### Visualización:

>El primer paso para modificar la realidad es entenderla.

Previo a la creación de un modelo, tenemos que familiarizarnos con la data; desde cómo está organizada, hasta observar cómo las diferentes variables se relacionan con aquel *target* que queremos inferir. Es fundamental para formarnos una idea de la problemática; lo que nos permitirá tomar mejores decisiones al momento de plantear nuestro modelo. A su vez, este proceso nos otorgará nuestro primer entregable.

Queremos que traduzcas la información de estas tablas a un formato que nos de un pantallazo de cuáles son las variables y de qué forma impactan en la variable *target*. Puedes usar la herramienta que desees para generar las visualizaciones (Python, R, Tableau, etc).

**Tipo de entregable**Presentación en Google Slides (con las visualizaciones).

Este entregable será presentado en conjunto con el análisis de la situación educativa (entregable 3) al final del evento en una presentación de formato de equipos.

La presentación deberá realizarse utilizando [Google Slides](https://docs.google.com/presentation/). Esta deberá ser compartida a *[datamktsci@rga.com](mailto:datamktsci@rga.com)*. El archivo deberá estar nombrado con el número y nombre de equipo.

#### Modelo

El foco en este entregable es realizar un modelo que prediga, lo más acertadamente posible, el valor de la variable *target* (esta será revelada el día del datathon). Para esto, vas a contar con los datos “semi-preparados”.
Por un lado, podrás acceder a los datos de entrenamiento, los cuales contarán con diversos campos así como también la variable *target*. Esta data irá desde el 2015 hasta el 2021.

Una vez que el equipo esté conforme con la performance del modelo, deberán realizar predicciones sobre nueva data que se les será disponibilizada, pero sin la variable *target*.
Volcarán estas variables en un archivo .csv y lo enviarán por correo, en donde el equipo de Data Science de R/GA calculará el rendimiento de cada modelo.

Si bien el data set estará pre-limpiado, hará falta realizar data cleaning y por sobre todo realizar [feature engineering]([https://en.wikipedia.org/wiki/Feature_engineering](https://en.wikipedia.org/wiki/Feature_engineering)).

Algunos campos al ser de texto libre tendrán casos escritos de forma ligeramente diferente.
Tener criterio a la hora de tratar con los valores faltantes.
Es posible que tengas que lidiar con anomalías.
Habrá columnas categóricas con habilidades o tecnologías que deberás transformar, ya sea haciendo agregaciones sobre estas o creando nuevas variables.
Al ser datos reales algunas respuestas no tendrán sentido(por ejemplo, algunas personas escriben chistes)
Deberás tratar con strings con dobles o triples espacios.
Algunos campos que preguntan por variables numéricas utilizaron la opción de “texto libre” por lo que deberás lidiar con integers, floats y texto en la misma columna. 
Tener en cuenta que el data cleaning que apliquen sobre la data de entrenamiento también va a tener que ser aplicada en la data de testeo. 

Por último, recordá que vamos a poner foco en el futuro, es decir en la precisión de predicciones del 2022.
**Tipo de entregable**: CSV con predicciones (ver ejemplo)

El archivo csv deberá ser enviado por un miembro del equipo a *[datamktsci@rga.com](mailto:datamktsci@rga.com)*. El archivo adjunto deberá contener el número y nombre del equipo.

**IMPORTANTE**
El csv deberá contar con dos columnas: “identificador” y “predicción”.
En donde “identificador” es el identificador único (UUID).<br>

Ejemplo:
|identificador|prediccion|
|--------------|------------|
|71e12df0-d2a0-4557-aab1-591af92d5cde|85000|
|a9a9c4f2-8e17-4d4f-9200-11e831d9ccc3|92000|

#### Análisis de la situación educativa

El principal motivo que nos trae acá, no es solamente poder predecir una variable tan susceptible a inequidades como es la variable *target*, sino explorar diversas vicisitudes que atraviesa el área de la educación.

La idea principal de esta sección es explorar las diferentes inequidades (o presuntas) en la data que observamos. Creemos que en la multiplicidad de perspectivas se dan los avances, por eso te invitamos a explorar y contar la historia que más te interese a vos y a tu grupo.

Un buen *storytelling* no es solamente encontrar un problema, es por eso que te alentamos a elaborar hipótesis o posibles recomendaciones para mejorar el mismo. Recordá que podés incorporar data externa para enriquecer tus descubrimientos y sugerencias.

Algunos disparadores que puedes utilizar son:
(no es necesario que elijas uno en especial, podés elegir la temática que más te interese).

-   ¿Cuánto más/menos ganaría una persona si tuviese estudios igual o mayores a secundarios ?
    
-   ¿Hay diferencias de acceso a la educación/especialización por género?
    
-   ¿Qué zonas presentan mayores desigualdades en el acceso a la educación digital?
    
-   ¿Qué áreas son las que presentan mayor crecimiento en los últimos años? ¿En gente? ¿En dinero?¿Cuánta gente en esas áreas tiene estudios correspondientes?

**Tipo de entregable**: Presentación en Google Slides ([reporte de resultados](https://www.inboundcycle.com/blog-de-inbound-marketing/como-elaborar-informe-para-presentar-resultados-estrategia))

Este entregable será presentado en conjunto con la visualización de datos (entregable 1) al final del evento en una presentación de formato de equipos. Los equipos tendrán libertad de decidir qué miembros de sus equipos presentarán. 

## Recomendaciones generales

-   Explorar el data schema antes del evento para tener una idea de los posibles desafíos a la hora de construir el modelo y posibles inequidades que deseen ser exploradas.

-   ¿Hay material que puedas adelantar antes del evento? Un template de la presentación a preparar puede terminar ahorrando mucho tiempo y ayudándonos a organizarnos antes de comenzar.

-   Si hay alguna temática que te interesa abordar con relación a la educación y conoces algún repositorio público que tenga esa data estaría bueno que la tengas a mano. No vas a conocer la data real hasta el día del evento, pero si tu equipo considera que esta data externa puede enriquecer el análisis siempre es bienvenida. 

-   Tomate un tiempo con tus compañeros para conocerse. La comunicación en este tipo de eventos es fundamental. Planifiquen cómo se van a dividir las tareas y acuerden objetivos en común antes de empezar a codear.

-   Construir de menos a más. Es mejor empezar con un mínimo producto viable (MVP) que funcione, sea un modelo sencillo pero que arroje predicciones o una presentación que cuente una historia sencilla pero coherente, a intentar apuntar a un producto complejo de una y quedar a medio camino.

## Criterios de evaluación

El formato de elección del equipo consistirá en una sumatoria sobre los diferentes entregables.

Máximo puntaje: 30
1.  Data discovery y visualización [Máximo puntaje: 10, Mínimo puntaje: 0]

	a.  Las visualizaciones son claras y adecuadas para mostrar la información presentada. [3,1,0]
    
	b.  El reporte es atractivo y provoca el engage de la audiencia. [2,1,0]
    
	c.  Se presenta la relevancia de las principales variables y su impacto en la predicción de la variable target. [3,1,0]
    
	d.  Se explica con claridad el tratamiento que fue aplicado a los datos y sus razones. [2,1,0]
    
2.  Modelo Predictivo [Máximo puntaje: 8, Mínimo puntaje: 0]

	a.  El puntaje de esta sección será asignado según el rendimiento de los modelos sobre un dataset de prueba. Este análisis será realizado y compartido por el equipo de Data Science de RGA.

3.  Análisis de la situación educativa [Máximo puntaje: 12, Mínimo puntaje: 0]
    
	a.  El reporte logra construir un storytelling acorde a los datos. [3,1,0]
    
	b.  El reporte indaga sobre las diferentes inequidades o sesgos sustentada en los datos [3,1,0]
    
	c.  En base a estas inequidades, se desarrollan recomendaciones relevantes basadas en los datos. [3,1,0]
    
	d.  **Bonus** - Se utilizó data de otras fuentes (válidas) para enriquecer el punto b. [3,0]

## Sponsors

Queremos agradecer a la gente que nos acompañó para que esto sea posible:

- [Argencom](https://www.argencon.org/)

- [Digital House](https://www.digitalhouse.com/ar)

- [Gobierno de la Ciudad de Buenos Aires](https://www.buenosaires.gob.ar/)

- [La Nación](https://www.lanacion.com.ar)

- [Patagonia](https://www.cervezapatagonia.com.ar/)

- [Puerta 18](http://www.puerta18.org.ar/)

- [SysArmy](https://sysarmy.com/blog)

- [Unesco](https://www.buenosaires.iipe.unesco.org/)