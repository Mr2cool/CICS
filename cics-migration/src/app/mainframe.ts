import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class Mainframe {

  constructor() { }

  getAccounts() {
    return [
      { accountNumber: '123456789', customerName: 'John Doe', balance: 10000, currency: 'USD' },
      { accountNumber: '987654321', customerName: 'Jane Smith', balance: 25000, currency: 'USD' },
      { accountNumber: '112233445', customerName: 'Peter Jones', balance: 5000, currency: 'EUR' }
    ];
  }
}
