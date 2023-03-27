# QuickNode Infra Take Home

This repository contains the result of the coding challenge.
To deploy this application run 
 `sh deploy.sh`

Docker was installed on the server
To make sure docker starts up even afetr a restart the command below needs to be run
 `systemctl enable docker`

I used docker because i could easily build my doocker script on it and it can run on any operating system capable of running docker


### Continuous Integration/Delivery Requirements

When a change is made to the code we can deploy Without using a CI/CD tool by running 
    `sh deploy.sh`

If a CI/CD tool was being used these are the following steps i would be automating with the CI/CD

1. Build the Docker image.
2. Tag the built image with a `date` tag
3. Write and run a simple integration test:
    1. Start a new container instance from the built image
    2. Query the endpoint `/test`
    3. Check that the returned value equals `329d4feb-c5c0-4de5-b10c-701b44fbec4f`
4. On passing the test, I would deploy it to a kubernetes cluster or any container orchestration system currently being used

##### Containers configuration

We could have used alpine images, to reduce the image size. It depends of the usage. Sometime you need some specific system packages for python to run some extensions, so it can be useful to use official images, since it's based on Ubuntu. Compared to Alpine images, more packages are availables if needed.

Having a smaller image is also better for:
 - To reduce the size of the container when storing in a registry
 - deployment, since the `docker pull` process will be faster (also, reducing layers can be interesting, since each layer contain the previous one...)