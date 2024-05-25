pipeline {
    environment {
        registry = "maxskalt/devopsproject"
        registryCredential = 'docker_hub'
        dockerImage = ''
    }
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
                // Run start_apps.py minimized in the background
                bat 'start /min python C:\\git\\MaxDevOpsProject\\start_apps.py'
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
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Write Build Number to .env') {
            steps {
                script {
                    // Write the build number to the .env file
                    writeFile file: 'C:\\git\\MaxDevOpsProject\\.env', text: "BUILD_NUMBER=${env.BUILD_NUMBER}\n"
                }
            }
        }
        stage('Run Docker Backend Tests') {
            steps {
                // Execute docker_backend_testing.py
                bat 'python C:\\git\\MaxDevOpsProject\\docker_backend_testing.py'
            }
        }
        stage('Clean Environment') {
            steps {
                // Stop servers using clean_environment.py
                bat 'python C:\\git\\MaxDevOpsProject\\clean_environment.py'
            }
        }
    }
    post {
        always {
            script {
                // Clean up Docker images locally to save space
                bat "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
