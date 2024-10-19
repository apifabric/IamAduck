import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'OrderStatu-new',
  templateUrl: './OrderStatu-new.component.html',
  styleUrls: ['./OrderStatu-new.component.scss']
})
export class OrderStatuNewComponent {
  @ViewChild("OrderStatuForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}