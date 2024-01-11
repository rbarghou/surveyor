# Surveyor

This is a tool to allow users to be given surveys and track those surveys.

This microservice provides similar functionality to SurveyMonkey or similar services
but takes advantage of [SurveyJS](https://surveyjs.io/) which allows you to build 
surveys in a json language.

This microservice serves an api which allows users to produce surveys that do not
require user authentication and have per-user urls.  Additionally, it provides a
simple example of a html page that can be used to present the survey, however
it is recommended to serve the surveys using an external client side app. 

## Overview

This is a containerized microservice with several components such as ...

1. a dockerfile that describes the build of a basic drf service
2. a docker-compose file to define a development environment including the supporting db
3. a setup.py that defines the installation of the client that talks to this microservice
4. a single-page jquery app that is rendered at the root of the service by the django
5. a django rest framework for other microservices to talk to.
6. an admin interface for creating and adding surveys
7. an openapi client to interface with the microservice

## Dev Setup

* `docker compose up`

## Dev cleanup
* `docker-compose down --volume`

## Interacting with service
After `docker compose up`
  
### Surveyor
* Running at http://localhost:8088

When running the development environment there are several ways to interact with it.
Firstly, the service can be accessed through a browser at django admin at 
http://localhost:8088/admin with the username: "root" and the password: "password"

### Example Survey
You can see an example survey here: http://localhost:8088/s/7b96a46e-b284-4ea2-b6bf-fa3207b9a8c1
and its api entry here: http://localhost:8088/surveys/7b96a46e-b284-4ea2-b6bf-fa3207b9a8c1/
its template here: http://localhost:8088/survey_templates/e50c6ab9-0cd4-426e-8e77-1b2fcca4fb9b/
If you take the survey, you should see the values updated in the api.
Additionally if you want to make new serveys you can do so either through the api or the admin
http://localhost:8088/admin/survey/surveytemplate/add/

To develop your own survey you can use this free builder: https://surveyjs.io/create-free-survey

### API Interaction
For this example authentication is set up using basic-auth, session-auth, and token auth

Token authentication is available at http://localhost:8088/api-token-auth/

To curl this you can use
```bash
> curl -d "username=root&password=password" -X POST http://localhost:8088/api-token-auth/
{"token":"8469ab271d48800ca3c5638ce0a58694e427c121"}%
```

If you have `jq` installed, then this can be parsed and assigned to a variable as follows

```bash
> export SURVEYOR_TOKEN=$(curl -s -d "username=root&password=password" -X POST http://localhost:8088/api-token-auth/ | jq '.token' | xargs echo)
> echo $SURVEYOR_TOKEN
8469ab271d48800ca3c5638ce0a58694e427c121
```

Then the api can be interacted with by using the `Authorization` header as follows.  This is supported by
using the DRF token autorization: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

```bash
> curl -H "Authorization: Token $SURVEYOR_TOKEN" http://localhost:8088/
{"surveys":"http://localhost:8088/surveys/","survey_templates":"http://localhost:8088/survey_templates/"}%
> curl -s -H "Authorization: Token $SURVEYOR_TOKEN" http://localhost:8088/surveys/7b96a46e-b284-4ea2-b6bf-fa3207b9a8c1/ | jq
{
  "id": "7b96a46e-b284-4ea2-b6bf-fa3207b9a8c1",
  "survey_url": "http://localhost:8088/s/7b96a46e-b284-4ea2-b6bf-fa3207b9a8c1",
  "created": "2020-11-05T15:13:49.356000Z",
  "modified": "2020-11-09T14:48:52.953762Z",
  "answers": {
    "question1": "item2"
  },
  "user_uuid": null,
  "complete": false,
  "survey_template": "e50c6ab9-0cd4-426e-8e77-1b2fcca4fb9b"
}
```


## Tests

Tests can be run with

`docker compsoe -f docker-compose-tests.yaml up`

Results can be found in the `./artifacts` folder.  Both a txt and html report are generated.

