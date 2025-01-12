pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'installing dep'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pytest
                '''
                
            }
        }
      stage('Test') {
            steps {
               sh '''
                    . venv/bin/activate
                    pytest tests
                '''
            }
        }
      stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
