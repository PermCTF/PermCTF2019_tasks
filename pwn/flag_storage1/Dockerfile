FROM debian:latest

EXPOSE 3228 

RUN apt-get update
RUN apt-get -y install python ipython xinetd

WORKDIR /root/flag_storage1
COPY . .
RUN cp xinetd.conf /etc/xinetd.d/flag_storage1
RUN service xinetd restart

CMD script -c "xinetd -d"
