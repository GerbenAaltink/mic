## Application usage

### Prepare docker container

```docker-compose up```

This will start the development server and automatically create and apply migrations

### Create superuser

```
docker-compose exec mic sh
cd mic
python manage.py createsuperuser
```

### Create device type 
Go to http://localhost:8000/device_type

### Create building

Go to http://localhost:8000/building

### Create location

Go to http://localhost:8000/location

### Create device 
E.g. UUID: dc50cc0c-b763-4eb6-aeab-f94a71e1db8d

Go to http://localhost:8000/device