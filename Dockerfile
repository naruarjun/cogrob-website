FROM klakegg/hugo:ext-ubuntu

# Install dependencies
RUN apt-get update && apt-get install -y \
    php5-mcrypt \
    python-pip

RUN pip install academic

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]

