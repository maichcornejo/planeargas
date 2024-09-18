const { Given, When, Then } = require('cucumber');
const assert = require('assert');
const request = require('sync-request');


Given(
    "el cargo institucional cuyo {string} que da título al mismo",
    function (nombre) {
        this.cargo = {
            nombre: nombre
        };
    }
);

Given("que es del {string}", function (tipoDesignacion) {
    this.cargo.tipoDesignacion = tipoDesignacion;
});

Given(
    "que tiene una {int} con la vigencia {string},{string}",
    function (cargaHoraria, fechaDesde, fechaHasta) {
        this.cargo.cargaHoraria = cargaHoraria;
        this.cargo.fechaDesde = new Date(fechaDesde);
        this.cargo.fechaHasta = fechaHasta ? new Date(fechaHasta) : null;
        this.cargo.horarios = [];
    }
);

Given(
    "que si el tipo es espacio curricular, opcionalmente se asigna a la división {int},{int},{string}",
    function (anio, numDivision, turno) {
        let res = request(
            'GET',
            `http://backend:8080/divisiones/${anio}/${numDivision}/${turno}`,
        );
        this.cargo.division = JSON.parse(res.body, 'utf8').data;
    }
);

When("se presiona el botón de guardar en cargos", function () {
        let res = request('POST', 'http://backend:8080/cargos', { json: this.cargo });
        this.response = JSON.parse(res.body, 'utf8');
    });

Then('se espera el siguiente {int} con la {string} en cargos', function (status, respuesta) {
    assert(this.response);
    assert.equal(this.response.message, respuesta);
    assert.equal(this.response.status, status);
});