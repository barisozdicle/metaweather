def gv

pipeline {
    agent any
    parameters {
        booleanParam(name: 'executeTests', defaultValue: true, description: '')
    }
    stages {
        stage("init") {
            steps {
                script {
                   gv = load "script.groovy"
                }
            }
        }
        stage("build") {
            steps {
                sh """
                  cp -p /var/lib/jenkins/workspace/Weather/Dockerfile /var/lib/jenkins/workspace/Weather/Dockerfile
                  docker build . -t weather
                """
            }
        }
        stage("test") {
            when {
                expression {
                    params.executeTests
                }
            }
            steps {
                sh """
                  docker run weather
                """
            }
        }
    }
}
