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
  this.http.get<any>(`https://eduhub-smd6.onrender.com/course`).subscribe((response)=>{this.user=response.course},(error)=>{console.log(error)})
}

}
