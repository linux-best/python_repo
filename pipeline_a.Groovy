pipeline {
    agent any

    stages {
        stage('Init') {
            steps {
                echo "Initializing......"
                script {
                    def pr = load "pipeline_b.Groovy"
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    pr.testapp()
                }
            }
        }
    }
}
