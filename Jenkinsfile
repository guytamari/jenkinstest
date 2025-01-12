pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'building python file'         
                
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
