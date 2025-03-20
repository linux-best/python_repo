pipeline {
  agent any
  stages {
    stage('checkout stage') {
      steps {
        echo "running ansible playbook"
        sh '''
        cd ~
        cd ansible/playbooks/
        ansible-playbook playbook_ansible.yml
        '''
      }
    }
  }
}
