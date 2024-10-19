import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './ProductPromotion-card.component.html',
  styleUrls: ['./ProductPromotion-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.ProductPromotion-card]': 'true'
  }
})

export class ProductPromotionCardComponent {


}