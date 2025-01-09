pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh ' . .env/bin/activate ' 
                // withPythonEnv('/usr/bin/python3.8') {
                // sh 'echo "Job is starting" '
                // }            
                
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
