pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sumanthskc/Calculator-app.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                docker build -t calculator-app .
            }
        }

        stage('Run Tests in Container') {
            steps {
                docker run --rm calculator-app
            }
        }
    }
}

