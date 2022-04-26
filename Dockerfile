FROM python:latest
COPY . /app
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install 
RUN aws configure set region us-east-1 
RUN aws configure set aws_access_key_id AKIAX24HVZXMHNJQ7DNV
RUN aws configure set aws_secret_access_key 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
RUN aws configure set output json
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5001

CMD [ "python3", "frontend.py" ]


