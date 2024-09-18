import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output, SimpleChanges, input } from '@angular/core';

@Component({
  selector: 'app-pagination',
  standalone: true,
  imports: [CommonModule],
  template: `
  <nav aria-label="Page navigation">
    <ul class="pagination pagination-centered">
      <li class="page-item">
        <a class="page-link" (click)="onPageChange(-2)">&laquo;</a>
      </li>
      <li class="page-item">
        <a class="page-link" (click)="onPageChange(-1)">&lsaquo;</a>
      </li>
      <li *ngFor="let t of pages" [ngClass] ="t === number ? 'active' : ''">
        <a class="page-link" (click)="onPageChange(t + 1)">{{t + 1}}</a>
      </li>
      <li class="page-item">
        <a class="page-link" (click)="onPageChange(-3)">&rsaquo;</a>
      </li>
      <li class="page-item">
        <a class="page-link" (click)="onPageChange(-4)">&raquo;</a>
      </li>
    </ul>
  </nav>
  `,
  styles: ``
})
export class PaginationComponent {
  @Input() totalPages: number =0;
  @Input() last: boolean= false;
  @Input() currentPage: number=1;
  @Input() number : number=1;
  @Output() pageChangeRequested = new EventEmitter<number>();
  pages: number[]=[];

  constructor(){}

  ngOnChanges(changes: SimpleChanges){
    if(changes['totalPages']){
      this.pages = Array.from(Array(this.totalPages).keys())
    }
  }
  
  onPageChange(pageId: number): void {
    let page = pageId;
    if (pageId === -2) {
      page = 1;
      this.last = false;
    } else if (pageId === -1) {
      page = Math.max(1, this.currentPage - 1);
      this.last = false;
    } else if (pageId === -3) {
      page = Math.min(this.currentPage + 1, this.totalPages);
      this.last = page === this.totalPages;
    } else if (pageId === -4) {
      page = this.totalPages;
      this.last = true;
    } else {
      this.last = pageId === this.totalPages;
    }
  
    this.currentPage = page;
    this.pageChangeRequested.emit(page);
  }
}
