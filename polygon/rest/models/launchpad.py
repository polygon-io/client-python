from typing import Optional

from polygon.modelclass import modelclass


@modelclass
class EdgeHeaders:
    def __init__(
        self,
        edge_id: Optional[str] = None,
        edge_user: Optional[str] = None,
        edge_ip_address: Optional[str] = None,
    ):
        self.EDGE_ID_KEY = "X-Polygon-Edge-ID"
        self.EDGE_USER_KEY = "X-Polygon-Edge-IP-Address"
        self.EDGE_IP_ADDRESS_KEY = "X-Polygon-Edge-User-Agent"

        self.EDGE_ID = edge_id
        self.EDGE_USER = edge_user
        self.EDGE_IP_ADDRESS = edge_ip_address

    def __dict__(self):
        d = {}

        if self.EDGE_ID is not None:
            d.__setitem__(self.EDGE_ID_KEY, self.EDGE_ID)
        if self.EDGE_USER is not None:
            d.__setitem__(self.EDGE_USER_KEY, self.EDGE_USER)
        if self.EDGE_IP_ADDRESS is not None:
            d.__setitem__(self.EDGE_IP_ADDRESS_KEY, self.EDGE_IP_ADDRESS)

        return d
