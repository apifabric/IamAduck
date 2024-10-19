import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'ProductPromotion-new',
  templateUrl: './ProductPromotion-new.component.html',
  styleUrls: ['./ProductPromotion-new.component.scss']
})
export class ProductPromotionNewComponent {
  @ViewChild("ProductPromotionForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}