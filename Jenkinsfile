pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install python3'
                sh 'pip install pytest'
            }
        }
      stage('Test') {
            steps {
                sh 'pytest simple.py'
            }
        }
      stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
