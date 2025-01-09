pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage('Build') {
            steps {
                withPythonEnv('/usr/bin/python3.8') {
                sh 'echo "Job is starting" '
                }            
                
            }
        }
      stage('Test') {
            steps {
                withPythonEnv('/usr/bin/python3.8') {
                sh 'pytest simple.py '
                }            
            }
        }
      stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
