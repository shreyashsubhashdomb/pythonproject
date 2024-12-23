pipeline {
    agent any

    environment {
        PYTHON = 'python3'  // Define Python version
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // If you had dependencies, you could install them here
                    // Example: sh '${PYTHON} -m pip install -r requirements.txt'
                    echo 'Installing dependencies (if any)...'
                }
            }
        }

        stage('Run Python Script') {
            steps {
                echo 'Running Python script...'
                sh '${PYTHON} example.py'  // Run the example.py script
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '${PYTHON} -m unittest test_example.py'  // Run the test script
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

