FROM  rstudio/plumber:v1.0.0
# Build args
ARG R_FILES_LOCAL_FOLDER_PATH=./r
ARG R_DEPENDENCY_FILE=dependencies.r
ARG R_FUNCTIONS_FILE=functions.r
ARG R_MAIN_FILE=main.r
# Set locales
ENV PYTHONIOENCODING=UTF-8
# Set WORKDIR
WORKDIR .
# Copy R files
COPY $R_FILES_LOCAL_FOLDER_PATH ./r
# Install R dependencies
RUN Rscript "./r/dependencies.r"
# Install python 3.8
RUN apt-get -y install software-properties-common
RUN apt-get -y install python3.8
RUN apt-get -y install python3-pip
# Copy Python app
COPY ./requirements.txt ./requirements.txt
COPY ./main ./main
# Install python dependencies
RUN pip3 install -r ./requirements.txt
# Env. used to configure the applications
ENV R_APPLICATION_PORT=4224
ENV R_APPLICATION_HOST="127.0.0.1"
ENV FUNCTIONS_PATH="./r/functions.r"
ENV PYTHON_APP_PORT=8000
ENV PYTHON_APP_HOST="0.0.0.0"
# COPY start script
COPY ./start_sidecar.sh ./start_sidecar.sh
RUN chmod +x start_sidecar.sh 
# Sidecar entrypoint
ENTRYPOINT ./start_sidecar.sh