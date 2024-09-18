const { Given, When, Then } = require('cucumber');
const assert = require('assert');
const request = require('sync-request');

Given('la persona con {string} {string} y {string}', function (dni,nombre,apellido) {
    let req = request('GET',encodeURI(`http://backend:8080/personas/${dni}/${nombre}/${apellido}`));
    
    const personaT = JSON.parse(req.body, 'utf8').data;
    this.nuevaDesignacion = {
        persona: personaT
    };
});

Given('que se asigna al cargo con tipo de designación {string} y {string}', function (tipoDesignacion, nombreDesignacion) {
    
    let req = request('GET', encodeURI(`http://backend:8080/cargos/${tipoDesignacion}/${nombreDesignacion}`));
    const cargo = JSON.parse(req.body, 'utf8').data;

    this.nuevaDesignacion.cargo = cargo;
        
});
Given('si es espacio curricular asignada a la división {int} {int} {string}', function (anio, numero, turno) {

});

Given('se designa por el período {string} {string}', function (fechaDesde, fechaHasta) {
    this.nuevaDesignacion.fechaDesde = new Date(fechaDesde);
    this.nuevaDesignacion.fechaHasta = new Date(fechaHasta);
});

When('se presiona el botón guardar en designaciones', function () {
    let res = request('POST', 'http://backend:8080/designaciones', { json: this.nuevaDesignacion });
    this.response = JSON.parse(res.body, 'utf8');
});

Then('se espera el siguiente {int} y {string}', function (status, respuesta) {
    assert(this.response);
    assert.equal(this.response.message, respuesta);
    assert.equal(this.response.status, status);
});