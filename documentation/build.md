### Build the container

The Dockerfile defines three images :
- A base image with a setup for both Python and R Plumber applications
- A 'regular' image which setup the application and start the sidecar when the container is started. This image can be used for deployment on various container runtimes
- A 'lambda' image which can be used to depoy the sidecar on AWS Lambda

### Build the base image

The base image is quite long (several minutes) to build because of R. It is recommended to build it once and reuse it.


```
docker build --target base --tag crypto-sidecar-base .
```

### Build the regular container

```
docker build --target regular --tag crypto-sidecar-regular .
```

### Build the lambda container

```
docker build --target lambda --tag crypto-sidecar-lambda .
```