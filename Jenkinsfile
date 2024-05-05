pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Clone the GitHub repository
                git 'https://github.com/MSkalt/DevOpsProject.git'
            }
        }
        stage('Start Applications') {
            steps {
                // Run start_apps.py to start the required services
                bat 'python C:\\git\\MaxDevOpsProject\\start_apps.py'
            }
        }
        stage('Run Backend Tests') {
            steps {
                // Execute backend tests
                bat 'python C:\\git\\MaxDevOpsProject\\backend_testing.py'
            }
        }
        stage('Run Frontend Tests') {
            steps {
                // Execute frontend tests
                bat 'python C:\\git\\MaxDevOpsProject\\frontend_testing.py'
            }
        }
        stage('Run Combined Tests') {
            steps {
                // Execute combined tests
                bat 'python C:\\git\\MaxDevOpsProject\\combined_testing.py'
            }
        }
        stage('Clean Environment') {
            steps {
                // Stop servers using clean_environment.py
                bat 'python C:\\git\\MaxDevOpsProject\\clean_environment.py'
            }
        }
    }
}
