import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductPromotionHomeComponent } from './home/ProductPromotion-home.component';
import { ProductPromotionNewComponent } from './new/ProductPromotion-new.component';
import { ProductPromotionDetailComponent } from './detail/ProductPromotion-detail.component';

const routes: Routes = [
  {path: '', component: ProductPromotionHomeComponent},
  { path: 'new', component: ProductPromotionNewComponent },
  { path: ':id', component: ProductPromotionDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ProductPromotion-detail-permissions'
      }
    }
  }
];

export const PRODUCTPROMOTION_MODULE_DECLARATIONS = [
    ProductPromotionHomeComponent,
    ProductPromotionNewComponent,
    ProductPromotionDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductPromotionRoutingModule { }