import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoteService {
  private apiUrl = 'http://localhost:28002';  // Asegúrate de usar la URL correcta

  constructor(private http: HttpClient) { }

  saveLote(loteData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/lote`, loteData);
  }
}
