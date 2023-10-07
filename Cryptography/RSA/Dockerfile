FROM alpine:3.18.4

RUN apk add python3 py-pip
COPY RSA.py /app/RSA.py
RUN python3 -m pip install rsa

EXPOSE 3434

WORKDIR /app
CMD ["python3", "RSA.py"]