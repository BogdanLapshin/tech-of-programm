pipeline {
    options {timestamps()}
    
    agent {
        docker {
            image 'alpine'
            args '-u=\"root\"'
        }
    }

    stages {
        stage("checkout scm") {
            agent any
            steps {
                checkout scm
            }
        }
        stage('build') {
            steps {
                echo "building..."
                echo "building completed"
                echo "kovalskyi ;)"
            }
        }
        stage('test') {
            steps {
                sh '''
                    apk add --update python3 py-pip
                    pip install xmlrunner
                    python3 tests.py
                '''
            }
            post {
                success {
                    echo "finally..."
                }
                failure {
                    echo "what? ?!?!? !?"
                }
            }
        }
    }
}