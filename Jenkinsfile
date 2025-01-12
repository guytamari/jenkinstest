pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }
    stages {
        stage('Check Docker') {
            steps {
                sh 'docker --version'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
