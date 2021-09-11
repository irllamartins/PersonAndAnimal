from sanic import Blueprint
from .device import DEVICES
from .body_presence import BODY_PRESENCE

ROUTES_API=Blueprint.group(DEVICES,BODY_PRESENCE)