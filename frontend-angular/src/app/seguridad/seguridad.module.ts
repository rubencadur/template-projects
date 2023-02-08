import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { SeguridadRoutingModule, SEGURIDAD_COMPONENTS } from './seguridad-routing.module';


@NgModule({
  declarations: [
    SEGURIDAD_COMPONENTS
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    SeguridadRoutingModule
  ]
})
export class SeguridadModule { }
