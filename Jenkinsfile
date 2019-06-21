pipeline {
    agent { label 'jenkins-deploy-pipeline-slave-01'}
   stages {
//   def mvnHome

   stage('Preparation') { // for display purposes
      steps {
      // Get some code from a GitHub repository
      git 'https://github.com/plaid/plaid-python'
      // Get the Maven tool.
      // ** NOTE: This 'M3' Maven tool must be configured
      // **       in the global configuration.           
      }
   }
   stage('Build') {
      steps{
      // Run the maven build
         sh "'${mvnHome}/bin/mvn' -Dmaven.test.failure.ignore clean package"
      }
   }
   stage('Results') {
      steps {
      junit '**/target/surefire-reports/TEST-*.xml'
      archive 'target/*.jar'
      }
   }
}
}
