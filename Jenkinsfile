pipeline {
  agent any
  environment {
    IMAGE_NAME = "flask-app"
    DOCKER_IMAGE = "${env.DOCKER_REGISTRY}/${IMAGE_NAME}:${GIT_COMMIT,short}"
    EC2_USER = credentials('ec2_user') // string credential for ec2 username
    EC2_HOST = credentials('ec2_host') // string credential for ec2 host/ip
    EC2_SSH_KEY = credentials('ec2_ssh_key') // ssh private key (Secret file credential)
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Unit Test') {
      steps {
        sh 'python -m pip install -r requirements.txt'
        sh 'python -m pytest -q || true' // optional tests
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t ${IMAGE_NAME}:${GIT_COMMIT,short} .'
      }
    }
    stage('Save Image Tar') {
      steps {
        sh 'docker save ${IMAGE_NAME}:${GIT_COMMIT,short} -o ${IMAGE_NAME}.tar'
        archiveArtifacts artifacts: '${IMAGE_NAME}.tar', fingerprint: true
      }
    }
    stage('Transfer & Deploy to EC2') {
      steps {
        // copy tar and deploy script to EC2 and run deployment
        withCredentials([file(credentialsId: 'ec2_ssh_key', variable: 'SSH_KEY')]) {
          sh 'scp -o StrictHostKeyChecking=no -i $SSH_KEY ${IMAGE_NAME}.tar ${EC2_USER}@${EC2_HOST}:/tmp/'
          sh 'scp -o StrictHostKeyChecking=no -i $SSH_KEY deploy/deploy_ec2.sh ${EC2_USER}@${EC2_HOST}:/tmp/'
          sh "ssh -o StrictHostKeyChecking=no -i $SSH_KEY ${EC2_USER}@${EC2_HOST} 'chmod +x /tmp/deploy_ec2.sh && sudo /tmp/deploy_ec2.sh /tmp/${IMAGE_NAME}.tar ${IMAGE_NAME}:${GIT_COMMIT,short}'"
        }
      }
    }
  }
}
