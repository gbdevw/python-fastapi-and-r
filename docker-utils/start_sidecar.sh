#!/bin/bash

# Start R sidecar
Rscript ./r/main.r &

# Check if R sidecar is OK before starting the Python app.
CALL_COUNT=1
MAX_CALLS=10
CURL_STATUS=1
R_APPLICATION_PORT="${R_APPLICATION_PORT:-4224}"
R_HEALTH_URL="http://127.0.0.1:"$R_APPLICATION_PORT"/health"

echo "BEGIN - R sidecar health check"

while [ $CALL_COUNT -le $MAX_CALLS ]
do 
    # Call R sidecar health endpoint
    echo "Calling R sidecar health endpoint"
    CURL_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $R_HEALTH_URL)
    # Check response
    if [ $CURL_STATUS -ne 200 ]
    then
        # Wait before next call
        echo "Retry sidecar healthcheck"
        sleep .5
    else
        # Break loop
        echo "Sidecar OK"
        CALL_COUNT=$MAX_CALLS
    fi
    # Increase call counts
    ((CALL_COUNT++))
done

# Start Python application
uvicorn main.app:app --host $PYTHON_APP_HOST --port $PYTHON_APP_PORT
