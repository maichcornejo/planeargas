const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const request = require('sync-request');

let reporteResponse;
let errorMessage;
let anio;

Given('los reportes de concepto del {int}', function (anio) {
 anio=anio;
});

When('se solicita el Reporte de Concepto para el {int}', function (anio) {
  try {
    const res = request('GET', `http://backend:8080/estadisticasPersona/${anio}`);
    const responseBody = JSON.parse(res.getBody('utf8'));
    if (responseBody.error) {
      errorMessage = responseBody.message;
    } else {
      reporteResponse = responseBody;
    }
  } catch (error) {
    this.error = error;
  }
});

Then('el sistema responde con un reporte', function (docString) {
  const expectedResponse = JSON.parse(docString);
  assert.deepStrictEqual(reporteResponse, expectedResponse);
});

Then('el sistema responde con un mensaje de error {string}', function (expectedMessage) {
  assert.strictEqual(errorMessage, expectedMessage);
});
