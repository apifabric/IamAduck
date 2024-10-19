import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './OrderStatu-card.component.html',
  styleUrls: ['./OrderStatu-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.OrderStatu-card]': 'true'
  }
})

export class OrderStatuCardComponent {


}