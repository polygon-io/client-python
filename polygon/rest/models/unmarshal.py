from typing import Type

from polygon.rest import models


def unmarshal_json(response_type, resp_json) -> Type[models.AnyDefinition]:
    obj = models.name_to_class[response_type]()
    obj.unmarshal_json(resp_json)
    return obj
