#!/bin/bash

cd `dirname ${0}`

docker run --rm -v $(pwd):/app covid19-cuckoo
