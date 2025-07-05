import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule } from '@angular/forms';
import { Login } from './login';

describe('Login', () => {
  let component: Login;
  let fixture: ComponentFixture<Login>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Login, ReactiveFormsModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Login);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have an invalid form when empty', () => {
    expect(component.loginForm.valid).toBeFalsy();
  });

  it('should have a valid form when filled', () => {
    component.loginForm.controls['userId'].setValue('testuser');
    component.loginForm.controls['password'].setValue('password');
    expect(component.loginForm.valid).toBeTruthy();
  });

  it('should have an invalid form when only userId is provided', () => {
    component.loginForm.controls['userId'].setValue('testuser');
    expect(component.loginForm.valid).toBeFalsy();
  });

  it('should have an invalid form when only password is provided', () => {
    component.loginForm.controls['password'].setValue('password');
    expect(component.loginForm.valid).toBeFalsy();
  });
});
