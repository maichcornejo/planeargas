            # language: es

            Característica: Gestión de divisiones
            Módulo responsable de administrar a las divisiones (espacios físicos) de una escuela

            Esquema del escenario: ingresar nueva división
            Dada la el espacio físico división con <anio>,<numDivision>,"<orientación>","<turno>"
            Cuando se presiona el botón de guardar en divisiones
            Entonces se espera el siguiente <status> con la "<respuesta>" en divisiones

            Ejemplos:
            | anio | numDivision | orientación | turno   | status | respuesta                                            |
            | 5    | 2           | Biológicas  | Maniana | 200    | División 5º 2º turno Maniana ingresada correctamente |
            | 3    | 1           | Sociales    | Tarde   | 200    | División 3º 1º turno Tarde ingresada correctamente   |
            | 3    | 2           | Sociales    | Tarde   | 200    | División 3º 2º turno Tarde ingresada correctamente   |
            | 1    | 1           | Matemáticas | Tarde   | 200    | División 1º 1º turno Tarde ingresada correctamente   |
            | 4    | 3           | Tecnología  | Maniana | 200    | División 4º 3º turno Maniana ingresada correctamente |
            | 2    | 3           | Física      | Maniana | 200    | División 2º 3º turno Maniana ingresada correctamente |
            | 1    | 1           | Exactas     | Maniana | 200    | División 1º 1º turno Maniana ingresada correctamente |
            | 1    | 2           | Exactas     | Maniana | 200    | División 1º 2º turno Maniana ingresada correctamente |
            | 1    | 3           | Exactas     | Maniana | 200    | División 1º 3º turno Maniana ingresada correctamente |
            | 2    | 1           | Exactas     | Maniana | 200    | División 2º 1º turno Maniana ingresada correctamente |
            | 2    | 2           | Exactas     | Maniana | 200    | División 2º 2º turno Maniana ingresada correctamente |
            | 3    | 1           | Exactas     | Maniana | 200    | División 3º 1º turno Maniana ingresada correctamente |
            | 3    | 2           | Exactas     | Maniana | 200    | División 3º 2º turno Maniana ingresada correctamente |
            | 3    | 3           | Exactas     | Maniana | 200    | División 3º 3º turno Maniana ingresada correctamente |
            | 4    | 1           | Exactas     | Maniana | 200    | División 4º 1º turno Maniana ingresada correctamente |
            | 4    | 2           | Exactas     | Maniana | 200    | División 4º 2º turno Maniana ingresada correctamente |
            | 5    | 1           | Exactas     | Maniana | 200    | División 5º 1º turno Maniana ingresada correctamente |
            | 5    | 3           | Exactas     | Maniana | 200    | División 5º 3º turno Maniana ingresada correctamente |
            | 6    | 1           | Exactas     | Maniana | 200    | División 6º 1º turno Maniana ingresada correctamente |
            | 6    | 2           | Exactas     | Maniana | 200    | División 6º 2º turno Maniana ingresada correctamente |
            | 6    | 3           | Exactas     | Maniana | 200    | División 6º 3º turno Maniana ingresada correctamente |
            | 1    | 1           | Humanidades | Noche   | 200    | División 1º 1º turno Noche ingresada correctamente   |
            | 1    | 2           | Humanidades | Noche   | 200    | División 1º 2º turno Noche ingresada correctamente   |
            | 1    | 3           | Humanidades | Noche   | 200    | División 1º 3º turno Noche ingresada correctamente   |
            | 2    | 1           | Humanidades | Noche   | 200    | División 2º 1º turno Noche ingresada correctamente   |
            | 2    | 2           | Humanidades | Noche   | 200    | División 2º 2º turno Noche ingresada correctamente   |
            | 2    | 3           | Humanidades | Noche   | 200    | División 2º 3º turno Noche ingresada correctamente   |
            | 3    | 1           | Humanidades | Noche   | 200    | División 3º 1º turno Noche ingresada correctamente   |
            | 3    | 2           | Humanidades | Noche   | 200    | División 3º 2º turno Noche ingresada correctamente   |
            | 3    | 3           | Humanidades | Noche   | 200    | División 3º 3º turno Noche ingresada correctamente   |
            | 4    | 1           | Humanidades | Noche   | 200    | División 4º 1º turno Noche ingresada correctamente   |
            | 4    | 2           | Humanidades | Noche   | 200    | División 4º 2º turno Noche ingresada correctamente   |
            | 4    | 3           | Humanidades | Noche   | 200    | División 4º 3º turno Noche ingresada correctamente   |
            | 5    | 1           | Humanidades | Noche   | 200    | División 5º 1º turno Noche ingresada correctamente   |
            | 5    | 2           | Humanidades | Noche   | 200    | División 5º 2º turno Noche ingresada correctamente   |
            | 5    | 3           | Humanidades | Noche   | 200    | División 5º 3º turno Noche ingresada correctamente   |
            | 6    | 1           | Humanidades | Noche   | 200    | División 6º 1º turno Noche ingresada correctamente   |
            | 6    | 2           | Humanidades | Noche   | 200    | División 6º 2º turno Noche ingresada correctamente   |
            | 6    | 3           | Humanidades | Noche   | 200    | División 6º 3º turno Noche ingresada correctamente   |