import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Addres-new',
  templateUrl: './Addres-new.component.html',
  styleUrls: ['./Addres-new.component.scss']
})
export class AddresNewComponent {
  @ViewChild("AddresForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}