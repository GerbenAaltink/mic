## Application usage

### Prepare docker container

```docker-compose up```

This will start the development server and automatically create and apply migrations


### General overview of end points
Go to http://localhost:8000/


### Create device type 
Go to http://localhost:8000/device_type

### Create building

Go to http://localhost:8000/building

### Create location
Make sure you have created:
 - building

Go to http://localhost:8000/location

### Create device 
Make sure you have created:
 - location

E.g. UUID: dc50cc0c-b763-4eb6-aeab-f94a71e1db8d

Go to http://localhost:8000/device

### Create registration
Make sure you have created:
 - device 

Go to http://localhost:8000/registration