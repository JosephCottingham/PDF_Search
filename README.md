# PDF Search

![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/josephcottingham/pdf-db)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/josephcottingham/pdf-keyword_analyzer)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/josephcottingham/pdf-search)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/josephcottingham/pdf-db)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/josephcottingham/pdf-keyword_analyzer)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/josephcottingham/pdf-search)
![Website](https://img.shields.io/website?url=http%3A%2F%2Fpdf-search.net%2F)

## Deploy with Docker Compose

Navigate to the PDF_Search Folder. The local directory of this file.

```
# Takes down any exsisting containers
$ docker-compose down

# Builds new images of the project (Reflects chances made to code base)
$ docker-compose build

# Takes images and creates new containers with them. Note that DB data is store in local data directory and therefore will remain.
$ docker-compose up
```