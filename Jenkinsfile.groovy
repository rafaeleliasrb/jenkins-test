pipeline {
    agent any

    stages {
        stage('Clean workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Tests') {
            agent { docker 'python:3.7' }
            
            steps {
                sh 'python --version'
                sh 'pip3 install -r requirements.txt'
                sh 'python ./test.py'
            }
        }
    }
}
