<<<<<<< HEAD
Documento de Visión “PlaneAr Gas” Alumnas: Pacheco Melisa, Maia Cornejo. Cátedra: Ernesto Mayorga, Cristian Pacheco. Desarrollo de Software UNPSJB - Puerto Madryn

Introducción Este documento describe la visión para una aplicación diseñada para ayudar a los gasistas matriculados a realizar planos de gas en PDF de manera sencilla. Proporcionando información básica al programa, este diseñará, calculará y presentará los planos en un formato que respete las normas vigentes, como la NAG-200, las normas ISO, y las disposiciones establecidas por el ENARGAS (Ente Nacional Regulador del Gas Argentino). Problemática El proceso de realización de planos de gas en Argentina es actualmente complejo y requiere la intervención de especialistas en dibujo técnico, cálculos de instalaciones, ventilación y normas vigentes. Este enfoque manual puede dar lugar a errores que resulten en el rechazo de planos por parte del ente regulador, compras incorrectas de materiales y demoras en la ejecución de la obra, generando así un impacto económico negativo tanto para el gasista matriculado como para el propietario de la obra. Solución propuesta Para simplificar este proceso, proponemos la creación de la aplicación “PlaneAr Gas”, diseñada para ayudar a los gasistas matriculados a generar planos de instalaciones de gas para viviendas unifamiliares de manera sencilla y cumpliendo con las normativas vigentes en Argentina. Mediante el uso de esta aplicación, los usuarios podrán cargar una planta de arquitectura, la cual será reconocida por colores para producir automáticamente un plano integral listo para presentar al ente regulador. Este incluirá una visualización detallada de la planta original, una perspectiva isométrica de la instalación, una lista de materiales y artefactos necesarios, y una tabla con los cálculos pertinentes, todo en un formato claro y comprensible.

Requerimientos Funcionales Ingreso de Datos Se permitirá a los usuarios ingresar información del lote, ubicación, datos del propietario, datos del gasista matriculado, características de los artefactos de gas, y cargar imágenes de la planta de arquitectura. Reconocimiento de Colores Las imágenes cargadas serán procesadas para realizar un reconocimiento de colores mediante técnicas de procesamiento de imágenes, identificando y diferenciando los elementos según el color asignado (por ejemplo, cañerías en rojo, ventilaciones en verde). Extracción de Características Se utilizarán algoritmos para extraer patrones y características relevantes de la imagen, agrupando colores similares y convirtiéndolos en datos numéricos. Realización de Perspectiva Isométrica Se generará una perspectiva isométrica de la instalación de gas, detallando longitudes, diámetros, tipo de cañería, ubicación, artefactos, ventilaciones, y otros detalles específicos. Cálculo de Cañerías y Ventilaciones Se calcularán el diámetro y longitud de las cañerías necesarias según el tipo especificado (hierro negro, acero revestido) y se sugerirán las ventilaciones adecuadas conforme a las normas vigentes. Generación de Planos El sistema generará un plano de gas que incluirá: ● Plantas de arquitectura con detalles de artefactos, consumos, diámetros, ubicación del medidor y ventilaciones. ● Perspectiva isométrica de la instalación. ● Cálculos detallados de cañerías y ventilaciones. ● Lista de materiales y artefactos con especificaciones. Creación de Listas de Materiales y Artefactos Se generará una lista de materiales necesaria para la instalación, especificando elementos, medidas, marcas, y matrículas, así como una lista de artefactos con su tipo, ubicación, diámetro de cañería y ventilaciones calculadas.

Visualización y Exportación Los usuarios podrán visualizar el plano generado, descargarlo, y exportar las listas de materiales y artefactos. Verificación y Validación Se verificará que todos los cálculos y diseños cumplen con las normas NAG-200, ISO, y las disposiciones del ENARGAS, alertando al usuario en caso de inconsistencias o incumplimientos normativos. Gestión de Usuarios Se permitirá la creación, edición y eliminación de cuentas de usuario, incluyendo permisos específicos para usuarios y administradores. Además, se llevará un registro de los proyectos realizados por cada usuario, permitiendo su consulta y modificación.

