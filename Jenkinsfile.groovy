pipeline {
    agent any

    stages {
        stage('Clean workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Tests') {
            agent {
                docker {
                    image 'python:3.7'
                    args '--network jenkins'
                }
            }
            agent { docker 'python:3.7' }
            
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                  sh "pip install -r requirements.txt --user"
                  sh 'python ./test.py'
                }                
            }
        }
    }
}
