#image
#workingdir
#copy
#run 
#cmd
#Expose
FROM python:3.9.5-slim-buster
WORKDIR /code 
COPY . /code
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]
