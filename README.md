<<<<<<< HEAD
### Laboratorio de Programación y Lenguajes
### Trabajo Práctico
# Novedades Docentes Secundarios

Para la instalación y configuración del entorno de desarrollo es necesario seguir el siguiente 
<a href="https://git.fi.mdn.unp.edu.ar/labprog/core/infraestructura-tps/-/blob/master/README.md" target="_blank">INSTRUCTIVO</a>

---

## Problema Planteado
La escuela 775 de la ciudad de Puerto Madryn Dicta materias de nivel secudario según las normativas del Ministerio de Educación de la  Provincia del Chubut.
La escuela cuenta con un espacio aúlico en el que se asignan las distintas divisiones de 1º a 6º año en la que se dictan durante la semana las distintas asignaturas según la currícula académica de cada año.
Los docentes mediante la asignación de cargos se les asigna el dictado de las distintas asignaturas (materias) para cada año en las distintas divisiones con un cronograma horario según la carga de la asignatura distribuida en los días de la semana.

Según las normas vigentes del Ministerio de Educación existe un reglamento o manual del docente entre los que se encuantra la reglamentación de los distíntos artículos de licencias que puede solicitar cada docente. Los mismos expresan las distintas reglas que deben respetar para poder ser otorgados.

## Objetivo de solución
Proveer una herramienta de gestión de novedades de licencias solicitadas por los docentes, permitiendo generar el "parte diario de novedades del personal".

La solución debe administrar los tipos de designación, las divisiones y los cargos que representan la cobertura completa de cargos y espacios curriculares de la escuela para cada división año y turno. La designación de docentes a los cargos y los espacios curriculares.

La misión principal de la aplicación será la de gestionar las novedades de las licencias solicitadas por el personal de la escuela, la verificación del cumplimiento y requisitos para otorgar la misma, la trazabilidad de actividades de novedades y la emisión de las planillas respectivas de novedades, tanto las diarias como las anuales para conformación del concepto del personal.

## La solución requiere
### Administración de Designaciones
La solución contará con una administración básica de altas bajas, modificaciones y consultas (_ABMC_) de:
1. **Tipos de designación** --> representa a todos los cargos y espacios curriculares disponibles o que han estado disponibles en la escuela.
1. **Divisiones** --> representa todas las divisiones que existen en la escuela indicando el año, numero, turno y vigencia de la misma.
1. **Cargo** --> es la gestión de asociación de los tipos de designación que existen en la escuela, tanto de cargos como de espacios curriculares. Si se trata de un espacio curricular se deberá asignar la división donde se dicta el espacio. Representa todas las instancias de cargos y espacios curriculares de la escuela. Se cuenta con vigencia que representa a los distintos planes o diseños curriculares implementados en los distintos años de la vida de la escuela.

### Administración del Personal
Para el correcto funcionamiento de información de la escuela es muy importante conocer el detalle de personas (personal) que trabaja o trabajó en la escuela, como así sus sucesivas designaciones a los cargos o espacios curriculares.

Para ello la aplicación deberá contar con la administración básica (ABMC) de Personas que representa al personal de la escuela.

También deberá contar con la gestión de designaciones de dichas personas a los cargos, que bien podrá ser un cargo o un espacio curricular. La gestión de designaciones se realizará mediante novedades de altas y bajas del personal.

La administración del personal deberá realizar todas las validaciones y verificaciones requeridas para garantizar la consistencia de información del personal que trabaja en la escuela.

En el caso de una suplencia se deberá administrar por este mismo mecanismo ingresando el alta de la nueva persona y asignando a un cargo. La aplicación nuevamente deberá garantizar la consistencia de la misma, en este caso en particular verificar que para la misma designación existe una licencia otorgada a la persona del cargo o espacio curricular.

### Administración de Licencias
El proceso de otorgamiento de una licencia estará sujeto primero a la correcta presentación de la misma y la debidas garantías validadas por la secretaría de la escuela. Una vez superada esta fase administrativa se procederá al ingreso de la licencia en el sistema, indicando la persona solicitante y el período solicitado.

Como resultado del ingreso la aplicación deberá correr el _*Proceso de validación de Licencia*_ que indica como resultado todas las verificaciones de consistencia del otorgamiento de la misma. La secretaría, pese a las advertencias del sistema, puede otorgar igualmente la licencia y el sistema deberá registrar dicha condición.

