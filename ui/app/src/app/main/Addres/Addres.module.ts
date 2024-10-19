import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ADDRES_MODULE_DECLARATIONS, AddresRoutingModule} from  './Addres-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AddresRoutingModule
  ],
  declarations: ADDRES_MODULE_DECLARATIONS,
  exports: ADDRES_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AddresModule { }