const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const request = require('sync-request');


let parteDiarioResponse;

Given('la existencia de las siguientes licencias', function (dataTable) {
  existingLicencias = dataTable.hashes();
});

Given('que se otorgan las siguientes nuevas licencias', function (dataTable) {
  newLicencias = dataTable.hashes();
});

When('se solicita el parte diario para la fecha {string}', function (fecha) {
  try {
    let res = request('GET', `http://backend:8080/licencias/partesdiarios/${fecha}`);
    parteDiarioResponse = JSON.parse(res.body, 'utf8').data;
  } catch (error) {
    this.error = error;
  }
});

Then('el sistema responde', function (docString) {
  const expectedResponse = JSON.parse(docString);
  assert.deepEqual(parteDiarioResponse, expectedResponse);
});