### Informes
La aplicación deberá como mínimo generar los siguientes informes:
+ Parte diario de licencias.
+ Informe anual de concepto del personal.
+ Mapa de horarios y designaciones por división.
+ Reporte de espacios curriculares sin cubrir, ya se por falta de designación como por licencia.

## Criterio de satisfacción
### Casos y ejemplos de verificación
La verificación de calidad se realizará utilizando las siguientes premisas para un conjunto de pruebas a realizar:
* Contar con todos los cargos y espacios curriculares actuales de la Escuela 775.
* Contar con todas las divisiones para todos los turnos que existen actualmente en la escuela 775.
* Genarar al menos 6 cargos de cargos.
* Generar al menos 25 cargos de espacios curriculares repartidas entre todas las divisiones.
* Generar el alta de al menos 10 personas nuevas a la escuela, contemplando las siguientes condiciones:
  + 2 personas en cargos de designación de cargo NO cubiertas en el período indicado.
  + 1 persona en un cargo que YA cuenta con una designación para el mismo período. Informar el error respectivo y abortar la transacción.
  + 2 personas en cargos de espacio curricular NO cubiertas en el período indicado.
  + 1 persona en cargo de espacio curricular que YA cuenta con designación por otra persona para el mismo período. Informar el error respectivo y abortar la transacción.
  + 1 persona en cargo que cubre una licencia de otra persona en la misma designación. Infomar que está correcto y que reemplaza al docente que solicitó licencia.
  + 1 persona en cargo que cubre una licencia de otra persona en la misma designación, pero que no coincide el mismo período. Infomar el error respectivo y abortar la transacción.
  + 1 persona en cargo de espacio curricular que cubre una licencia de otra persona en la misma designación. Infomar que está correcto y que reemplaza al docente que solicitó licencia.
  + 1 personas en cargo de espacio curricular que cubre una licencia de otra persona en la misma designación, pero que no coincide el mismo período. Infomar el error respectivo y abortar la transacción.
* Generar el otorgamiento de Licencias con las siguientes condiciones:
  + Distintas licencias según las reglas de los distintos artículos. la menos 1 Verificación positiva por cada artículo. al menos 2 verificaciones negativas por cada artículo, demostración la violación de las condiciones de los artículos. Por ejemplo topes.
  + Licencia de 2 personas en espacios curriculares en rango de períodos que NO tienen horario previsto (no están en la escuela en el día o días solicitados).
  + Licencia a docente no designado.
  + Licencia de una licencia YA otorgada.
* Parte diario
  1. Otorgar 5 licencia para fechas previas con vigencia de al menos 15 días. y que permanezcan vigentes hasta el otorgamiento siguiente.
  2. Otorgar 3 licencias para la fecha de hoy.
    + Emitir el parte diario y verificar que muestra los 8 docentes en cuestión.
  3. Dejar pasar el tiempo hasta que caduquen las licencias de al menos 2 personas del punto 1.
    + Emitir el parte diario y verificar que la persona ya no sale más en el mismo.
  4. Designar un suplente para al menos 3 cargos de los de licencia.
    + Emitir el parte diario que deberá indicar la persona de licencia y la persona que lo reemplaza.
* Reporte de concepto
  1. generar traza de licencias para al menos 20 docentes distribuidas a lo largo del año, especialmente considerando los artículos imputables al concepto.
    + Emitir el reporte de concepto para cada docente y verificar lso resultados esperados según la documentación relevada,
* Calendario de espacios curriculares y docente asignado. Deberá mostrar la semana calendario de lunes a viernes para un turno (por ejemplo mañana) mostrando el horario de 1º hora a 8º hora y que espacio curricular y docente la ocupan.

## Modelo de Dominio propuesto
![](diagram.png)
=======
## Laboratorio de Programación y Lenguajes

### Departamento de Informática - FI-UNPSJB-PM

## Instalación y configuración del entorno de desarrollo

