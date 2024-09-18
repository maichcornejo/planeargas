const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const request = require('sync-request');

Given('la persona con {string},{string},{string},{string},{string},{string},{string},{string}', function (nombre, apellido, dni, cuil, sexo, titulo, domicilio, telefono) {
    this.personaData = {
        nombre: nombre,
        apellido: apellido,
        dni: dni,
        cuil: cuil,
        sexo: sexo,
        titulo: titulo,
        domicilio: domicilio,
        telefono: telefono,
      };
});

When('se presiona el botón de guardar', function () {
    try {
        let res = request('POST', 'http://backend:8080/personas', {
            json: this.personaData
        });

        this.response = JSON.parse(res.body,'utf8');
    } catch (error) {
        this.error = error;
    }
});

Then('se espera el siguiente {int} con la {string}', function (status, respuesta) {
    assert(this.response);
    assert.equal(this.response.status, status);
    assert.equal(this.response.message, respuesta);
});
