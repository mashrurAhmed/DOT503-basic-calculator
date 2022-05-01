pipeline{
    
    agent any

    stages {
        stage("Clone Repo"){
            steps {
                echo "Cloning the repository..."
                sh "git clone https://github.com/mashrurAhmed/DOT503-basic-calculator.git"
                sh "git fetch"
                sh "git checkout unit-test"
            }
        }
    }
}