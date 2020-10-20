FROM python:3.8.5
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENV ENVIROMENT dev
ENTRYPOINT ["python"]
CMD ["app.py"]