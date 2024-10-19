import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SUPPLIERPRODUCT_MODULE_DECLARATIONS, SupplierProductRoutingModule} from  './SupplierProduct-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SupplierProductRoutingModule
  ],
  declarations: SUPPLIERPRODUCT_MODULE_DECLARATIONS,
  exports: SUPPLIERPRODUCT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SupplierProductModule { }