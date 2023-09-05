import { HttpClient } from '@angular/common/http';
import { Component,OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-course-details',
  templateUrl: './course-details.component.html',
  styleUrls: ['./course-details.component.css']
})
export class CourseDetailsComponent implements OnInit {
   courseId:any;
   course:any;
   constructor(private route:ActivatedRoute, private http:HttpClient){}

   ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.courseId = params.get('id');
      console.log("courseIdt",this.courseId)
      // Fetch the course details by courseId and assign it to this.course
      // You can use an HTTP request or any other data source here.
      const apiUrl = `https://eduhub-smd6.onrender.com/course/${this.courseId}`;

      // Make an HTTP GET request to fetch course details
      this.http.get(apiUrl).subscribe(
        (response: any) => {
          this.course = response.course;
          console.log(response)
        },
        (error) => {
          console.error('Error fetching course details:', error);
        }
      );
    });
  }
}
