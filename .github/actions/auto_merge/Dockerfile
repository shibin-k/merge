FROM python:3-alpine

#MAINTAINER ss

LABEL "com.github.actions.name"="Auto merge pull requests"
LABEL "com.github.actions.description"="Merge the pull requests automatically based on required conditions"
LABEL "com.github.actions.icon"="activity"
LABEL "com.github.actions.color"="green"

#COPY requirements.txt /requirements.txt
RUN	pip3 install requests #-r /requirements.txt

COPY merge_pr.py /merge_pr.py

ENTRYPOINT ["python3", "/merge_pr.py"]
