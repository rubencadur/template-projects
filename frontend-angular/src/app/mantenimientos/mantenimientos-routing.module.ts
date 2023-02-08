import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [

  // {
  //   path: 'mantenimientos',
  //   component: MenuPrincipal,
  //   children: [
  //     {
  //       path: 'empleados',
  //       component: ListadoEmpleadosPage
  //     },
  //     {
  //       path: 'productos',
  //       component: ListadoProductosPage
  //     }
  //   ]

  // }

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MantenimientosRoutingModule { }
