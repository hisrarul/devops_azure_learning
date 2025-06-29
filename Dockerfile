From jenkins/jenkins:jdk21
User root
RUN apt update && apt install python3 python3-pip -y
User jenkins