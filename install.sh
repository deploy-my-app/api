
apt-get -y update
apt-get -y upgrade
apt-get -y install redis
apt-get -y install mongodb
apt-get -y install python

curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python -
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python -
export PATH="/usr/local/bin:$PATH"

pip install flask
pip install flask-restful
pip install requests
pip install flask-httpauth
pip install pymongo
pip install mongoengine
pip install cherrypy