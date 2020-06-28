pipeline {
    agent any

    stages {

        stage('Tests') {
            agent {
                docker {
                    image 'python:3.7'
                }
            }
            
            steps {
                environment {
                    HOME = ${env.WORKSPACE}
                    SFTP_USERNAME = ${env.SFTP_USERNAME}
                    SFTP_PASSWORD = ${env.SFTP_PASSWORD}
                    SFTP_HOSTNAME = ${env.SFTP_HOSTNAME}
                    SFTP_PORT = ${env.SFTP_PORT}
                }
                script {
                  sh "pip install -r requirements.txt --user"
                  sh 'python ./test.py'
                }                
            }
        }
    }
}
