pipeline{
    
    agent any

    stages {
        stage("Clone Repo"){
            steps {
                echo "Cloning the repository..."
                sh "rm -fr DOT503-basic-calculator"
                sh "git clone https://github.com/mashrurAhmed/DOT503-basic-calculator.git"
                sh "git fetch"
                sh "git checkout unit-test"
            }
        }
    }
}