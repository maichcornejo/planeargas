const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const request = require('sync-request');


Given('la el espacio físico división con {int},{int},{string},{string}', function(anio, numDivision, orientacion, turno) {
    this.divisionData = {
        anio: anio,
        numDivision: numDivision,
        orientacion: orientacion,
        turno: turno
    };
});

When('se presiona el botón de guardar en divisiones', function () {
    try {
        let res = request('POST', encodeURI('http://backend:8080/divisiones'), {
            json: this.divisionData
        });

        response = JSON.parse(res.body, 'utf8');
    } catch (error) {
        throw new Error('Error al enviar la solicitud: ' + error);
    }
});

Then('se espera el siguiente {int} con la {string} en divisiones', function (status, respuesta) {
    assert(response);
    assert.equal(response.status, status);
    assert.equal(response.message, respuesta);
});