import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';  // Importa FormsModule
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';  // Para las peticiones HTTP

import { AppComponent } from './app.component';
import { LoteComponent } from './components/lote/lote.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'lote', component: LoteComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    LoteComponent,
   // HomeComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,  // Asegúrate de agregar FormsModule aquí
    HttpClientModule,  // Para las peticiones HTTP
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
