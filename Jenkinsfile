pipeline {
  agent any
  stages {
    stage('checkout stage') {
      steps {
        echo "running ansible playbook"
        sh '''
        ansible_playbook playbook_ansible.yml
        '''
      }
    }
  }
}
