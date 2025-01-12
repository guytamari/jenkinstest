pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install pytest'
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
