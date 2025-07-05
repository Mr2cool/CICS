import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { MainMenuComponent } from './main-menu/main-menu.component';
import { CustomerInquiryComponent } from './customer-inquiry/customer-inquiry.component';
import { AccountListComponent } from './account-list/account-list.component';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'menu', component: MainMenuComponent },
  { path: 'customer', component: CustomerInquiryComponent },
  { path: 'account', component: AccountListComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}# Sample Angular Screens for Migrating CICS 3270 "Green Screen" Applications

Migrating legacy CICS 3270 "green screen" applications to Angular web interfaces involves modernizing the UI while maintaining the core business logic and workflows. Below are sample Angular screen designs that can serve as a starting point for your migration.

---

## 1. **Login Screen**

**Purpose:** Simulates mainframe login with improved UX.

```typescript name=login.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  loginForm: FormGroup;
  constructor(private fb: FormBuilder) {
    this.loginForm = this.fb.group({
      userId: ['', Validators.required],
      password: ['', Validators.required]
    });
  }
  onSubmit() {
    // Call API to authenticate with CICS backend
  }
}
```

```html name=login.component.html
<div class="login-container">
  <h2>CICS Application Login</h2>
  <form [formGroup]="loginForm" (ngSubmit)="onSubmit()">
    <label>User ID:</label>
    <input formControlName="userId" type="text" />
    <label>Password:</label>
    <input formControlName="password" type="password" />
    <button type="submit" [disabled]="!loginForm.valid">Login</button>
  </form>
</div>
```

---

## 2. **Main Menu Screen**

**Purpose:** Replicates the main menu of a CICS green screen app.

```typescript name=main-menu.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-main-menu',
  templateUrl: './main-menu.component.html',
  styleUrls: ['./main-menu.component.css']
})
export class MainMenuComponent {
  menuOptions = [
    { label: '1. Customer Inquiry', route: '/customer' },
    { label: '2. Account Management', route: '/account' },
    { label: '3. Reports', route: '/reports' },
    { label: '4. Logout', route: '/logout' }
  ];
}
```

```html name=main-menu.component.html
<div class="main-menu">
  <h2>Main Menu</h2>
  <ul>
    <li *ngFor="let option of menuOptions">
      <a [routerLink]="option.route">{{ option.label }}</a>
    </li>
  </ul>
</div>
```

---

## 3. **Customer Inquiry Screen**

**Purpose:** Modernizes a typical CICS inquiry screen.

```typescript name=customer-inquiry.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-customer-inquiry',
  templateUrl: './customer-inquiry.component.html',
  styleUrls: ['./customer-inquiry.component.css']
})
export class CustomerInquiryComponent {
  inquiryForm: FormGroup;
  customerData: any = null;
  constructor(private fb: FormBuilder) {
    this.inquiryForm = this.fb.group({
      customerId: ['']
    });
  }
  onSearch() {
    // Call API to mainframe for customer data
    // this.customerData = response;
  }
}
```

```html name=customer-inquiry.component.html
<div class="inquiry-container">
  <h3>Customer Inquiry</h3>
  <form [formGroup]="inquiryForm" (ngSubmit)="onSearch()">
    <label>Customer ID:</label>
    <input formControlName="customerId" type="text" />
    <button type="submit">Search</button>
  </form>
  <div *ngIf="customerData">
    <h4>Customer Details</h4>
    <p>Name: {{ customerData.name }}</p>
    <p>Email: {{ customerData.email }}</p>
    <p>Status: {{ customerData.status }}</p>
  </div>
</div>
```

### Practical Example

#### 1. Mainframe (CICS 3270) “Green Screen” Example

```
-------------------------------
| CUSTOMER INQUIRY            |
|                             |
| Customer ID:  [__________]  |
|                             |
| Name:         [__________]  |
| Email:        [__________]  |
| Status:       [__________]  |
|                             |
| PF3=Exit  PF5=Submit        |
-------------------------------
```

---

#### 2. Modern Angular Screen Equivalent

```typescript name=customer-inquiry.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-customer-inquiry',
  templateUrl: './customer-inquiry.component.html',
  styleUrls: ['./customer-inquiry.component.css']
})
export class CustomerInquiryComponent {
  inquiryForm: FormGroup;
  customerData: any = null;

  constructor(private fb: FormBuilder) {
    this.inquiryForm = this.fb.group({
      customerId: ['']
    });
  }

  onSearch() {
    // Replace this with your API call
    this.customerData = {
      name: 'Jane Doe',
      email: 'jane.doe@example.com',
      status: 'Active'
    };
  }
}
```

