import { TestBed } from '@angular/core/testing';

import { Mainframe } from './mainframe';

describe('Mainframe', () => {
  let service: Mainframe;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Mainframe);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
