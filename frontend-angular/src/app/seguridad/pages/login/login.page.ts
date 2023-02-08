import { Component, OnInit } from "@angular/core";
import { LoginModel } from "../../models/login.model";

@Component({
    selector: 'app-login',
    templateUrl: './login.page.html',
    styleUrls: ['./login.page.scss']
})
export class LoginPage implements OnInit {

    data: LoginModel;
    

    constructor() {
        this.data = { username: "", password: "" };
    }

    ngOnInit(): void {
		//this.data.username = "ad";
        //this.data.password = "q1";
	}

    login(e:any): void {
        e.preventDefault();

        
    }
}