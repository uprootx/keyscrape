# keyscrape

A simple utility to refresh a list of public ssh keys from Github.

Write each user you'd like to scrape on a new line and save it as a ```config.py``` file.

Example:

```
  user1
  user2
  user3
```

The results will be saved in a ```keys``` file.


From this repo run

```docker build -t keyscrape .```

```docker run --rm -ti -v $(pwd):/usr/src/app keyscrape:latest```