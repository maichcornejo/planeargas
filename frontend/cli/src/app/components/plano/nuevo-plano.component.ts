import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-nuevo-plano',
  templateUrl: './nuevo-plano.component.html'
})
export class NuevoPlanoComponent {
  plano = {
    artefactos: 0,
    material: '',
    nombre: '',
    apellido: '',
    matricula: '',
    categoria: '',
    credencial: null,
    planta: null
  };

  constructor(private http: HttpClient) {}

  onFileSelect(event: any, fileType: string) {
    const file = event.target.files[0];
    if (fileType === 'credencial') {
      this.plano.credencial = file;
    } else if (fileType === 'planta') {
      this.plano.planta = file;
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('artefactos', this.plano.artefactos.toString());
    formData.append('material', this.plano.material);
    formData.append('nombre', this.plano.nombre);
    formData.append('apellido', this.plano.apellido);
    formData.append('matricula', this.plano.matricula);
    formData.append('categoria', this.plano.categoria);
    if (this.plano.credencial) {
      formData.append('credencial', this.plano.credencial);
    }
    if (this.plano.planta) {
      formData.append('planta', this.plano.planta);
    }

    this.http.post('http://localhost:28002/nuevo-plano', formData).subscribe(response => {
      console.log('Plano cargado con éxito', response);
    }, error => {
      console.error('Error al cargar el plano', error);
    });
  }
}
