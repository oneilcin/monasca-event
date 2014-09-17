import json
import time


class OpenstackEvent:
    # required fields
    REQUEST_ID = '_context_request_id'
    EVENT_TYPE = 'event_type'
    EVENT_TIMESTAMP = 'timestamp'
    # meta fields we care about
    # NOTE: payload fields are the wild west, not required.
    PAYLOAD = 'payload'   
    TENANT_ID = '_context_tenant'
    REGION = 'availability_zone'


class Event:
       
    def fromFields(self, type, id, timestamp, **dim_kwargs):
        self.type = type
        self.id = id
        self.timestamp = timestamp
        self.dimensions = {}
        self.dimensions = dim_kwargs

    def fromOpenstackEvent(self, json_message):
        self.type = json_message[OpenstackEvent.EVENT_TYPE]
        self.id = json_message[OpenstackEvent.REQUEST_ID] 
        self.timestamp = json_message[OpenstackEvent.EVENT_TIMESTAMP]
        # i've left the type, id , timestamp in the dimensions, i could delete them out.
        self.dimensions = {}
        self.dimensions = json_message

    def as_json(self):
        return json.dumps(self.__dict__)

    def as_dict(self):
        return self.__dict__


class EventEnvelope:

    def __init__(self, event, creation_time, **meta_kwargs):
        self.event = {}
        self.event = event.as_dict()
        self.meta = {}
        self.meta = meta_kwargs
        # creation_time is a long
        self.creation_time = creation_time

    def as_json(self):
        return json.dumps(self.__dict__)