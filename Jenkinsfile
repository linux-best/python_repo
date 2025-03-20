pipeline {
  agent any
  stages {
    stage('checkout stage') {
      steps {
        echo "running ansible playbook"
        sh '''
        cd ~
        cd ansible/playbooks/
        ansible_playbook playbook_ansible.yml
        '''
      }
    }
  }
}
