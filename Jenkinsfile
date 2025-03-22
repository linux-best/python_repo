pipeline {
  agent any
  stages {
    stage('execute stage') {
      steps {
        echo "running ansible playbook"
        sh '''
        cd ~
        cd repo_project/ansible/playbooks/
        ansible-playbook playbook_ansible.yml
        '''
      }
    }
    stage('logging stage') {
      steps {
        echo "sending a log_Msg"
        sh """
        cd ~
        cd repo_project/python_repo/
        python3 python_1.py >> file10
        """
      }
    }
  }
  post {
    success {
      echo "Done !"
    }
  }
}
