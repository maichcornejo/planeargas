
            # language: es
            Característica: Gestión de personas
            Módulo responsable de administrar a las personas del sistema

            Esquema del escenario: ingresar nuevas personas
            Dada la persona con "<nombre>","<apellido>","<dni>","<cuil>","<sexo>","<titulo>","<domicilio>","<telefono>"
            Cuando se presiona el botón de guardar
            Entonces se espera el siguiente <status> con la "<respuesta>"

            Ejemplos:
            | dni      | nombre      | apellido     | cuil        | sexo | titulo                    | domicilio            | telefono           | status | respuesta                                                      |
            | 10100100 | Alberto     | Lopez        | 27101001009 | M    | Profesor de Biología      | Charcas 54           | +54 (280) 411-1111 | 200    | Alberto Lopez con DNI 10100100 ingresado/a correctamente       |
            | 20200200 | Susana      | Álvarez      | 20202002009 | F    | Profesora de historia     | Mitre 154            | +54 (280) 422-2222 | 200    | Susana Álvarez con DNI 20200200 ingresado/a correctamente      |
            | 30300300 | Pedro       | Benítez      | 27303003009 | M    |                           | Jujuy 255            | +54 (280) 433-3333 | 200    | Pedro Benítez con DNI 30300300 ingresado/a correctamente       |
            | 40400400 | Marisa      | Amuchástegui | 20404004009 | F    | Profesora de historia     | Zar 555              | +54 (280) 444-4444 | 200    | Marisa Amuchástegui con DNI 40400400 ingresado/a correctamente |
            | 50500500 | Raúl        | Gómez        | 27505005009 | M    | Profesor de Geografía     | Roca 2458            | +54 (280) 455-5555 | 200    | Raúl Gómez con DNI 50500500 ingresado/a correctamente          |
            | 60600600 | Inés        | Torres       | 20606006009 | F    | Licenciada en Geografía   | La Pampa 322         | +54 (280) 466-6666 | 200    | Inés Torres con DNI 60600600 ingresado/a correctamente         |
            | 70700700 | Jorge       | Dismal       | 27707007009 | M    |                           | Mitre 1855           | +54 (280) 477-7777 | 200    | Jorge Dismal con DNI 70700700 ingresado/a correctamente        |
            | 20000000 | Rosalía     | Fernandez    | 20200000009 | F    | Maestra de grado          | Maiz 356             | +54 (280) 420-0000 | 200    | Rosalía Fernandez con DNI 20000000 ingresado/a correctamente   |
            | 80800800 | Analía      | Rojas        | 20808008009 | F    | Técnica superior          | Rosa 556             | +54 (280) 488-8888 | 200    | Analía Rojas con DNI 80800800 ingresado/a correctamente        |
            | 99100000 | Ermenegildo | Sabat        | 20991000009 | M    | Licenciado en Fisica      | 25 de mayo 555       | +54 (280) 433-9871 | 200    | Ermenegildo Sabat con DNI 99100000 ingresado/a correctamente   |
            | 99200000 | María Rosa  | Gallo        | 20992000009 | F    | Licenciada en Matematica  | San Martin 1882      | +54 (280) 421-5475 | 200    | María Rosa Gallo con DNI 99200000 ingresado/a correctamente    |
            | 99300000 | Homero      | Manzi        | 20993000009 | M    | Técnico superior          | Belgrano 761         | +54 (280) 412-8618 | 200    | Homero Manzi con DNI 99300000 ingresado/a correctamente        |
            | 99999999 | Raúl        | Guitierrez   | 20999999999 | M    | Maestro de grado          | Albarracin 1361      | +54 (280) 512-8518 | 200    | Raúl Guitierrez con DNI 99999999 ingresado/a correctamente     |
            | 88888888 | Marisa      | Balaguer     | 27888888889 | F    | Maestra de grado          | Moreno 89            | +54 (280) 412-1121 | 200    | Marisa Balaguer con DNI 88888888 ingresado/a correctamente     |
            | 88100000 | Raúl        | Orellanos    | 20881000009 | M    | Licenciado en Física      | Calle 123, Ciudad    | +54 11 1234-5678   | 200    | Raúl Orellanos con DNI 88100000 ingresado/a correctamente      |
            | 88200000 | Matías      | Barto        | 20882000009 | M    | Profesor de Matemáticas   | Avenida 456, Pueblo  | +54 11 9876-5432   | 200    | Matías Barto con DNI 88200000 ingresado/a correctamente        |
            | 88300000 | Andrea      | Sosa         | 27883000009 | F    | Ingeniera Química         | Calle 789, Villa     | +54 11 5678-1234   | 200    | Andrea Sosa con DNI 88300000 ingresado/a correctamente         |
            | 88400000 | Laura       | Barrientos   | 27884000009 | F    | Doctora en Biología       | Avenida 012, Barrio  | +54 11 4321-8765   | 200    | Laura Barrientos con DNI 88400000 ingresado/a correctamente    |
            | 88500000 | Natalia     | Zabala       | 27885000009 | F    | Licenciada en Historia    | Calle 345, Localidad | +54 11 2109-8765   | 200    | Natalia Zabala con DNI 88500000 ingresado/a correctamente      |
            | 45380520 | Lucas       | San Martin   | 20453805205 | M    | Licenciado en Informatica | Albarracin 723       | 2804725250         | 200    | Lucas San Martin con DNI 45380520 ingresado/a correctamente    |
            | 45682000 | Facundo     | Español      | 20456820000 | M    | Licenciado en Informatica | Doradillo            | 126961675          | 200    | Facundo Español con DNI 45682000 ingresado/a correctamente     |
            | 42033100 | Romina      | Lopez        | 27420331009 | F    | Doctora en Biología       | 25 de mayo 123       | +54 11 6745-4113   | 200    | Romina Lopez con DNI 42033100 ingresado/a correctamente        |
            | 43987413 | Lautaro     | Martinez     | 20439874135 | M    | Ingeniero Civil           | La Pampa 863         | +54 11 4409-1265   | 200    | Lautaro Martinez con DNI 43987413 ingresado/a correctamente    |
            | 40800212 | Maia        | Cornejo      | 27408002120 | F    | Licenciada en Informatica | Estivariz 745,       | 2804841251         | 200    | Maia Cornejo con DNI 40800212 ingresado/a correctamente        |
            | 42234951 | Mauro       | Fernandez    | 20422349515 | M    | Licenciado en Química     | Belgrano 23          | 280461823          | 200    | Mauro Fernandez con DNI 42234951 ingresado/a correctamente     |
            | 40112000 | Francisco   | Gomez        | 20401120005 | M    | Enfermero                 | Av Rawson 1130       | 9912313123         | 200    | Francisco Gomez con DNI 40112000 ingresado/a correctamente     |
            | 40987654 | Julia       | Martinez     | 27409876540 | F    | Contadora Pública         | Mitre 456            | 2804856789         | 200    | Julia Martinez con DNI 40987654 ingresado/a correctamente      |
            | 43322112 | Marcos      | Perez        | 20433221125 | M    | Médico                    | Rivadavia 789        | 2804678921         | 200    | Marcos Perez con DNI 43322112 ingresado/a correctamente        |