pipeline {
    agent {
        docker {
            image 'python:3.12-alpine'
            args '-u root'
        }
    }
    stages {
        stage("deps") {
            steps {
                sh 'ping pypi.org'
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
            recordCoverage(tools: [[parser: 'COBERTURA']],
            id: 'cobertura', name: 'Cobertura Coverage',
            sourceCodeRetention: 'EVERY_BUILD')
        }
    }
}