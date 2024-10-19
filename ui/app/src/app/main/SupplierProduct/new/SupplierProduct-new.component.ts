import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'SupplierProduct-new',
  templateUrl: './SupplierProduct-new.component.html',
  styleUrls: ['./SupplierProduct-new.component.scss']
})
export class SupplierProductNewComponent {
  @ViewChild("SupplierProductForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}