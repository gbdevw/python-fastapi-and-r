Rscript ./r/main.r &
uvicorn main.app:app --host $PYTHON_APP_HOST --port $PYTHON_APP_PORT
