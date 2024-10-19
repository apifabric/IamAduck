import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PRODUCTPROMOTION_MODULE_DECLARATIONS, ProductPromotionRoutingModule} from  './ProductPromotion-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ProductPromotionRoutingModule
  ],
  declarations: PRODUCTPROMOTION_MODULE_DECLARATIONS,
  exports: PRODUCTPROMOTION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ProductPromotionModule { }