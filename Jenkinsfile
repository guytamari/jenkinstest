pipeline {
    agent any
    stages {
        // stage('Build') {
        //     steps {
        //         sh 'pip3 install pytest'
        //     }
        // }
        stage('Test') {
            steps {
                sh 'pipx run pytest test.py'

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy'
            }
        }
    }
}
