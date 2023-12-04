FROM ultralytics/ultralytics:latest
RUN pip3 install flask 
RUN pip3 install flask-cors
WORKDIR /usr/src/ultralytics
COPY . .
CMD ["python3", "./server/server.py"]

