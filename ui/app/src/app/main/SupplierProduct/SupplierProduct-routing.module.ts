import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplierProductHomeComponent } from './home/SupplierProduct-home.component';
import { SupplierProductNewComponent } from './new/SupplierProduct-new.component';
import { SupplierProductDetailComponent } from './detail/SupplierProduct-detail.component';

const routes: Routes = [
  {path: '', component: SupplierProductHomeComponent},
  { path: 'new', component: SupplierProductNewComponent },
  { path: ':id', component: SupplierProductDetailComponent,
    data: {
      oPermission: {
        permissionId: 'SupplierProduct-detail-permissions'
      }
    }
  }
];

export const SUPPLIERPRODUCT_MODULE_DECLARATIONS = [
    SupplierProductHomeComponent,
    SupplierProductNewComponent,
    SupplierProductDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplierProductRoutingModule { }