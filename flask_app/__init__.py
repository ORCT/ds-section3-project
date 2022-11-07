from flask import Flask, Blueprint, render_template

def create_app():
    app = Flask(__name__)
    
    from routes.root_route import root_bp
    from routes.result_route import result_bp
    
    app.register_blueprint(root_bp)
    app.register_blueprint(result_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)