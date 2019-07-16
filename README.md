# nsfwoid

This is a fork of the [open_nsfw--][] project, updated for use in Wikimedia production. The project is originally based on Yahoo's [open_nsfw][].

It provides image NSFW likelihood scoring as a web service.

## Running the service

### Quick start
To run the service as a local Python process:
```
python3 api.py
```

### Dockerization via Blubber

Dockerfile generation and Docker image creation is supported with Wikimedia's Blubber tool. See the [project documentation][Blubber] for details.

**Note:** Currently broken without patching Blubber; see https://phabricator.wikimedia.org/T227919.

The branch at https://github.com/mdholloway/blubber/tree/python-fix contains the commit adding the `use-system-flag` declaration used in the Blubberfile here, cherry-picked on top of the latest Debian release.

## API usage

POST the `url` of an image, and the service will fetch it and return the probability that it's NSFW, expressed as a floating point number between 0 and 1.

``` shell
curl -d 'url=https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/263px-Wikipedia-logo-v2.svg.png' localhost:8080
0.018645038828253746
```

[open_nsfw--]: https://github.com/rahiel/open_nsfw--
[open_nsfw]: https://github.com/yahoo/open_nsfw
[docker]: https://docs.docker.com/engine/installation/
[dpkg]: https://packages.debian.org/sid/docker.io
[Blubber]: https://wikitech.wikimedia.org/wiki/Blubber
