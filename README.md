# whats-slot-iiitb

#### To install locally

1.create virtual environment using python3

```
virtualenv -p python3 myenv
```

2. Install dependencies using requirements.txt

```
pip3 install -r requirements.txt
```

3. In root directory of project

Activate virtual env

```
source myenv/bin/activate
```
Run app

```
flask run 
```
Go to localhost:5000


#### To run on docker

1. Ensure you have docker and docker-compose installed 

```
docker -v
```
2. Go to root directory of folder

```
docker build -t whatslot:latest .
docker run -d -p 5000:5000 whatslot
```

Go to localhost:5000

#### Pull from dockerhub and run

```
docker run -p 5000:5000 -it asquare14/whats-slot-iiitb
```

ok
