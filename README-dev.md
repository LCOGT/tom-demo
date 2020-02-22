## Development Notes

### Local Development

```bash
cd /path/to/tom-demo             # if you haven't already
/path/to/python3.7 -m venv env   # if you haven't already
source env/bin/activate          # if you haven't already
./manage.py runserver 
```
Notes:
* Pay attention to `runserver` output. You may need to `./manage.py migrate`
* You may want to run `./manage.py createsuperuser` if (as is currenly the case) we're using an sqlite DB.

#### Developing Demonstrations of Un-released `tom_base` Features
You may want to `pip install` the `development` or some other branch of `tom_base`.
This can be done from GitHub or a locally checked out `tom_base` repository.
This is documented [here](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support).
 
To point to a locally checked out repository:
```bash
pip install -e /path/to/tom_base
```

#
### Containerized Development
```bash
cd /path/to/tom-demo
docker build -t tom-demo .
docker run -p 8080:80 tom-demo &
```
Point your browser to `localhost:8080`



#
#### LCO Deployment
_(Links below are LCO-specific and may not be available everywhere)._

This repo is deployed using the `helmPipeline()` ([LCO link](https://github.com/LCOGT/jenkins-shared-libraries/blob/master/vars/helmPipeline.md)).
Accordingly, when you `git push` to the `dev` branch, [Jenkins](http://jenkins.lco.gtn/blue/organizations/jenkins/lcogt%2Ftom-demo/activity) will
build and deploy to [tom-demo-dev.lco.gtn](http://tom-demo-dev.lco.gtn). Deployment to production, won't happen
until you tag the repo (`git tag BUMPED.VERSION.NUMBER`) and `git push --tags`. (Tags may be annotated or not). 

#
#### Colophon
This repository follows a convention in which the _repository_ `my-project`
contains the _django project_ `my_project`. Thus,
```
├── tom-demo
│   ├── tom_demo
│   ├── Dockerfile
│   ├── env
│   ├── Jenkinsfile
│   ├── manage.py
│   ├── README.md
│   └── requirements.txt
```
Here's how the repository was created:
```bash
 django-admin startproject tom_demo    # assume you have django installed (for django-admin) 
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