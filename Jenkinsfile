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
                pytest
            }
        }
      stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
