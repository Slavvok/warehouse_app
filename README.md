Little project using Flask, Flask-Restful, Swagger

Documentation
```
http://localhost:5000/api/spec.json
```

Do before run
```
flask db init && flask db migrate -m "migration" && flask db upgrade
```

Run 
```python
python main.py
```

Test
```python
python tests.py
```

Postman
```
https://www.getpostman.com/collections/8126201e49161843a6df
```