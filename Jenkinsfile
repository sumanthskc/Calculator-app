pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sumanthskc/Calculator-app.git'

            }
        }

        stage('Run Tests in Docker') {
            steps {
                bat 'docker pull python:3.11-slim'
                bat '''
                docker run --rm -v "%CD%:/app" -w /app python:3.11-slim \
                python -m unittest test_calculator.py
                '''
            }
        }
    }
}
