pipeline {
    agent any

    stages {
        options { timestamps () }
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
            
            steps{
                script {
                    sendMsgToSlack("Begin the cancellation process...")
                    sh "pip install -r requirements.txt --user"
                    sh 'python ./test.py'
                }
            }
        }

        stage('Upload a CSV') {
            steps {
                script {
                    def inputFile = input message: 'Upload file', parameters: [file(name: "cancel_report.csv", description: 'Upload only CSV file')]
                    echo "FILE PATH: '${inputFile}'"
                    def filePath = "${inputFile}"
                    //saves the file on the workspace
                    sh "cat ${filePath} > ${FTP_FILE}"
                    //delete the uploaded file
                    // inputFile.delete()
                }
            }
        }
        
    }
}
