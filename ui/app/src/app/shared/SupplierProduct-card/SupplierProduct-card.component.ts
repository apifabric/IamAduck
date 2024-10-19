import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './SupplierProduct-card.component.html',
  styleUrls: ['./SupplierProduct-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.SupplierProduct-card]': 'true'
  }
})

export class SupplierProductCardComponent {


}