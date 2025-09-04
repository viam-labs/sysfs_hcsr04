# `sysfs_hcsr04` modular sensor component

This module implements the [Viam sensor API](https://docs.viam.com/dev/reference/apis/components/sensor/) in a `viamlabs:sensor:sysfs-hcsr04` model.
With this model, you can gather distance readings from the HCSR04 ultrasonic sensor for boards that can use `sysfs` to interact with GPIO.

Navigate to the **CONFIGURE** tab of your machine's page.
Click the **+** button, select **Component or service**, then select the `sensor / sysfs-hcsr04` model provided by the [`sysfs_hcsr04` module](https://app.viam.com/module/viamlabs/sysfs_hcsr04).
Click **Add module**, enter a name for your sensor, and click **Create**.

## Configure your `sysfs_hcsr04` sensor

On the new component panel, copy and paste the following attribute template into your sensor's **Attributes** box:

```json
{
  "trigger_pin": <integer>,
  "echo_pin": <integer>
}
```

### Attributes

The following attributes are available for `viamlabs:sensor:sysfs-hcsr04` sensors:

| Name           | Type    | Inclusion | Description                    |
| -------------- | ------- | --------- | ------------------------------ |
| `trigger_pin`  | integer | **Required**  | GPIO pin number for trigger     |
| `echo_pin`     | integer | **Required**  | GPIO pin number for echo        |

### Example Configuration

```json
{
  "trigger_pin": 32,
  "echo_pin": 30
}
```

## Prerequisites

```bash
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3
sudo apt install python3-pip
```

## API

The sysfs_hcsr04 resource fulfills the Viam sensor interface.

### get_readings()

The `get_readings()` command takes no arguments, and returns the detected distance in meters (with the key 'distance').

