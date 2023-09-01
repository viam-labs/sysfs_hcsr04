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

from periphery import GPIO

LOGGER = getLogger(__name__)

class HCSR04(Sensor, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("viam-labs", "sensor"), "sysfs-hcsr04")
    
    trigger_pin: int
    echo_pin: int

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        trigger_pin = config.attributes.fields["trigger_pin"].number_value
        if trigger_pin == "":
            raise Exception("A trigger_pin must be defined")
        echo_pin = config.attributes.fields["echo_pin"].number_value
        if echo_pin == "":
            raise Exception("A echo_pin must be defined")
        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.trigger_pin = int(config.attributes.fields["trigger_pin"].number_value)
        self.echo_pin = int(config.attributes.fields["echo_pin"].number_value)
        # set both pins to low state
        echo = GPIO(self.echo_pin, "out")
        trigger = GPIO(self.trigger_pin, "out")
        echo.write(False)
        trigger.write(False)

        return

    """ Implement the methods the Viam RDK defines for the sensor API (rdk:component:sensor) """

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        trigger = GPIO(self.trigger_pin, "out")
        echo = GPIO(self.echo_pin, "in")

        trigger.write(True)
        time.sleep(.00001)
        trigger.write(False)

        while echo.read()==False:
            pulse_start = time.time()

        while echo.read()==True:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 171.5
        distance = round(distance, 2)

        trigger.close()
        echo.close()

        return {"distance": distance}
