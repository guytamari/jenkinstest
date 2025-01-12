pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'installing dep'
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
