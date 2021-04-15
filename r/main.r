# Load plubmer librairy
library(plumber)

function_path <- Sys.getenv(c("R_FUNCTIONS_PATH"), unset="./r/functions/functions.r")
r_application_port <- as.integer(Sys.getenv(c("R_APPLICATION_PORT"), unset="4224"))
r_application_host <- Sys.getenv(c("R_APPLICATION_HOST"), unset="127.0.0.1")
# 'plumber.R' is the location of the file shown above
pr(function_path) %>%
  pr_run(host=r_application_host, port=r_application_port)