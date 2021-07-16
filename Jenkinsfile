// Declarative Pipeline
pipeline {
    // Set up the docker agent the jenkins slave will run on
    //  agent { docker { image 'python:3.8' } }
    agent none
    environment {
        VERSION_NO         = '1.0'
        repo               = "bchewy/eti_game"
        registryCredential = 'dockerhub'
        dockerImg          = ''
        
    }

    stages {
        stage('Initialize'){
            agent { dockerfile true  }
            steps{
                script{
                    def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('Build') {
            agent { dockerfile true  }
            steps {
                echo 'Building..'
                sh 'python --version'
                sh 'python3 py_compileCheck.py'
            }
        }
        stage('Test') {
            agent { dockerfile true  }
            steps {
                echo 'Testing..'
                // Run pytest and check coverage of explicit files to 90% Coverage./
                sh 'pytest  --cov --cov-fail-under 35 --junitxml=coverage.xml'
            }
            post {
                always {
                    junit 'coverage.xml'
                }
            }
        }
        stage('Deploy') {
            agent { label 'master' }

            steps {
                echo 'Deploying....'
                // Push to dockerhub image repository with tags per mergeid/featurebranch or etc.
                script{
                    dockerImg = docker.build repo+":$BUILD_NUMBER"
                    docker.withRegistry( '', registryCredential ) {
                        dockerImg.push()
                    }
                    sh 'docker rmi $repo:$BUILD_NUMBER'
                }
            }
        }
    }
}

// Scripted Pipeline
// node{
//     Stage 'Checkout'
//         echo 'Checkout Stage'
//         checkout scm

//     Stage 'Build'
//         echo 'Building Stage'
//         sh 'python --version'
//         sh 'python3 Game/py_compileCheck.py'

//     Stage 'Test'
//         echo 'Test Stage'
//         //Pytest here

//     Stage 'Deploy'
//         echo 'Test Stage'

// }    agent any
        stage('Build') {
        stage('Build') {
    agent any
    agent any
            steps { sh 'docker build -t eti_game .' }
        stage('Build') {
        stage('Build') {
    agent any
    }
