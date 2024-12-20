from flask import Flask, render_template, request, redirect, url_for
import secrets


def create_app():

    app = Flask(__name__)
    app.secret_key = secrets.token_urlsafe(16)

    from form import csrf, bootstrap
    csrf.init_app(app)
    bootstrap.init_app(app)


    # URL mapping

    ## Register User
    @app.route('/')
    @app.route('/register', methods=['GET', 'POST'])
    def register():

        from form import SignUp
        myForm = SignUp()

        if myForm.validate_on_submit():

            return redirect(url_for('login'))

        return render_template('register.html', form=myForm)
    

    @app.route('/login')
    def login():

        return f"Welcome to Login Page"
    
    return app


app = create_app()

if __name__ == '__main__':
    app.run()