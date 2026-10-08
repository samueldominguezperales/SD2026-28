FROM ubuntu:latest

#Argumento del sistema operativo para que el GUI no cause problemas
ARG DEBIAN_FROTEND=noninteractive

#Se instala python
# apt update
RUN apt-get update && 
RUN apt-get install -y python3
RUN apt-get install -y pytho3-pip
RUN apt-get install -y git 
RUn apt get install -y curl

RUN apt-get upfate && \
    apt-get install -y \
    python3 python-pip \
    git curl && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /chekitas

RUN git clone https://github.com/ChekaSabe/SD2026-2B.git

CMD ["sleep", "infinity"]
# CMD ["/bin/bash"]
# CMD ["python3", "RCDD_2026/main.py"]