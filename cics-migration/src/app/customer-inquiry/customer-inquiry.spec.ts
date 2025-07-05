import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustomerInquiry } from './customer-inquiry';

describe('CustomerInquiry', () => {
  let component: CustomerInquiry;
  let fixture: ComponentFixture<CustomerInquiry>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CustomerInquiry]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CustomerInquiry);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
