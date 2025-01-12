pipeline {
    agent any
    stages {
        stage('Install Python3 and pip') {
            steps {
                script {
                    // Install Python3 and pip with sudo
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y python3 python3-pip'
                }
            }
        }
        
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
