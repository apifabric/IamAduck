import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ORDERSTATU_MODULE_DECLARATIONS, OrderStatuRoutingModule} from  './OrderStatu-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    OrderStatuRoutingModule
  ],
  declarations: ORDERSTATU_MODULE_DECLARATIONS,
  exports: ORDERSTATU_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class OrderStatuModule { }