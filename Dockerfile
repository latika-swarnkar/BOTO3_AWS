FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD [ "frontend.py" ]