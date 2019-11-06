from polygon.rest import models


def unmarshal_json(response_type, resp_json) -> models.Definition:
    obj = models.name_to_class[response_type]()
    obj.unmarshal_json(resp_json)
    return obj
