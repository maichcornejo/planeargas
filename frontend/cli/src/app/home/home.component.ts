import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  template: `
    <div class="welcome-message">
      Bienvenidos al frontend de planear gas
    </div>
  `,
  styles: `
    .welcome-message {
      padding: 20px;
      text-align: center;
      font-size: 24px;
    }
  `
})
export class HomeComponent { }
