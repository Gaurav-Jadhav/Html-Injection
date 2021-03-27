Jenkinsfile

pipeline{
agent any
stages{
          stage("git repo & clean"){
            steps{
                    sh "rmdir" /s /q Html-Injection"
                    sh "git clone https://github.com/Gaurav-Jadhav/Html-Injection.git"
                    sh "mvn clean -f Html-Injection"
                }
         }
        
        stage("install"){
                    
                    sh "mvn install -f Html-Injection"
                 }
        }
        
        stage("test"){
                    sh "mvn test -f Html-Injection"
        
                }
        }
        
        stage("package"){
                    sh "mvn package -f Html-Injection"
        
                }        
        }
        
     }  

}



}