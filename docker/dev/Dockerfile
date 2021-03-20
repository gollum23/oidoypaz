FROM python:3.7

RUN apt-get update && apt-get install -y gcc gettext postgresql-client libpq-dev \
    libjpeg-dev wget zsh

COPY base.txt /tmp/base.txt
RUN pip install -r /tmp/base.txt

RUN mkdir /var/run/sshd

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

RUN chsh -s /bin/zsh root
