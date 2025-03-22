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
        cd repo_projects/python_repo/
        python3 log_Msg.py >> /var/lib/jenkins/repo_projects/python_repo/file_log
        """
      }
    }
  }
  post {
    success {
      echo "Done !" >> file_log
    }
  }
}
