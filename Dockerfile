# Use the official Airflow image as the base
FROM apache/airflow:2.9.2

# Install PHP
USER root
RUN apt-get update && apt-get install -y php php-cli

# Install Golang
RUN apt-get install -y golang

# Install Node.js and npm
RUN apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# To install pre-requirements for python if needed
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --user -r ./requirements.txt

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Jakarta

# Ensure all commands are available in the PATH

# This below PATH required if you have engine run on golang
# ENV PATH="/usr/local/go/bin:/usr/local/node/bin:${PATH}"

# Switch back to the airflow user
USER airflow