import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//import { HomeComponent } from './components/home/home.component';  // Importar el componente Home
import { LoteComponent } from './components/lote/lote.component';  // Importar el componente Lote
import { NuevoPlanoComponent } from './components/plano/nuevo-plano.component';  // Importa el nuevo componente de planos

const routes: Routes = [
  { path: 'lote', component: LoteComponent },  // Ruta para la carga de lotes
  { path: 'nuevo-plano', component: NuevoPlanoComponent },  // Nueva ruta para la carga de planos
  { path: '', redirectTo: '/lote', pathMatch: 'full' },  // Ruta predeterminada (puede ser 'lote' u otro)
  { path: '**', redirectTo: '', pathMatch: 'full' }  // Ruta para manejar URLs no válidas
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
