pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/SakshiTathe/dockertodo.git'
            }
        }

        stage('Ansible Deploy') {
            steps {
                sh '''
                ansible-playbook -i ansible/inventory ansible/playbook.yml
                '''
            }
        }
    }
}

