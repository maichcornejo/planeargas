import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//import { HomeComponent } from './components/home/home.component';  // Importar el componente Home
import { LoteComponent } from './components/lote/lote.component';  // Importar el componente Lote

const routes: Routes = [
 // { path: '', component: HomeComponent },  // Ruta inicial (home)
  { path: 'lote', component: LoteComponent },  // Ruta para la carga de lotes
  { path: '**', redirectTo: '', pathMatch: 'full' }  // Ruta para manejar URLs no válidas
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
