from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, cast
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.sensor import Sensor
from viam.logging import getLogger

import time
import asyncio

import gpio as GPIO

LOGGER = getLogger(__name__)

class HCSR04(Sensor, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("viamlabs", "sensor"), "sysfs-hcsr04")
    
    trigger_pin: int
    echo_pin: int

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        LOGGER.warning("starting!")
        sensor = cls(HCSR04(config.name))
        sensor.reconfigure(config, dependencies)
        LOGGER.warning("initialized")
        return sensor

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        LOGGER.warning("validating")
        trigger_pin = config.attributes.fields["trigger_pin"].number_value
        if trigger_pin == "":
            raise Exception("A trigger_pin must be defined")
        echo_pin = config.attributes.fields["echo_pin"].number_value
        if echo_pin == "":
            raise Exception("A echo_pin must be defined")
        LOGGER.warning("validated")
        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        LOGGER.warning("reconfig")
        trigger_pin = config.attributes.fields["trigger_pin"].number_value
        echo_pin = config.attributes.fields["echo_pin"].number_value
        return

    """ Implement the methods the Viam RDK defines for the sensor API (rdk:component:sensor) """

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)

        GPIO.output(self.trigger_pin, False)
        time.sleep(.2)

        GPIO.output(self.trigger_pin, True)
        time.sleep(.00001)
        GPIO.output(self.trigger_pin, False)

        while GPIO.input(self.echo_pin)==0:
            pulse_start = time.time()

        while GPIO.input(self.echo_pin)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 171.5
        distance = round(distance, 2)

        GPIO.cleanup()

        return distance