Alcance del Sistema Lo que el sistema hará: Generación de Planos Domiciliarios de Gas para Viviendas Unifamiliares: ● Creará planos de gas en formato PDF, incluyendo plantas de arquitectura, perspectiva isométrica, y detalles de artefactos, cañerías y ventilaciones. ● Realizará cálculos automáticos para determinar los diámetros y longitudes de las cañerías, así como las ventilaciones necesarias, basándose en normas vigentes en Argentina (NAG-200, ISO, ENARGAS). Creación de Listas de Materiales: ● Generará listas detalladas de materiales necesarios para la instalación, especificando elementos, medidas, marcas y matrículas. Gestión de Usuarios: ● Permitirá el registro de usuarios. ● Proporcionará acceso seguro a la plataforma mediante autenticación de usuarios. Lo que el sistema no hará: Diseño Arquitectónico Completo: ● No diseñará la planta arquitectónica desde cero; se basará en imágenes previamente diseñadas por un especialista. ● No contemplará la inclusión de barrales de medidores ni sistemas de doble regulación. Detección de Errores en la Imagen de la Planta: ● No corregirá errores en las imágenes de la planta de arquitectura. La calidad y precisión de los datos procesados dependerán de la calidad de la imagen suministrada.
=======
Documento de Visión “PlaneAr Gas”
Alumnas: Pacheco Melisa, Maia Cornejo.
Cátedra: Ernesto Mayorga, Cristian Pacheco.
Desarrollo de Software
UNPSJB - Puerto Madryn

Introducción
Este documento describe la visión para una aplicación diseñada para ayudar a los
gasistas matriculados a realizar planos de gas en PDF de manera sencilla.
Proporcionando información básica al programa, este diseñará, calculará y
presentará los planos en un formato que respete las normas vigentes, como la
NAG-200, las normas ISO, y las disposiciones establecidas por el ENARGAS (Ente
Nacional Regulador del Gas Argentino).
Problemática
El proceso de realización de planos de gas en Argentina es actualmente complejo y
requiere la intervención de especialistas en dibujo técnico, cálculos de instalaciones,
ventilación y normas vigentes. Este enfoque manual puede dar lugar a errores que
resulten en el rechazo de planos por parte del ente regulador, compras incorrectas
de materiales y demoras en la ejecución de la obra, generando así un impacto
económico negativo tanto para el gasista matriculado como para el propietario de
la obra.
Solución propuesta
Para simplificar este proceso, proponemos la creación de la aplicación “PlaneAr
Gas”, diseñada para ayudar a los gasistas matriculados a generar planos de
instalaciones de gas para viviendas unifamiliares de manera sencilla y cumpliendo
con las normativas vigentes en Argentina. Mediante el uso de esta aplicación, los
usuarios podrán cargar una planta de arquitectura, la cual será reconocida por
colores para producir automáticamente un plano integral listo para presentar al
ente regulador. Este incluirá una visualización detallada de la planta original, una
perspectiva isométrica de la instalación, una lista de materiales y artefactos
necesarios, y una tabla con los cálculos pertinentes, todo en un formato claro y
comprensible.

Requerimientos Funcionales
Ingreso de Datos
Se permitirá a los usuarios ingresar información del lote, ubicación, datos del
propietario, datos del gasista matriculado, características de los artefactos de gas,
y cargar imágenes de la planta de arquitectura.
Reconocimiento de Colores
Las imágenes cargadas serán procesadas para realizar un reconocimiento de
colores mediante técnicas de procesamiento de imágenes, identificando y
diferenciando los elementos según el color asignado (por ejemplo, cañerías en rojo,
ventilaciones en verde).
Extracción de Características
Se utilizarán algoritmos para extraer patrones y características relevantes de la
imagen, agrupando colores similares y convirtiéndolos en datos numéricos.
Realización de Perspectiva Isométrica
Se generará una perspectiva isométrica de la instalación de gas, detallando
longitudes, diámetros, tipo de cañería, ubicación, artefactos, ventilaciones, y otros
detalles específicos.
Cálculo de Cañerías y Ventilaciones
Se calcularán el diámetro y longitud de las cañerías necesarias según el tipo
especificado (hierro negro, acero revestido) y se sugerirán las ventilaciones
adecuadas conforme a las normas vigentes.
Generación de Planos
El sistema generará un plano de gas que incluirá:
● Plantas de arquitectura con detalles de artefactos, consumos, diámetros,
ubicación del medidor y ventilaciones.
● Perspectiva isométrica de la instalación.
● Cálculos detallados de cañerías y ventilaciones.
● Lista de materiales y artefactos con especificaciones.
Creación de Listas de Materiales y Artefactos
Se generará una lista de materiales necesaria para la instalación, especificando
elementos, medidas, marcas, y matrículas, así como una lista de artefactos con su
tipo, ubicación, diámetro de cañería y ventilaciones calculadas.

