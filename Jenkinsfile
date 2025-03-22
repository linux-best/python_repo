pipeline {
  agent any
  stages {
    stage('execute stage') {
      steps {
        echo "running ansible playbook"
        sh '''
        cd ~
        cd ansible/playbooks/
        ansible-playbook playbook_ansible.yml
        '''
      }
    }
    stage('logging stage') {
      steps {
        echo "sending a log_Msg"
        sh """
        cd ~
        cd workspace/my_python_job/
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
