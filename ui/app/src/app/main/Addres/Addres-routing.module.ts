import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddresHomeComponent } from './home/Addres-home.component';
import { AddresNewComponent } from './new/Addres-new.component';
import { AddresDetailComponent } from './detail/Addres-detail.component';

const routes: Routes = [
  {path: '', component: AddresHomeComponent},
  { path: 'new', component: AddresNewComponent },
  { path: ':id', component: AddresDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Addres-detail-permissions'
      }
    }
  }
];

export const ADDRES_MODULE_DECLARATIONS = [
    AddresHomeComponent,
    AddresNewComponent,
    AddresDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AddresRoutingModule { }