# Multi-stage build - Build base image with R & Python
FROM ubuntu:latest AS base
# Set locales for R & Python
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LC_COLLATE=en_US.UTF-8 \
    LC_CTYPE=en_US.UTF-8 \
    LC_MONETARY=en_US.UTF-8 \
    LC_NUMERIC=en_US.UTF-8 \
    LC_TIME=en_US.UTF-8
# Install dev tools, libsodium, libcurl, R & Python
RUN apt-get --no-install-recommends --yes install software-properties-common
RUN apt-get --no-install-recommends --yes install \
    build-essential \
    libsodium-dev \
    libcurl4-openssl-dev \
    littler \
    r-cran-rcpp \
    python3.8 \
    python3-pip
# Install R Plumber
RUN Rscript -e "install.packages(\"plumber\")"

# Multi-stage build - Build regular container from base image
FROM base AS regular
# Build args
ARG R_FILES_LOCAL_FOLDER_PATH=./r
# Set WORKDIR
WORKDIR .
# Copy R files
COPY $R_FILES_LOCAL_FOLDER_PATH ./r
# Copy Python app
COPY ./requirements.txt ./requirements.txt
COPY ./main ./main
# Install python dependencies
RUN pip3 install -r ./requirements.txt
# Install R dependencies
RUN Rscript "./r/dependencies.r"
# Env. used to configure the applications
ENV R_APPLICATION_PORT=4224 \
    R_APPLICATION_HOST="127.0.0.1" \
    R_FUNCTIONS_PATH="./r/functions/functions.r" \
    PYTHON_APP_PORT=8000 \
    PYTHON_APP_HOST="0.0.0.0"
# Tell which ports should be exposed
EXPOSE $PYTHON_APP_PORT
# COPY start script
COPY ./docker-utils/start_sidecar.sh ./start_sidecar.sh
RUN chmod +x start_sidecar.sh 
# Sidecar entrypoint
ENTRYPOINT ./start_sidecar.sh

# Multi-stage build - Build AWS Lambda container from base image
FROM base AS lambda
# Build args
ARG R_FILES_LOCAL_FOLDER_PATH=./r
# Set WORKDIR
WORKDIR .
# Install Lambda Runtime Interface Client for Python
RUN pip3 install awslambdaric
# Add Lambda Runtime Interface Emulator and use a script in the ENTRYPOINT for simpler local runs
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
# Copy R files
COPY $R_FILES_LOCAL_FOLDER_PATH ./r
# Copy Python app
COPY ./requirements.txt ./requirements.txt
COPY ./main ./main
# Install python dependencies
RUN pip3 install -r ./requirements.txt
# Install R dependencies
RUN Rscript "./r/dependencies.r"
# Env. used to configure the applications
ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    R_APPLICATION_PORT=4224 \
    R_APPLICATION_HOST="127.0.0.1" \
    R_FUNCTIONS_PATH="./r/functions/functions.r"
# COPY start script
COPY ./docker-utils/lambda_entry.sh /entry.sh
RUN chmod 755 /usr/bin/aws-lambda-rie /entry.sh
# Lambda entrypoint
ENTRYPOINT [ "/entry.sh" ]
CMD [ "main.app.handler" ]