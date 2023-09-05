import { Component } from '@angular/core';
import { Router} from '@angular/router';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent  {

  constructor(private router: Router){}
   
   user={name:"",role:"",email:"",password:""}

   handleSubmit(){
    console.log(this.user)
    fetch(`https://eduhub-smd6.onrender.com/user/register`,{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify(this.user)
    }).then(res=>res.json()).then((res)=>{alert(res.msg);this.router.navigate(['/login']);
  }).catch(e=>console.log(e))
   }

}
