
# Project description
Simple application for registration of device usage. Device types, devices and locations are manageable using the django admin. For registration of usage percentage is a rest api available.

## Application API

### Rest
Single end point for registration of usage. It expects:
 - device_id
 - percentage_usage (integer of percentage)

### Export 
Per room csv document of usages. Document contains:
 - location name
 - device name
 - registration date
 - percentage use

API Filters:
 - start 
 - end

### Django admin
In django admin core data such as locations / devices / device types can be managed.

## Application database
Application will have four tables:

### Table DeviceType
This table contains the type of the device. This could be a lamp or a heather for example. The amount of kwh is stored here.
Fields:
 - name
 - kwh

### Table Device 
This table contains the location and the type of device.
Fields:
 - name
 - type (relation to DeviceType)
 - location (relation to Location)

### Table Location
This table contains the location name.
Fields:
 - name 

### Table Registration 
This table contains the percentage used of a device. 
Fields:
 - percentage_use (TinyInteger field)
 - device (relation to Device)
 - created (timestamp)