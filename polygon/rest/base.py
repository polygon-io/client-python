import os
import json
import urllib3
import inspect
from enum import Enum
from typing import Optional, Any, Dict
from datetime import datetime

base = "https://api.polygon.io"
env_key = "POLYGON_API_KEY"


class BaseClient:
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(env_key),
        connect_timeout: float = 10.0,
        read_timeout: float = 10.0,
        num_pools: int = 10,
        retries=3,
        base: str = base,
        verbose: bool = False,
    ):
        if api_key is None:
            raise Exception(
                f"Must specify env var {env_key} or pass api_key in constructor"
            )
        self.API_KEY = api_key
        self.BASE = base

        # https://urllib3.readthedocs.io/en/stable/reference/urllib3.poolmanager.html
        # https://urllib3.readthedocs.io/en/stable/reference/urllib3.connectionpool.html#urllib3.HTTPConnectionPool
        self.client = urllib3.PoolManager(
            num_pools=num_pools,
            headers={
                "Authorization": "Bearer " + self.API_KEY,
                "User-Agent": "Python client",
            },
        )
        self.timeout = urllib3.Timeout(connect=connect_timeout, read=read_timeout)
        self.retries = retries
        self.verbose = verbose

    def _decode(self, resp):
        return json.loads(resp.data.decode("utf-8"))

    def _get(
        self,
        path: str,
        params: Optional[dict] = None,
        result_key: Optional[str] = None,
        deserializer=None,
        raw: bool = False,
    ) -> Any:
        if params is None:
            params = {}
        params = {str(k): str(v) for k, v in params.items() if v is not None}
        if self.verbose:
            print("_get", path, params)
        resp = self.client.request(
            "GET", self.BASE + path, fields=params, retries=self.retries
        )

        if resp.status != 200:
            raise Exception(resp.data.decode("utf-8"))

        if raw:
            return resp

        obj = self._decode(resp)

        if result_key:
            obj = obj[result_key]

        # If obj is not yet a list, need to turn it into a list
        # This is for the Daily Open/Close and Last Trade endpoints
        if type(obj) != list:
            obj = [obj]

        if deserializer:
            obj = [deserializer(o) for o in obj]

        return obj

    @staticmethod
    def time_mult(timestamp_res: str) -> int:
        if timestamp_res == "nanos":
            return 1000000000
        elif timestamp_res == "micros":
            return 1000000
        elif timestamp_res == "millis":
            return 1000

        return 1

    def _get_params(
        self, fn, caller_locals: Dict[str, Any], datetime_res: str = "nanos"
    ):
        params = caller_locals["params"]
        if params is None:
            params = {}
        # https://docs.python.org/3.7/library/inspect.html#inspect.Signature
        for argname, v in inspect.signature(fn).parameters.items():
            # https://docs.python.org/3.7/library/inspect.html#inspect.Parameter
            if argname in ["params", "raw"]:
                continue
            if v.default != v.empty:
                # timestamp_lt -> timestamp.lt
                val = caller_locals.get(argname, v.default)
                if isinstance(val, Enum):
                    val = val.value
                elif isinstance(val, datetime):
                    val = int(val.timestamp() * self.time_mult(datetime_res))
                if val is not None:
                    params[argname.replace("_", ".")] = val

        return params

    def _paginate_iter(
        self,
        path: str,
        params: dict,
        raw: bool,
        deserializer,
        result_key: str = "results",
    ):
        while True:
            resp = self._get(
                path=path,
                params=params,
                deserializer=deserializer,
                result_key=result_key,
                raw=True,
            )
            decoded = self._decode(resp)
            for t in decoded[result_key]:
                yield deserializer(t)
            if "next_url" in decoded:
                path = decoded["next_url"].replace(self.BASE, "")
                params = {}
            else:
                return

    def _paginate(
        self,
        path: str,
        params: dict,
        raw: bool,
        deserializer,
        result_key: str = "results",
    ):
        if raw:
            return self._get(
                path=path, params=params, deserializer=deserializer, raw=True
            )

        return self._paginate_iter(
            path=path,
            params=params,
            deserializer=deserializer,
            result_key=result_key,
            raw=True,
        )