> ESTE LABORATORIO ESTÁ PREPARADO Y PROBADO PARA SER DESARROLLADO SOBRE SISTEMAS **LINUX**, ES REQUERIMIENTO DE LA ASIGNATURA FAMILIARIZARSE CON EL MISMO.
>
> Quien no cuente con el mismo en sus máquinas la cátedra sugiere dos posibles aproximaciones:
> 1. (Recomendada) Instalar cualquier distro Linux dual-boot.
> 2. Instalar el sistema en una máquina virtual

> En la raíz de este directorio existe el script ´lpl´ para facilitar la ejecución de varios comandos. En el presente instructivo se indicará en cada paso, si corresponde, la opción de ejecución mediante este script. 

## Setup

### Software necesario previamente

1. Instalar [Git](https://git-scm.com/download/linux)

1. Instalar [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) y [Docker Compose](https://docs.docker.com/compose/install/)
    > **¡CONFIGURACIÓN IMPORTANTE ANTES DE CONTINUAR!**
    >
    1. No olvidar los pasos de post instalación para ejecutar docker sin priviliegios de `root`.
        ```sh
        sudo groupadd docker
        sudo usermod -aG docker $USER
        ```
        Para hacer efectivos los cambios en los grupos, reiniciar la terminal o ejecutar
        ```sh
        newgrp docker
        ```
    1. *Opcional:* Para que docker no arranque de forma automática al inicio:
        ```sh
        sudo systemctl disable docker.service
        sudo systemctl disable containerd.service
        ```
    1. Crear el archivo `/etc/docker/daemon.json` con el siguiente conenido:
        ```json
        {
          "userns-remap": "TU_NOMBRE_DE_USUARIO"
        }
        ```
    1. Editar los archivos `/etc/subuid` y `/etc/subgid`. Agregar la línea:
        ```
        TU_NOMBRE_DE_USUARIO:1000:65536
        ```

1. Iniciar servicio docker `sudo systemctl start docker`
    > Este comando puede variar según la distro de linux utilizada.

1. Instalar [Postman](https://www.postman.com/downloads/) y [DBeaver](https://dbeaver.io/download/)

1. Instalar un editor de texto para escribir el código, se recomienda [VS Code](https://code.visualstudio.com/download).

### Configuración de usuario de Gitlab

1. Genera una clave pública y agregarla al repo desde settings/ssh keys en Gitlab. Seguir este [instructivo](https://git.fi.mdn.unp.edu.ar/help/ssh/README#generating-a-new-ssh-key-pair)

### Obtener el código para trabajar

1. Realizar el **Fork** y dirigirse al repositorio nuevo.

1. Desde la línea de comandos, clonar este repositorio con la url ssh. 
    ```sh
    git clone ssh://git@git.fi.mdn.unp.edu.ar:30000/<repo>`
    ```

1. Ir al directorio clonado `cd <repo_dir>`

1. Dar permisos de ejecución al script `lpl`: `chmod +x lpl`.

1. Hacer el build de las imágenes Docker `./lpl build` 

1. Levantar los servidores `./lpl up`
      > Este paso toma un tiempo debido a que debe descargar las dependencias del proyecto. Para monitorear el progreso utilizar `./lpl logs`.
      >
      > Cuando la aplicación esté lista se verá el mensaje:
      >
      > `backend | [...] Started BackendApplication in xxx seconds`

1. Verificar funcionamiento ingresando a http://localhost:8080/ . Si todo funciona correctamente debería responder el siguiente JSON:
      ```json
      {
      "data": "Hello Labprog!",
      "message": "Server Online",
      "status": 200
      }
      ```
1. Crear el proyecto Angular en el front:
    ```sh
    $ ./lpl sh frontend
    [frontend:node]$ ng new cli --minimal -S -g --defaults 
    ```

1. Detener los servidores `./lpl down`

1. Descomentar linea indicadas en `docker-compose.yml`.

1. Levantar los servidores `./lpl up`

1. Verificar funcionamiento ingresando a http://localhost:4200/ .

Aquí finaliza la instalación y configuración del ambiente de desarrollo, a continuación se detallan los pasos para comenzar con el desarrollo.

## Desarrollar con Docker

Para los siguientes pasos asegurarse de que el servicio de Docker esté corriendo, se puede ejecutar el comando `docker ps`.

El script `lpl` en la raíz del repositorio tiene una serie de comandos útiles abreviados para asistir en el proceso de desarrollo.

### Conectarse a los servidores por línea de comandos

Para conectarse al servidor **backend**, una vez corriendo los servicios, ejecutar: ```./lpl sh backend```

De la misma forma es posible conectarse a cualquiera de los contenedores solo indicando el nombre del mismo.

### Detener los servicios

Para detener los servicios configurados en el archivo de docker-compose ejecutar: ```./lpl down```

El siguiente comando es para detener por completo el servicio de docker. En este caso, si los servicios están corriendo se detendrán y cuando docker sea iniciado nuevamente, estos contenedores serán levantados de forma automática.

`sudo systemctl stop docker`

## Desarrollar en Java en el backend

El servidor de backend despliga automáticamente el código compilado. Luego de modificar los archivos locales se debe ejecutar el siguiente comando:

1. `./lpl compile`

Esto compilará el código en el servidor. Si no hay errores de compilación se desplegará al instante.

En ciertas ocaciones, debido a algún error de compilación que haya sido corregido, es posible que el backend no vuelva a desplegar la aplicación. En este caso, sólo es necesario reiniciar el backend.

1. `./lpl restart backend`

## Staging de datos

> PENDIENTE

## Stack tecnológico
Además de cumplir con los requerimientos funcionales planteados en cada TP, el desarrollo de la aplicación deberá garantizar las siguientes premisas:
* Usar JPA como método de persistencia del modelo de datos. Para las consultas a la base de datos se deberá utilizar JPQL.
* Diseñar la aplicación utilizando los principios de los patrones de Separación en capas &rarr; Layered y N-Tiers.
* La aplicación deberá garantizar transacciones ACID. Especialmente para los procesos.
* Siempre que se pueda y deba, garantizar los principios SOLID de la programación Orientada a Objetos. (SRP, OCP, LSP, ISP, DIP).
* El stack tecnológico requerido para la solución contempla el uso de:
  + **Git** para el control de versiones y distribución del código.
  + **Docker** para la administración de la virtualización en contenedores de los servidores.
  + **Docker compose** pra la coordinación de multiples contenedores.
  + **Angular**  para el desarrollo de la aplicación frontend en javascript.
  + **Spring Boot** para el desarrollo de la aplicación backend en java.
  + **JPA** como ORM para la implementación del modelo.
  + **Postgres** cómo motor de base de datos.
  + **Cucumber-js** para el testing de los servicios REST.
* La gestión de tablas se realizará exclusivamente desde el modelo provisto a continuación y generado desde el ORM. **No se permite ingeniería inversa desde la DB.**

## Forma de entrega
* El trabajo será realizado en forma individual. Se podrá trabajar colaborativamente con otros compañeros.
* El trabajo práctico deberá ser entregado de la siguiente forma:
  * Todo el sitema completo debe ser entrega mediante el proyecto en Git.
  * Bitacora del desarrollo que incluya: Toma de decisiones de la arquitectura de la solución, restricciones de uso y relato del detalle de la evolución del desarrollo. En formato Wiki o Markdown. Este informe debería ser evolutivo en el transcurso del desarrollo del TP.
  * Toda la bibliografía utilizada deberá ser referenciada indicando título y autor, en una sección dedicada a tal efecto.
  * El diseño con el que se aborda la solución al problema planteado. En el caso de utilizar patrones, cuales de ellos utilizó y en qué contexto.
  * El programa de aplicación que implementa la solución mediante el cumplimiento efectivo de los test planteados en las features de BDD.
  * El código fuente debe estar sincronizado en git todo el tiempo para que la cátedra acceda al mismo y pueda verificar permanenetente los avances.

## Forma de aprobación
Se tendrá en cuenta para la aprobación del trabajo práctico y los integrantes del grupo:
1. Planificación del desarrollo de la aplicación. Cumplimiento de las etapas previstas.
2. Funcionamiento de la aplicación desarrollada. Se evaluará si la funcionalidad cumple con lo solicitado, en función de test de Criterios de Aceptación escritos en las features BDD.
3. Estructura general de la presentación, su legibilidad y facilidad de lectura y comprensión.
4. Contenido del informe y el uso de la información técnica para elaborarlo.




>>>>>>> 366618d8 (primer actualizacion melli)

