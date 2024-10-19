import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrderStatuHomeComponent } from './home/OrderStatu-home.component';
import { OrderStatuNewComponent } from './new/OrderStatu-new.component';
import { OrderStatuDetailComponent } from './detail/OrderStatu-detail.component';

const routes: Routes = [
  {path: '', component: OrderStatuHomeComponent},
  { path: 'new', component: OrderStatuNewComponent },
  { path: ':id', component: OrderStatuDetailComponent,
    data: {
      oPermission: {
        permissionId: 'OrderStatu-detail-permissions'
      }
    }
  }
];

export const ORDERSTATU_MODULE_DECLARATIONS = [
    OrderStatuHomeComponent,
    OrderStatuNewComponent,
    OrderStatuDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class OrderStatuRoutingModule { }