Visualización y Exportación
Los usuarios podrán visualizar el plano generado, descargarlo, y exportar las listas
de materiales y artefactos.
Verificación y Validación
Se verificará que todos los cálculos y diseños cumplen con las normas NAG-200,
ISO, y las disposiciones del ENARGAS, alertando al usuario en caso de
inconsistencias o incumplimientos normativos.
Gestión de Usuarios
Se permitirá la creación, edición y eliminación de cuentas de usuario, incluyendo
permisos específicos para usuarios y administradores. Además, se llevará un
registro de los proyectos realizados por cada usuario, permitiendo su consulta y
modificación.

Alcance del Sistema
Lo que el sistema hará:
Generación de Planos Domiciliarios de Gas para Viviendas Unifamiliares:
● Creará planos de gas en formato PDF, incluyendo plantas de arquitectura,
perspectiva isométrica, y detalles de artefactos, cañerías y ventilaciones.
● Realizará cálculos automáticos para determinar los diámetros y longitudes
de las cañerías, así como las ventilaciones necesarias, basándose en normas
vigentes en Argentina (NAG-200, ISO, ENARGAS).
Creación de Listas de Materiales:
● Generará listas detalladas de materiales necesarios para la instalación,
especificando elementos, medidas, marcas y matrículas.
Gestión de Usuarios:
● Permitirá el registro de usuarios.
● Proporcionará acceso seguro a la plataforma mediante autenticación de
usuarios.
Lo que el sistema no hará:
Diseño Arquitectónico Completo:
● No diseñará la planta arquitectónica desde cero; se basará en imágenes
previamente diseñadas por un especialista.
● No contemplará la inclusión de barrales de medidores ni sistemas de doble
regulación.
Detección de Errores en la Imagen de la Planta:
● No corregirá errores en las imágenes de la planta de arquitectura. La calidad
y precisión de los datos procesados dependerán de la calidad de la imagen
suministrada.

Posibles Mejoras
Soporte para Normativas Internacionales:
Ampliar el sistema para que soporte normativas internacionales, permitiendo que
los cálculos y validaciones se ajusten a diferentes marcos regulatorios según el país
o región seleccionada por el usuario.
Generación de planos para todo tipo de edificaciones:
Esta mejora incluiría la incorporación de características como barrales de medidores
y sistemas de doble regulación, elementos que actualmente no están contemplados.
De esta manera, se facilitará el diseño y la planificación de instalaciones más
complejas.
Monetización de la aplicación:
En un futuro la aplicación contará con diferentes planes para que el usuario se
suscriba. Estos planes serán mensuales, con una cantidad determinada de planos
por usuario
>>>>>>> meli

Posibles Mejoras Soporte para Normativas Internacionales: Ampliar el sistema para que soporte normativas internacionales, permitiendo que los cálculos y validaciones se ajusten a diferentes marcos regulatorios según el país o región seleccionada por el usuario. Generación de planos para todo tipo de edificaciones: Esta mejora incluiría la incorporación de características como barrales de medidores y sistemas de doble regulación, elementos que actualmente no están contemplados. De esta manera, se facilitará el diseño y la planificación de instalaciones más complejas. Monetización de la aplicación: En un futuro la aplicación contará con diferentes planes para que el usuario se suscriba. Estos planes serán mensuales, con una cantidad determinada de planos por usuario
