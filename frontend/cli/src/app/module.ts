import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';  // Importar HttpClientModule

import { AppComponent } from './app.component';
import { LoteComponent } from './components/lote/lote.component';
import { LoteService } from './service/lote.service';  // Importar el servicio

@NgModule({
  declarations: [
    AppComponent,
    LoteComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule  // Agregar HttpClientModule aquí
  ],
  providers: [LoteService],
  bootstrap: [AppComponent]
})
export class AppModule { }
