import { Component } from '@angular/core';
import { Router } from '@angular/router';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  constructor(private router: Router) { }
      user={email:"",password:""}

      handleSubmit(){
        console.log(this.user);
        fetch(`http://localhost:8080/user/login`,{
          method:"POST",
          headers:{
            "Content-Type":"application/json"
          },
          body:JSON.stringify(this.user)
        }).then(res=>res.json()).then((res)=>{res.token ? localStorage.setItem('loginToken',JSON.stringify(res.token)) : localStorage.setItem('loginToken',JSON.stringify(""));alert("Login Successfull");this.router.navigate(['']);
      }).catch(e=>console.log(e))
      }

     
}
