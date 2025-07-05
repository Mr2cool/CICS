import { Routes } from '@angular/router';
import { Login } from './login/login';
import { MainMenu } from './main-menu/main-menu';
import { CustomerInquiry } from './customer-inquiry/customer-inquiry';
import { AccountList } from './account-list/account-list';

export const routes: Routes = [
    { path: '', redirectTo: 'login', pathMatch: 'full' },
    { path: 'login', component: Login },
    { path: 'main-menu', component: MainMenu },
    { path: 'customer-inquiry', component: CustomerInquiry },
    { path: 'account-list', component: AccountList }
];
