pipeline {
    agent any

    environment {
        IMAGE_NAME = "mohamed200707/flask-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        TEST_CONTAINER = "test-container"
        APP_CONTAINER = "flask-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Test Container') {
            steps {
                sh '''
                # Remove old test container
                docker stop $TEST_CONTAINER || true
                docker rm $TEST_CONTAINER || true

                # Run test container
                docker run -d \
                  --name $TEST_CONTAINER \
                  -p 5002:5050 \
                  $IMAGE_NAME:$IMAGE_TAG

                sleep 10

                echo "Checking running container..."
                docker ps | grep $TEST_CONTAINER

                echo "Testing Flask application..."
                curl --fail http://localhost:5002 || exit 1

                # Cleanup
                docker stop $TEST_CONTAINER
                docker rm $TEST_CONTAINER
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-cred',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push $IMAGE_NAME:$IMAGE_TAG

                docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest

                docker push $IMAGE_NAME:latest
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker stop $APP_CONTAINER || true
                docker rm $APP_CONTAINER || true

                docker image prune -f || true

                docker run -d \
                  --name $APP_CONTAINER \
                  -p 5050:5050 \
                  --restart unless-stopped \
                  $IMAGE_NAME:$IMAGE_TAG

                sleep 5

                docker ps

                echo "Application deployed successfully."
                '''
            }
        }
    }

    post {

        success {
            echo "CI/CD Pipeline Completed Successfully"
        }

        failure {
            echo "Pipeline Failed"

            sh '''
            docker logs $TEST_CONTAINER || true
            docker logs $APP_CONTAINER || true
            '''
        }

        always {
            sh '''
            docker image prune -f || true
            docker container prune -f || true
            '''
        }
    }
}
