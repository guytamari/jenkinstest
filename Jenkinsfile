pipeline {
    agent any
    stages {
        stage('Install Python3 and pip') {
            steps {
                script {
                    // Manually install pip if not already available
                    sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                    sh 'python3 get-pip.py'
                }
            }
        }
        stage('Check Docker') {
            steps {
                sh 'docker --version'
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
