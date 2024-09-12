FROM python:3.8
USER root
RUN mdir /app
COPY ./app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW__CORE_ENABLE_XCOM_PICKLING=True
RUN airflow db init
RUN airflow users create -e rajat.k.singh64@gmail.com -f Rajat -l Singh -p rjsingh -u rjsingh
RUN chmod 777 start.sh 
RUN apt update -y && apt install awscli -y 
ENTRYPOINT [ "/bin/sh" ]
CMD [ "start.sh"]