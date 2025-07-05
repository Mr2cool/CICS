import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-customer-inquiry',
  templateUrl: './customer-inquiry.html',
  styleUrls: ['./customer-inquiry.css']
})
export class CustomerInquiry {
  inquiryForm: FormGroup;
  customerData: { name: string, email: string, status: string } | null = null;

  constructor(private fb: FormBuilder) {
    this.inquiryForm = this.fb.group({
      customerId: ['']
    });
  }

  onSearch() {
    // Mock data, replace with actual API call
    this.customerData = {
      name: 'Jane Doe',
      email: 'jane.doe@example.com',
      status: 'Active'
    };
  }
}
