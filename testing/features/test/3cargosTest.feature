            # language: es

            Característica: Gestión de cargos
            Módulo responsable de administrar los cargos (trabajos) de una escuela

            Esquema del escenario: ingresar nuevo cargo institucional
            Dado el cargo institucional cuyo "<nombre>" que da título al mismo
            Y que es del "<tipoDesignación>"
            Y que tiene una <cargaHoraria> con la vigencia "<fechaDesde>","<fechaHasta>"
            Y que si el tipo es espacio curricular, opcionalmente se asigna a la división <anio>,<num_división>,"<turno>"
            Cuando se presiona el botón de guardar en cargos
            Entonces se espera el siguiente <status> con la "<respuesta>"

            Ejemplos:
            | nombre            | tipoDesignación    | cargaHoraria | fechaDesde | fechaHasta | anio | num_división | turno   | status | respuesta                                                                                       |
            | Vicedirector      | CARGO              | 36           | 2020-03-01 |            | 0    | 0            | null    | 200    | Cargo de Vicedirector ingresado correctamente                                                   |
            | Preceptor         | CARGO              | 36           | 2020-03-01 |            | 0    | 0            | null    | 200    | Cargo de Preceptor ingresado correctamente                                                      |
            | Auxiliar ADM     | CARGO              | 30           | 2020-03-01 |            | 0    | 0            | null    | 200    | Cargo de Auxiliar ADM ingresado correctamente                                                    |
            | Auxiliar ACAD    | CARGO              | 30           | 2020-03-01 |            | 3    | 2            | Tarde   | 501    | Cargo de Auxiliar ACAD es CARGO y no corresponde asignar división                                |
            | Auxiliar Mate    | CARGO              | 30           | 2020-03-01 |            | 0    | 0            | null    | 200    | Cargo de Auxiliar Mate ingresado correctamente                                                   |
            | Conserje         | CARGO              | 36           | 2023-01-01 |            | 0    | 0            | null    | 200    | Cargo de Conserje ingresado correctamente                                                        |
            | Portero          | CARGO              | 36           | 2023-01-01 |            | 0    | 0            | null    | 200    | Cargo de Portero ingresado correctamente                                                         |
            | Auxiliar DOC     | CARGO              | 30           | 2023-01-01 |            | 0    | 0            | null    | 200    | Cargo de Auxiliar DOC ingresado correctamente                                                    |
            | Matematicas      | ESPACIO_CURRICULAR | 6            | 2020-03-01 |            | 0    | 0            | null    | 501    | Espacio Curricular Matematicas falta asignar división                                            |
            | Derecho          | ESPACIO_CURRICULAR | 5            | 2020-03-01 |            | 4    | 3            | Maniana | 200    | Espacio Curricular Derecho para la división 4º 3º Turno Maniana ingresado correctamente          |
            | Historia         | ESPACIO_CURRICULAR | 4            | 2020-03-01 |            | 5    | 2            | Maniana | 200    | Espacio Curricular Historia para la división 5º 2º Turno Maniana ingresado correctamente         |
            | Geografia        | ESPACIO_CURRICULAR | 3            | 2020-03-01 |            | 3    | 1            | Tarde   | 200    | Espacio Curricular Geografia para la división 3º 1º Turno Tarde ingresado correctamente          |
            | Tecnologia       | ESPACIO_CURRICULAR | 5            | 2020-03-01 |            | 4    | 3            | Maniana | 200    | Espacio Curricular Tecnologia para la división 4º 3º Turno Maniana ingresado correctamente       |
            | Fisica           | ESPACIO_CURRICULAR | 4            | 2020-03-01 |            | 2    | 3            | Maniana | 200    | Espacio Curricular Fisica para la división 2º 3º Turno Maniana ingresado correctamente           |
            | Ingles           | ESPACIO_CURRICULAR | 4            | 2023-01-01 |            | 2    | 3            | Maniana | 200    | Espacio Curricular Ingles para la división 2º 3º Turno Maniana ingresado correctamente           |
            | Astrofisica      | ESPACIO_CURRICULAR | 4            | 2023-01-01 |            | 3    | 1            | Tarde   | 200    | Espacio Curricular Astrofisica para la división 3º 1º Turno Tarde ingresado correctamente        |
            | Matematicas      | ESPACIO_CURRICULAR | 5            | 2020-03-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Matematicas para la división 1º 1º Turno Tarde ingresado correctamente        |
            | Informática      | ESPACIO_CURRICULAR | 2            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Informática para la división 1º 1º Turno Tarde ingresado correctamente        |
            | Teatro           | ESPACIO_CURRICULAR | 2            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Teatro para la división 1º 1º Turno Tarde ingresado correctamente             |
            | Frances          | ESPACIO_CURRICULAR | 3            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Frances para la división 1º 1º Turno Tarde ingresado correctamente            |
            | Literatura       | ESPACIO_CURRICULAR | 5            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Literatura para la división 1º 1º Turno Tarde ingresado correctamente         |
            | Química          | ESPACIO_CURRICULAR | 4            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Química para la división 1º 1º Turno Tarde ingresado correctamente            |
            | Biología         | ESPACIO_CURRICULAR | 5            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Biología para la división 1º 1º Turno Tarde ingresado correctamente           |
            | Música           | ESPACIO_CURRICULAR | 2            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Música para la división 1º 1º Turno Tarde ingresado correctamente             |
            | Artes Plásticas  | ESPACIO_CURRICULAR | 3            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Artes Plásticas para la división 1º 1º Turno Tarde ingresado correctamente    |
            | Filosofía        | ESPACIO_CURRICULAR | 3            | 2023-01-01 |            | 1    | 1            | Tarde   | 200    | Espacio Curricular Filosofía para la división 1º 1º Turno Tarde ingresado correctamente          |
            | Educación Física | ESPACIO_CURRICULAR | 3            | 2023-01-01 |            | 1    | 2            | Maniana | 200    | Espacio Curricular Educación Física para la división 1º 2º Turno Maniana ingresado correctamente |
            | Economía         | ESPACIO_CURRICULAR | 4            | 2023-01-01 |            | 2    | 2            | Maniana | 200    | Espacio Curricular Economía para la división 2º 2º Turno Maniana ingresado correctamente         |
            | Ética            | ESPACIO_CURRICULAR | 2            | 2023-01-01 |            | 1    | 2            | Maniana | 200    | Espacio Curricular Ética para la división 1º 2º Turno Maniana ingresado correctamente            |
            | Psicología       | ESPACIO_CURRICULAR | 3            | 2023-01-01 |            | 3    | 1            | Tarde   | 200    | Espacio Curricular Psicología para la división 3º 1º Turno Tarde ingresado correctamente         |
            | Sociología       | ESPACIO_CURRICULAR | 3            | 2023-01-01 |            | 1    | 2            | Maniana | 200    | Espacio Curricular Sociología para la división 1º 2º Turno Maniana ingresado correctamente       |