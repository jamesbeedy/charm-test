#!/bin/bash

set -eux

rm -rf build/
mkdir build/

docker run -it --rm \
    -v `pwd`/requirements.txt:/srv/requirements.txt \
    -v `pwd`/build:/srv/build \
    quay.io/pypa/manylinux2014_x86_64 \
    /bin/sh -c '/opt/python/cp38-cp38/bin/python -m venv --copies --clear /srv/build/venv &&
                /opt/python/cp38-cp38/bin/pip install -r /srv/requirements.txt \
                -t /srv/build/venv/lib/python3.8/site-packages && chown -R 1000:1000 /srv/build'