```html name=customer-inquiry.component.html
<div class="customer-inquiry-container">
  <h2>Customer Inquiry</h2>
  <form [formGroup]="inquiryForm" (ngSubmit)="onSearch()">
    <label for="customerId">Customer ID:</label>
    <input id="customerId" formControlName="customerId" type="text" />
    <button type="submit">Search</button>
  </form>

  <div *ngIf="customerData" class="result">
    <h3>Customer Details</h3>
    <p><strong>Name:</strong> {{ customerData.name }}</p>
    <p><strong>Email:</strong> {{ customerData.email }}</p>
    <p><strong>Status:</strong> {{ customerData.status }}</p>
  </div>
</div>
```

```css name=customer-inquiry.component.css
.customer-inquiry-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  background: #f4f8fb;
  border-radius: 8px;
  box-shadow: 0 2px 8px #e0e0e0;
}
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.result {
  margin-top: 2rem;
  background: #fff;
  padding: 1rem;
  border-radius: 6px;
  box-shadow: 0 1px 4px #e0e0e0;
}
```

---

## 4. **Responsive Table Screen (e.g., Account Listing)**

**Purpose:** Presents tabular data in a modern style.

```typescript name=account-list.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-account-list',
  templateUrl: './account-list.component.html',
  styleUrls: ['./account-list.component.css']
})
export class AccountListComponent {
  accounts = [
    { id: 'A123', type: 'Checking', balance: 1500.00 },
    { id: 'B456', type: 'Savings', balance: 5000.00 }
  ];
}
```

```html name=account-list.component.html
<div class="account-list">
  <h3>Accounts</h3>
  <table>
    <thead>
      <tr>
        <th>Account ID</th>
        <th>Type</th>
        <th>Balance</th>
      </tr>
    </thead>
    <tbody>
      <tr *ngFor="let acc of accounts">
        <td>{{ acc.id }}</td>
        <td>{{ acc.type }}</td>
        <td>{{ acc.balance | currency }}</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 5. **Error/Message Dialog**

**Purpose:** Modern alternative for CICS message line.

```typescript name=message-dialog.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-message-dialog',
  template: `<div class="message" *ngIf="message">{{message}}</div>`,
  styleUrls: ['./message-dialog.component.css']
})
export class MessageDialogComponent {
  @Input() message: string = '';
}
```

---

## 6. **Angular Service Example (API Communication)**

```typescript name=mainframe.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class MainframeService {
  constructor(private http: HttpClient) {}

  getCustomer(customerId: string): Observable<any> {
    return this.http.get(`/api/customer/${customerId}`);
    // This endpoint should route through your middleware/API Gateway to the mainframe
  }
}
```

---

## 7. **Sample Styling (SCSS/CSS)**

```css name=main-menu.component.css
.main-menu {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px #ddd;
}
.main-menu h2 { margin-bottom: 1rem; }
.main-menu ul { list-style: none; padding: 0; }
.main-menu li { margin: 0.5rem 0; }
.main-menu a { text-decoration: none; color: #007bff; }
.main-menu a:hover { text-decoration: underline; }
```

---

## **Notes and Best Practices**

- **API Gateway**: All API calls from the Angular app should go through a secure middleware layer that handles translation and authentication for mainframe calls.
- **State Management**: Use NgRx or similar for complex workflows.
- **Accessibility**: Ensure WCAG compliance for all screens.
- **Testing**: Implement unit and integration tests for all components and services.
- **Error Handling**: Provide clear feedback to users for all error scenarios.

---

### **References**

- [Enabling CICS web support for CICS as an HTTP server - IBM][1]
- [Web services samples - IBM][2]
- [Mainframe Tutorials - Micro Focus][3]
- [CICS Screen Tutorial - Micro Focus][4]

[1]: https://www.ibm.com/docs/en/cics-ts/5.5.0?topic=ccwsc-enabling-cics-web-support-cics-as-http-server&utm_source=chatgpt.com
[2]: https://www.ibm.com/docs/en/cics-ts/5.6.0?topic=samples-web-services&utm_source=chatgpt.com
[3]: https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-VS2019/GUID-86C8565D-A393-4B8B-9A8D-7CF37E676D6E.html?utm_source=chatgpt.com
[4]: https://www.microfocus.com/documentation/studio-enterprise-edition/studioee60sp2ws2/Studio%20EE%2060%20SP2%20WS2%20Windows%3D2%3DWeb%20Help%202016%20%28MF%29%3Den/GUID-840E728D-164D-4251-BC85-1A08FF5634CD.html?utm_source=chatgpt.com
