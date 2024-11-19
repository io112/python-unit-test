pipeline {
    agent {
        docker {
            image 'python:latest'
            args '-u root'
        }
    }
    stages {
        stage("deps") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage("test") {
            steps {
                sh 'coverage run -m nose2'
            }
        }
        stage("reports") {
            steps {
                sh 'coverage report'
                sh 'coverage html'
                sh 'coverage xml'
            }
        }
    }
    post {
        success {
            archiveAcrtifacts 'htmlcov/*'
        }
    }
}