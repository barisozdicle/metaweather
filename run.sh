#!/usr/bin/env bash

docker build . -t weather
docker run weather