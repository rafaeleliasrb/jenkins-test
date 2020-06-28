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
                withEnv(["HOME=${env.WORKSPACE}"]) {
                  sh "pip install -r requirements.txt --user"
                  sh 'python ./test.py'
                }                
            }
        }
    }
}
