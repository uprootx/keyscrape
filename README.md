# keyscrape

A simple utility to refresh a list of public ssh keys from Github.

Write each user you'd like to scrape in a ```config.py``` file.

From this repo run

```docker build -t keyscrape .```

```docker run --rm -ti -v $(pwd):/usr/src/app keyscrape:latest```