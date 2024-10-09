import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';  // Importa FormsModule para el manejo de formularios
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';  // Importa HttpClientModule para las peticiones HTTP

import { AppComponent } from './app.component';
import { LoteComponent } from './components/lote/lote.component';
import { HomeComponent } from './components/home/home.component';
import { NuevoPlanoComponent } from './components/plano/nuevo-plano.component';  // Importa el nuevo componente de planos

const routes: Routes = [
  { path: '', component: HomeComponent },  // Ruta principal (Home)
  { path: 'lote', component: LoteComponent },  // Ruta para la carga de lotes
  { path: 'nuevo-plano', component: NuevoPlanoComponent }  // Ruta para la carga de nuevo plano
];

@NgModule({
  declarations: [
    AppComponent,
    LoteComponent,
    //HomeComponent,
    NuevoPlanoComponent  // Asegúrate de declarar el componente nuevo aquí
  ],
  imports: [
    BrowserModule,
    FormsModule,  // Para el manejo de formularios en Angular
    HttpClientModule,  // Para las peticiones HTTP a tu backend
    RouterModule.forRoot(routes)  // Configuración de rutas
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
