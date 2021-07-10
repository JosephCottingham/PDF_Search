# PDF_Search

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