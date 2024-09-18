         # language: es

         Característica: Emitir el parte diario de licencias de una escuela para un determinado día

         Escenario: Verificar el funcionamiento de licencias para un día
         Dada la existencia de las siguientes licencias
         | dni      | nombre  | apellido   | articulo | descripcion                | desde      | hasta      |
         | 88100000 | Raúl    | Orellanos  | 5A       | ENFERMEDAD CORTA EVOLUCIÓN | 2023-05-07 | 2023-05-15 |
         | 88200000 | Matías  | Barto      | 5A       | ENFERMEDAD CORTA EVOLUCIÓN | 2023-05-10 | 2023-05-15 |
         | 88300000 | Andrea  | Sosa       | 5A       | ENFERMEDAD CORTA EVOLUCIÓN | 2023-05-11 | 2023-06-17 |
         | 88400000 | Laura   | Barrientos | 23A      | ATENCION FAMILIAR          | 2023-05-08 | 2023-10-16 |
         | 88500000 | Natalia | Zabala     | 23A      | ATENCION FAMILIAR          | 2023-05-13 | 2023-10-22 |
         Y que se otorgan las siguientes nuevas licencias
         | dni      | nombre  | apellido | articulo | descripcion          | desde      | hasta      |
         | 88600000 | Marta   | Ríos     | 36A      | ASUNTOS PARTICULARES | 2023-05-15 | 2023-05-15 |
         | 88700000 | Rosalía | Ramón    | 36A      | ASUNTOS PARTICULARES | 2023-05-15 | 2023-05-15 |
         | 88800000 | José    | Pérez    | 36A      | ASUNTOS PARTICULARES | 2023-05-15 | 2023-05-15 |
         Cuando se solicita el parte diario para la fecha "2023-05-15"
         Entonces el sistema responde

          """
            [{"dni":"99100000","nombre":"Ermenegildo","apellido":"Sabat","articulo":"5A","descripcion":"ENFERMEDAD CORTA EVOLUCIÓN","desde":"2023-05-07","hasta":"2023-05-17"},
            {"dni":"20200200","nombre":"Susana","apellido":"Álvarez","articulo":"5A","descripcion":"ENFERMEDAD CORTA EVOLUCIÓN","desde":"2023-05-12","hasta":"2023-05-30"},
            {"dni":"88100000","nombre":"Raúl","apellido":"Orellanos","articulo":"5A","descripcion":"ENFERMEDAD CORTA EVOLUCIÓN","desde":"2023-05-07","hasta":"2023-05-15"},
            {"dni":"88200000","nombre":"Matías","apellido":"Barto","articulo":"5A","descripcion":"ENFERMEDAD CORTA EVOLUCIÓN","desde":"2023-05-10","hasta":"2023-05-15"},
            {"dni":"88300000","nombre":"Andrea","apellido":"Sosa","articulo":"5A","descripcion":"ENFERMEDAD CORTA EVOLUCIÓN","desde":"2023-05-11","hasta":"2023-05-17"},
            {"dni":"88400000","nombre":"Laura","apellido":"Barrientos","articulo":"23A","descripcion":"ATENCIÓN FAMILIAR","desde":"2023-05-08","hasta":"2023-05-16"},
            {"dni":"88500000","nombre":"Natalia","apellido":"Zabala","articulo":"23A","descripcion":"ATENCIÓN FAMILIAR","desde":"2023-05-13","hasta":"2023-05-22"}]
         """
         Escenario: Verificar el parte diario luego de trasncurridos 2 días
         Dada la existencia de las siguientes licencias

         | dni      | nombre      | apellido | articulo | descripcion                | desde      | hasta      |
         | 99100000 | Ermenegildo | Sabat    | 5A       | ENFERMEDAD CORTA EVOLUCIÓN | 2023-05-07 | 2023-05-17 | 
         | 20200200 | Susana      | Álvarez  | 5A       | ENFERMEDAD CORTA EVOLUCIÓN | 2023-05-12 | 2023-05-30 | 
         | 88300000 | Andrea      | Sosa     | 5A       | ENFERMEDAD CORTA EVOLUCIÓN | 2023-05-11 | 2023-06-17 |
         | 88500000 | Natalia     | Zabala   | 23A      | ATENCION FAMILIAR          | 2023-05-13 | 2023-10-22 |
         Cuando se solicita el parte diario para la fecha "2023-05-17"
         Entonces el sistema responde
         """
        [
         {"dni":"99100000","nombre":"Ermenegildo","apellido":"Sabat","articulo":"5A","descripcion":"ENFERMEDAD CORTA EVOLUCIÓN","desde":"2023-05-07","hasta":"2023-05-17"},
         {"dni":"20200200","nombre":"Susana","apellido":"Álvarez","articulo":"5A","descripcion":"ENFERMEDAD CORTA EVOLUCIÓN","desde":"2023-05-12","hasta":"2023-05-30"},
         {"dni": "88300000", "nombre": "Andrea", "apellido": "Sosa","articulo": "5A", "descripcion": "ENFERMEDAD CORTA EVOLUCIÓN","desde": "2023-05-11", "hasta": "2023-05-17"},
         {"dni": "88500000", "nombre": "Natalia", "apellido": "Zabala","articulo": "23A", "descripcion": "ATENCIÓN FAMILIAR","desde": "2023-05-13", "hasta": "2023-05-22"}
         ]
         """

