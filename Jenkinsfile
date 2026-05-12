pipeline {
    agent any

    tools {
        sonarQube 'SonarScanner'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Amogh-Hegde/devlab-finale.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {

                withSonarQubeEnv('SonarCloud') {

                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=Amogh-Hegde_devlab-finale \
                    -Dsonar.organization=amogh-hegde \
                    -Dsonar.sources=. \
                    -Dsonar.python.version=3.11
                    '''
                }
            }
        }
    }
}