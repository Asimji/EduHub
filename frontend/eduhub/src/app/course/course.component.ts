import { Component,OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http'

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})
export class CourseComponent {
  
 user:any[]=[]
constructor(private http:HttpClient){}

ngOnInit(){
  this.http.get<any>(`http://localhost:8080/course`).subscribe((response)=>{this.user=response.course},(error)=>{console.log(error)})
}

}
