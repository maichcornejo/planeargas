                  # language: es

                  Característica: Emitir el Reporte de Concepto de una persona.

                  Escenario: Verificar el funcionamiento de Reporte de Concepto
                  Dada los reportes de concepto del 2024
                  Cuando se solicita el Reporte de Concepto para el 2024
                  Entonces el sistema responde con un reporte
                   """
  {
    "data": [
      {"personaId": 10845, "nombre": "Rosalía", "apellido": "Fernandez", "licenciasPedidas": 1, "licenciasOtorgadas": 1, "designacionesPedidas": 1, "designacionesOtorgadas": 1, "cantDiasLicenciaOtorgada": 10, "cantDiasLicenciaPedidos": 10},
      {"personaId": 10857, "nombre": "Lucas", "apellido": "San Martin", "licenciasPedidas": 5, "licenciasOtorgadas": 3, "designacionesPedidas": 5, "designacionesOtorgadas": 4, "cantDiasLicenciaOtorgada": 29, "cantDiasLicenciaPedidos": 46},
      {"personaId": 10858, "nombre": "Facundo", "apellido": "Español", "licenciasPedidas": 3, "licenciasOtorgadas": 3, "designacionesPedidas": 3, "designacionesOtorgadas": 3, "cantDiasLicenciaOtorgada": 3, "cantDiasLicenciaPedidos": 3},
      {"personaId": 10864, "nombre": "Julia", "apellido": "Martinez", "licenciasPedidas": 1, "licenciasOtorgadas": 1, "designacionesPedidas": 1, "designacionesOtorgadas": 1, "cantDiasLicenciaOtorgada": 3, "cantDiasLicenciaPedidos": 3}
    ],
    "message": "OK",
    "status": 200
  }
  """