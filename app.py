from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'The Flask App ECS is a simple web app built using the Flask framework, containerized with Docker, and deployed on Amazon ECS (Elastic Container Service). It is designed to be scalable and easy to manage in the cloud environment. The app runs on port 80 and uses ECS for container orchestration, making it suitable for cloud-based applications that need to be scaled efficiently.'

@app.route('/health')
def health():
    return 'Server is up and running'
