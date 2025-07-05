import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Mainframe } from '../mainframe';

@Component({
  selector: 'app-account-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './account-list.html',
  styleUrls: ['./account-list.css']
})
export class AccountList implements OnInit {
  accounts: any[] = [];

  constructor(private mainframe: Mainframe) {}

  ngOnInit() {
    this.accounts = this.mainframe.getAccounts();
  }
}
