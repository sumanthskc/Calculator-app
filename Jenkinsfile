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
                script {
                    sh 'docker build -t calculator-app .'
                }
            }
        }

        stage('Run Tests in Container') {
            steps {
                script {
                    sh 'docker run --rm calculator-app'
                }
            }
        }
    }
}

