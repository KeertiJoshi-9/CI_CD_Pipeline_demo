#Getting OS and python from dockerhub
FROM python:3.13.0-slim-bullseye

#where do you want to store all your files -- You root folder -- docker folder
WORKDIR /docker

#Copying dependencies of apps we need. (all from pip freeze)
COPY requirements.txt ./
#Installing above dependencies of apps we need from requirements.txt
RUN pip install -r requirements.txt

#to copy and send our code, models, file and all other stuff:
COPY . .

#to run the command, we use CMD finally. 
CMD ["python", "-m", "flask", "--app", "loanapp", "run", "--host=0.0.0.0"]