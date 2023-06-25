# sysfs_hcsr04 modular sensor component

*sysfs_hcsr04* is a modular sensor component that provides distance readings from the HCSR04 ultrasonic sensor for boards that can use sysfs to interact with GPIO.

## Prerequisites

``` bash
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3
sudo apt install python3-pip
```

## API

The sysfs_hcsr04 resource fulfills the Viam sensor interface

### get_readings()

The *get_readings()* command takes no arguments, and returns the detected distance in meters.

## Viam Component Configuration

This component should be configured as type *sensor*, model *viamlabs:sensor:sysfs-hcsr04*.

The following attributes may be configured as sysfs_hcsr04 component config attributes.

Example:

``` json
{
  "trigger_pin": 32,
  "echo_pin": 30
}
```

### trigger_pin

*integer - required*

### echo_pin

*integer - required*

