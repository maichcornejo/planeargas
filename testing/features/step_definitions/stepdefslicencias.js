const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const request = require('sync-request');



Given('el docente con DNI {string}, nombre {string} y apellido {string}', function (dni, nombre, apellido) {

    let req = request('GET', encodeURI(`http://backend:8080/personas/${dni}/${nombre}/${apellido}`));

    const personaT = JSON.parse(req.body, 'utf8').data;
    this.nuevaLicencia = {
        persona: personaT
    };
});

When('solicita una licencia artículo {string} con descripción {string} para el período {string} {string}', function (articulo, descripción, pedidoDesde, pedidoHasta) {

    let req1 = request('GET', `http://backend:8080/articulos/articulo/${articulo}`);
    const articuloLicenciaSolicitado = JSON.parse(req1.body, 'utf8').data;
    this.nuevaLicencia.articuloLicencia = articuloLicenciaSolicitado;
    this.nuevaLicencia.pedidoDesde = new Date(pedidoDesde);
    this.nuevaLicencia.pedidoHasta = new Date(pedidoHasta);
    let req = request('POST', 'http://backend:8080/licencias', {
        json: this.nuevaLicencia
    });
    this.actualAnswer = JSON.parse(req.body, 'utf8');
   
});

Then('debería obtener el siguiente resultado de {int} y {string}', function (status, mensajeEsperado) {
    assert(this.actualAnswer);
    assert.equal(this.actualAnswer.message, mensajeEsperado);
    assert.equal(this.actualAnswer.status, status);
});


Given('que existe la persona', function (dataTable) {
    const personaData = dataTable.hashes()[0];
    this.persona = {
        dni: personaData.DNI,
        nombre: personaData.Nombre,
        apellido: personaData.Apellido
    };
    let req = request('GET', encodeURI(`http://backend:8080/personas/${this.persona.dni}/${this.persona.nombre}/${this.persona.apellido}`));
    const personaT = JSON.parse(req.body, 'utf8').data;
    this.nuevaDesignacion = {
        persona: personaT
    };

});

Given('que existen las siguientes instancias de designación asignada', function (dataTable) {
    const cargoData = dataTable.hashes()[0];
    this.cargoData = {
        tipoDesignacion: cargoData.TipoDesignacion,
        nombreDesignacion: cargoData.NombreTipoDesignacion
    };
    let req = request('GET', encodeURI(`http://backend:8080/cargos/${this.cargoData.tipoDesignacion}/${this.cargoData.nombreDesignacion}`));
    const cargo = JSON.parse(req.body, 'utf8').data;

    this.nuevaDesignacion.cargo = cargo;
});

Given('que la instancia de designación está asignada a la persona', function (dataTable) {
    const designacionData = dataTable.hashes()[0];
    this.designacionExistente = {
        dni: designacionData.DNI,
        nombre: designacionData.Nombre,
        apellido: designacionData.Apellido,
        desde: new Date(designacionData.Desde),
        hasta: new Date(designacionData.Hasta)
    };
});

Given('que la instancia de designación está asignada a la persona con licencia {string} comprendida en el período desde {string} hasta {string}', function (articulo, pedidoDesde, pedidoHasta) {
    let reqPersona = request('GET', encodeURI(`http://backend:8080/personas/${this.designacionExistente.dni}/${this.designacionExistente.nombre}/${this.designacionExistente.apellido}`));
    const respuestaPersona = JSON.parse(reqPersona.body, 'utf8').data;
    const personaId = respuestaPersona.id;
    let reqA = request('GET', encodeURI(`http://backend:8080/articulos/articulo/${articulo}`));

    const art = JSON.parse(reqA.body, 'utf8').data;
    const articuloId = art.id;

    const fechaInicio = new Date(pedidoDesde);
    const fechaFin = new Date(pedidoHasta);

    let resL = request('GET', encodeURI(`http://backend:8080/licencias/${personaId}/${articuloId}/${fechaInicio}/${fechaFin}`));
    const respuesta = JSON.parse(resL.body, 'utf8').data;

    return assert.equal(resL.statusCode, 200);
});

When('se solicita el servicio de designación de la persona al cargo en el período comprendido desde {string} hasta {string}', function (fechaDesde, fechaHasta) {
    this.nuevaDesignacion.fechaDesde = new Date(fechaDesde);
    this.nuevaDesignacion.fechaHasta = new Date(fechaHasta);


    let req = request('POST', 'http://backend:8080/designaciones', {
        json: this.nuevaDesignacion
    });
    this.actualAnswer = JSON.parse(req.body, 'utf8');
});

Then('se recupera el mensaje', function (docString) {
    const expectedAnswer = JSON.parse(docString);
    assert.equal(this.actualAnswer.message, expectedAnswer.StatusText);
    assert.equal(this.actualAnswer.status, expectedAnswer.StatusCode);
});