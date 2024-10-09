import { Component } from '@angular/core';
import { LoteService } from '../../service/lote.service';

@Component({
  selector: 'app-lote',
  templateUrl: './lote.component.html',
  styleUrls: ['./lote.component.css']
})
export class LoteComponent {
  loteData = {
    tipo_calle: '',
    nombre_calle: '',
    altura: '',
    manzana: '',
    lote: '',
    piso: '',
    departamento: '',
    entre_calles_1: '',
    entre_calles_2: '',
    distancia_esquinas: ''
  };

  constructor(private loteService: LoteService) { }

  submitLote() {
    this.loteService.saveLote(this.loteData).subscribe(response => {
      console.log('Lote guardado:', response);
    }, error => {
      console.error('Error guardando el lote:', error);
    });
  }
}
