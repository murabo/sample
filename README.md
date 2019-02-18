# sample

```buildoutcfg

pip install -U pip

pip install -r requirements.txt

./manage.py migrate

./manage.py createsuperuser

./manage.py runserver
```

 
```bash

curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d  '{"username": "上で作ったusername", "password": "上で作ったpassword"}' http://127.0.0.1:8000/api-token-auth/
```