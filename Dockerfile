From jenkins/jenkins:jdk21
USER root
RUN apt update && apt install python3 python3-pip python3-venv -y
USER jenkins