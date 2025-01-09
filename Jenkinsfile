pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'build'
            }
        }
      stage('Test') {
            steps {
                bat 'pytest simple.py'
            }
        }
      stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
