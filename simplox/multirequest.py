import requests
from protobuf_delim import delimited
import simplox_pb2
from functools import partial
import sys
import logging
from time import time

log = logging.getLogger(__name__)

CONTENT_TYPE = "application/protobuf+vnd.simplox.multirequest"
ACCEPT = "application/protobuf+delimited+vnd.simplox.response"


def multirequest(*requests):
    msg = simplox_pb2.MultiRequest()
    msg.requests.extend(requests)
    return msg


def request(method, url, headers=None, content_type=None, body=None, key=None):
    msg = simplox_pb2.Request()
    msg.method = method
    msg.url = url

    maybe_setattr(msg, "content_type", content_type)
    maybe_setattr(msg, "body", body)
    maybe_setattr(msg, "key", key)

    return msg


head = partial(request, "head")
get = partial(request, "get")
put = partial(request, "put")
post = partial(request, "post")
delete = partial(request, "delete")


def maybe(val, f):
    if val is not None:
        return f(val)


def default(val, f):
    if val is not None:
        return val
    else:
        return f()


def maybe_setattr(obj, key, val):
    return maybe(val, lambda _: setattr(obj, key, val))


def header(key, value):
    msg = simplox_pb2.Header()
    msg.key = key
    msg.value = value
    return msg


class MultiRequestError(Exception):
    def __init__(self, resp):
        super(MultiRequestError, self).__init__(
            "Error executing multirequest: {0} {1}".format(
                resp.status_code,
                resp.content))


def fetch(endpoint, mr):
    resp = requests.post(
        endpoint, data=mr.SerializeToString(),
        stream=True,
        headers={"content-type": CONTENT_TYPE,
                 "accept": ACCEPT})

    if resp.status_code != 200:
        raise MultiRequestError(resp)
    
    start = time()
    for packet in delimited(resp.raw):
        msg = simplox_pb2.Response()
        msg.ParseFromString(packet)

        elapsed = (time() - start) * 1000.0
        start = time()
        sync_time = msg.request_time / 1000.0
        diff = sync_time - elapsed

        log.debug("{0} {sync_time:.2f} - {elapsed:.2f} = {diff:.2f}".format(msg.url, **locals()))
        yield msg


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    endpoint = sys.argv[1]
    urls = sys.argv[2:]
    mr = multirequest(*map(get, urls))

    start = time()
    for data in fetch(endpoint, mr):
        pass

