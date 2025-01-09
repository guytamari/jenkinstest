pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                    pip install python3.10
                    python3.10 -m venv ./venv
                '''
            }
        }
      stage('Test') {
            steps {
                sh '''
                    . ./venv/bin/activate
                    pytest simple.py
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
