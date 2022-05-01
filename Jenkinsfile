pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python -m py_compile src/Calculator.py src/main.py'
                stash(name: 'compiled-results', includes: 'src/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml src/calculator_tests.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
                    agent any
                    environment {
                        VOLUME = '$(pwd)/src:/src'
                        IMAGE = 'cdrx/pyinstaller-linux:python3'
                    }
                    steps {
                        dir(path: env.BUILD_ID) {
                            unstash(name: 'compiled-results')
                            sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F Calculator.py'"
                        }
                    }
                    post {
                        success {
                            archiveArtifacts "${env.BUILD_ID}/src/dist/Calculator"
                            sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                        }
                    }
        }
    }
}