pipeline {
    agent any

    stages {

        stage('Tests') {
            agent {
                docker {
                    image 'python:3.7'
                    args '--network host'
                }
            }
            
            environment {
                SFTP_USERNAME = "foo"
                SFTP_PASSWORD = "pass"
                SFTP_HOSTNAME = "sftp"
                SFTP_PORT = "22"
            }
            
            steps {
                script {
                  sh "pip install -r requirements.txt --user"
                  sh 'python ./test.py'
                }                
            }
        }
    }
}
