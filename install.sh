#install somethings
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
apt-get -y update
apt-get -y upgrade
apt-get -y install redis
apt-get -y install mongodb-org
apt-get -y install python
apt-get -y install rabbitmq-server

#get pip
curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python -
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python -
export PATH="/usr/local/bin:$PATH"
#install python moudles
pip install flask
pip install flask-restful
pip install requests
pip install flask-httpauth
pip install pymongo
pip install mongoengine
pip install flask-mongoengine
pip install cherrypy
pip install flask-debugtoolbar

service mongod start
service rabbitmq-server start