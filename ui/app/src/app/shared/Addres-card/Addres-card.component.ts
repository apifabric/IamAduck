import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Addres-card.component.html',
  styleUrls: ['./Addres-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Addres-card]': 'true'
  }
})

export class AddresCardComponent {


}