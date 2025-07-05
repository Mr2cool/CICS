import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-main-menu',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './main-menu.html',
  styleUrls: ['./main-menu.css']
})
export class MainMenu {
  menuOptions = [
    { label: '1. Customer Inquiry', route: '/customer-inquiry' },
    { label: '2. Account List', route: '/account-list' },
    { label: '3. Logout', route: '/login' }
  ];
}
