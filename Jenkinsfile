pipeline {
  agent any
  stages {
    stage('Git-Checkout') {
      steps {
        git(url: 'https://github.com/notwld/jenkins-testing', branch: 'master')
      }
    }

    stage('Run Tests') {
      parallel {
        stage('Run Tests') {
          steps {
            sh 'cd tests && python unit.py'
          }
        }

        stage('Logs') {
          steps {
            sh 'ls '
          }
        }

      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t api-dev .'
      }
    }

  }
}