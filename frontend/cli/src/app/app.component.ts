import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule, NgbModule], 
  styleUrls: ['./app.component.css', './dropdowns.css'],
  templateUrl: 'app.component2.html',
})
export class AppComponent {
  
  
  isDropdownOpen= false;
  
  constructor(private router: Router) { }

  toggleDropdown() {
    this.isDropdownOpen = !this.isDropdownOpen;
  }
}