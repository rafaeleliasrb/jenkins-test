pipeline {
    agent any

    environment {
        FILTERED_FILE="./filtered_data.cvs"
        FTP_FILE="./ftp_data.cvs"
    }
    stages {
        stage("Download cancelation file") {
            agent {
                docker {
                    image 'python:3.7'
                    args '--network host'
                    reuseNode true
                }
            }
            
            environment {
                HOME = "${env.WORKSPACE}"
                SFTP_USERNAME = "foo"
                SFTP_PASSWORD = "pass"
                SFTP_HOSTNAME = "sftp"
                SFTP_PORT = "22"
                DIRECTORY="local-directory"
            }
            
            steps {
                script {
                    sh "pip install -r requirements.txt --user"
                    sh 'python ./test.py'
                }
            }
        }

        stage("Filtering valid cancelations...") {
            steps {
                sh'''#!/bin/bash -e
                    ls -lh
                '''
            }
        }  
    }
}
