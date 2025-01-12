pipeline {
    agent any
    stages {
        stage('Install Python3 and pip') {
            steps {
                script {
                    // Ensure Python3 and pip3 are installed
                    sh 'apt-get update -y'
                    sh 'apt-get install -y python3 python3-pip'
                }
            }
        }
        
        stage('Build') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install pytest'
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
