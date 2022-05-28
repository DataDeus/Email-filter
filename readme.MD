# Overview

This script is a python function: filter() that takes an email sentence and determines it's matching response.
For referrence, [read here]('https://careers.foondamate.com/machine-learning-engineer-remote/foondamate-ml-engineer-coding-challenge-001')

## How function works
The function uses NLTK chunking and POS tags (VBZ, TO, VBD, MD, VB, NN, NNP, PRP, and PRP$ ) to determine if a sentence is interrogative ('Student wants to know if can share') or delcarative ('Student has shared') and as an extra feature, suggestive ('Student might share email')

# Build and docker image

Following commands need to be run from the root directory.

First, build the docker image by running the command below;

`docker build -t filter .`

## Run function locally

To run the built image;

`docker run filter`

## Use function in another code base

-  you can simply CMD + c, CMD + v
or...
- import the function in your python code;
**(ensure that the 'filter.py' file is in the same directory as your code)**
**(make sure to install all needed dependencies in the 'requirements.txt' file)**

`from filter import filter` 

and you can call in your code;
`filter()`

## Run tests

Grab the ID of the docker container running the script and run the following command;

`docker exec -it <container ID > sh`

Once you are in a shell, run the command below;

`pytest`

### Sample request
`filter('may i share your email')` should output, 'Student wants to know if can share'
