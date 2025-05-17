pipeline {
  agent any
  stages {
    stage('execute stage') {
      steps {
        echo "running ansible playbook"
        sh '''
        cd ~
        cd repo_projects/ansible/playbooks/
        ansible-playbook playbook_ansible.yml
        '''
      }
    }
    stage('logging stage') {
      steps {
        echo "sending a log_Msg"
        sh """
        cd ~
        cd workspace/my_python_Job/
        python3 log_Msg.py >> file_log
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
