FROM lgatica/python-alpine:latest

# Place your flask application on the server
COPY . /app
WORKDIR /app
    
# Install requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
    
ENTRYPOINT ["python"]
CMD ["app.py"]
