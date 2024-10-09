import { Component } from '@angular/core';

@Component({
  selector: 'app-root',  // El selector para insertar este componente en HTML
  templateUrl: './app.component.html',  // El archivo HTML asociado
  styleUrls: ['./app.component.css']  // Los estilos CSS asociados
})
export class AppComponent {
  title = 'Mi Aplicación de Carga de Lotes';
}
