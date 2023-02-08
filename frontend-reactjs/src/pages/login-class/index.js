import React from 'react';
import axios from 'axios';
import Constantes from '../../common/constantes';


class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        };

        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
        // load default data
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({ [name]: value });
    }

    handleSubmit(event) {
        event.preventDefault();

        const url = Constantes.ApiURL + "/seguridad/login";
        const json = { username: this.state.username, password: this.state.password };

        axios({
            method: "post",
            url: url,
            data: json,
            //responseType: 'application/json'
        })
            .then(function(response) {
                const data = response.data;
                if (data && data.ok == true && data.token != "") {
                    alert("Bienvenido");
                } else {
                    alert("Usuario o password errados");
                }
            })
            .catch(function(response) {
                alert("Error al consultar los datos");
            });
    }

    render() {
        return (
            <main className="form-signin w-100 m-auto">
                <form onSubmit={this.handleSubmit}>
                    <img className="mb-4" src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57" />
                    <h1 className="h3 mb-3 fw-normal">Please sign-in</h1>

                    <div className="form-floating">
                        <input type="text" className="form-control" id="floatingInput" placeholder="username" name="username" value={this.state.username} onChange={this.handleInputChange} />
                        <label htmlFor="floatingInput">Username</label>
                    </div>
                    <div className="form-floating">
                        <input type="password" className="form-control" id="floatingPassword" placeholder="Password" name="password" value={this.state.password} onChange={this.handleInputChange} />
                        <label htmlFor="floatingPassword">Password</label>
                    </div>

                    <div className="checkbox mb-3">
                        <label>
                            <input type="checkbox" value="remember-me" /> Remember me
                        </label>
                    </div>

                    <button className="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
                    <p className="mt-5 mb-3 text-muted">&copy; 2023 - class component</p>
                </form>
            </main>
        );
    }

}

export default LoginPage;