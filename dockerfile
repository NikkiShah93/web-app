## selecting a small base image
FROM python:3.10.0-alpine3.15
## setting the working dir
WORKDIR /app
## and copy the needed content
COPY requirements.txt .
## installing all the required packages
RUN pip install -r requirements.txt
COPY src src
## running our docker on port 5000
EXPOSE 5000
## using the health entry point
## to check on our container
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1 
## creating an entry point 
ENTRYPOINT [ "python", "./src/app.py"]