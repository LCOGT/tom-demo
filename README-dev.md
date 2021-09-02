## Development Notes

### Local Development
In this context, "Local" means on your local machine and there are a few ways of doing this:
 - in your virtual environment, via `./manage.py runserver`
 - dockerized, via `docker run`
 - dockerized, via `docker-compose`

Each are described below, but for local development, there's a pre-requisite that must come first:

#### Setting Up a Local `tom-demo` Database
##### Start up the Database Server 
As of `tom-demo` version 0.3.x, we are demonstrating the use of an external PostgreSQL database.
Getting that database up and running is a pre-requisite to all of the local development methods. Here's how:
```bash
docker run --name tom-demo-postgres
           -v /var/lib/postgresql/data
           -p 5432:5432
           -d
           postgres:11.1

docker exec -it tom-demo-postgres /bin/bash  # start a shell inside the postgres container
createdb -U postgres tom_demo                # create the tom_demo database
exit                                         # leave the container, back to your shell
```

##### Prepare the `tom-demo` Database
If this is your first time creating the `tom_demo` database, you must create the tables and put
some data in the database that you just created.
```bash
# make sure you are in your virtual environment, then
./manage.py migrate           # create the tables
./manage.py collectstatic     # gather up the static files for serving
```
#
Now that you have a database server up and running on your local machine, consider these alternatives for local development your TOM:

#### Aternative 1: Running `tom-demo` in your virtual environment, via `./manage.py runserver`
<details>
<summary>Click to expand.</summary>

```bash
./manage.py runserver &
# see the output "Starting development server at <URL>" for where to point your browser.
```
</details>

#### Alternative 2: Running `tom-demo` dockerized, via `docker run`
<details>
<summary>Click to expand.</summary>

```bash
docker build -t tom-demo .                     # build a docker image of your current sandbox
docker run --network="host" tom-demo &
# point your browser at localhost 
```
The switch `--network="host"` tells your TOMs docker container to use the host machines network. This
allows your TOM to look for a postgresql database at `127.0.0.1:5432` which is where you set it up above.
If you don't specify `--network="host"`, then the `tom-demo` container expects the database to be running
_in the `tom-demo` container_ at `127.0.0.1:5432` (and there's no database running there). 

_NOTE: the `--network="hosts"` method is not secure and should never be used outside your development environment._ 
</details>

#### Alternative 3: Running `tom-demo` dockerized, via `docker-compose`
<details>
<summary>Click to expand.</summary>
# TODO...
</details>


### Developing Demonstrations of Un-released `tom_base` Features
You may want to `pip install` into your `tom-demo` virtual environment the `development` or some other pre-release
branch of `tom_base`.
This can be done from GitHub or a locally checked out `tom_base` repository.
This is documented [here](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support).
 
To point to a locally checked out repository:
```bash
pip install -e /path/to/tom_base
```
#
### LCO Deployment
_(Links below are LCO-specific and may not be available everywhere)._

This repo is deployed using the `helmPipeline()` ([LCO link](https://github.com/LCOGT/jenkins-shared-libraries/blob/master/vars/helmPipeline.md)).
Accordingly, when you `git push` to the `dev` branch, [Jenkins](http://jenkins.lco.gtn/blue/organizations/jenkins/lcogt%2Ftom-demo/activity) will
build and deploy to [tom-demo-dev.lco.gtn](http://tom-demo-dev.lco.gtn). Deployment to production, won't happen
until you tag the repo (`git tag BUMPED.VERSION.NUMBER`) and `git push --tags`. (Tags may be annotated or not). 

#
### Colophon
This repository follows a convention in which the _repository_ `my-project`
contains the _django project_ `my_project`. Thus,
```
├── tom-demo
│   ├── tom_demo_base
│   ├── Dockerfile
│   ├── env
│   ├── Jenkinsfile
│   ├── manage.py
│   ├── README.md
│   └── requirements.txt
```
Here's how the repository was created:
```bash
django-admin startproject tom_demo    # django was installed (for django-admin) 
cd tom_demo/
/opt/lcogt-python37/bin/python3.7 -m venv env
source env/bin/activate
emacs tom_demo/settings.py &        # add tom_setup to settings.py INSTALLED_APPS
./manage.py tom_setup
./manage.py migrate
cd ..                               # Here we create the directory struture described above
mv tom_demo tom-demo                # This works around an issue with tom_setup that 
cd tom-demo
git init                            # from here on the commit history tells the story
```
