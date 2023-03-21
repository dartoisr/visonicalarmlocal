import requests
import json
import datetime
import socket
from visonicalarmlocal.exceptions import *
from visonicalarmlocal.devices import *


class API(object):
    """ Class used for communication with the Visonic API """
    __url = None
    
    def __init__(self, url):

        # Set connection specific details
        self.__url = url
        
        # Create a new session
        self.__session = requests.session()

    def __send_request(self, method, params):
        # Prepare the payload to be sent
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": 1,
        }
        
        # Perform the request and raise an exception
        # if the response is not OK (HTML 200)
        try:
            response = self.__session.post(self.__url, json=payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise HTTPError(err)
            
        # Check HTTP response code
        if response.status_code == requests.codes.ok:
            resp = json.loads(response.content.decode('utf-8'))
            # Check response status
            if "error" in resp:
                raise RequestError(resp['error']['message'] + "(code : " + str(resp['error']['code']) + ")")
            else:
                return resp
        else:
            return None

    def register(self, user, code):
        ip_address = socket.gethostbyname(socket.gethostname())
        self.__send_request("PmaxService/registerClient", [ip_address, code, user])

    def is_authorized(self):
        start = (datetime.datetime.now() - datetime.timedelta(minutes=1)).strftime("%Y%m%d%H%M%S")
        end = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        authorized = True
        try:
            self.__send_request("PmaxService/getLogHistory", [start, end])
        except:
            authorized = False
        return authorized
        
    def get_panel_statuses(self):
        return self.__send_request("PmaxService/getPanelStatuses", None)["result"]
    
    def get_panel_state(self, partition_id):
        return self.__send_request("PmaxService/getPanelState", [partition_id])["result"]
    
    def get_devices_config(self):
        devices = []
        result_devices = self.__send_request("PmaxService/getDevicesConfig", None)["result"]
        for device in result_devices:
            if device["type"] == 3 and device["subtype"] == 4:
                motionDetectorWithCameraDevice = MotionDetectorWithCameraDevice(device["id"], device["partitions"], device["type"], device["location"], device["serial"], device["subtype"], device["zoneSecurityType"], device["viewOnDemand"])
                devices.append(motionDetectorWithCameraDevice)
            elif device["type"] == 3 and device["subtype"] == 30:
                smokeDevice = SmokeDevice(device["id"], device["partitions"], device["type"], device["location"], device["serial"], device["subtype"], device["zoneSecurityType"])
                devices.append(smokeDevice)
            elif device["type"] == 3 and device["subtype"] == 15:
                curtainDetectorDevice = CurtainDetectorDevice(device["id"], device["partitions"], device["type"], device["location"], device["serial"], device["subtype"], device["zoneSecurityType"])
                devices.append(curtainDetectorDevice)
            elif device["type"] == 3 and device["subtype"] == 42:
                doorConcatDevice = DoorContactDevice(device["id"], device["partitions"], device["type"], device["location"], device["serial"], device["subtype"], device["zoneSecurityType"])
                devices.append(doorConcatDevice)
            
        return devices

            
    
    