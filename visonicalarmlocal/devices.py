class Device(object):
    """ Base class definition of a device in the alarm system. """

    # Property variables
    __id = None
    __partitions = None
    __type = None
    __location = None
    __serial = None
    __subtype = None
    __zoneSecurityType = None


    def __init__(self, id, partitions, type, location, serial, subtype, zoneSecurityType):
        """ Set the private variable values on instantiation. """

        self.__id = id
        self.__partitions = partitions
        self.__type = type
        self.__location = location
        self.__serial = serial
        self.__subtype = subtype
        self.__zoneSecurityType = zoneSecurityType

    def __str__(self):
        """ Define how the print() method should print the object. """
        object_type = type(self).__name__
        return object_type + ": " + str(self.as_dict()) 
    
    def __repr__(self):
        """ Define how the object is represented when output to console. """

        class_name          = self.__class__.__name__
        id                  = f"id = '{self.id}'"
        partitions          = f"partitions = '{self.partitions}'"
        type            = f"type = {self.type}"
        location            = f"location = {self.location}"
        serial            = f"serial = {self.serial}"
        subtype            = f"subtype = {self.subtype}"
        zoneSecurityType            = f"zoneSecurityType = {self.zoneSecurityType}"

        return f"{class_name}({id}, {partitions}, {type}, {location}, {serial}, {subtype}, {zoneSecurityType})"

    def as_dict(self):
        """ Return the object properties in a dictionary. """
        return {
            'id': self.id,
            'partitions': self.partitions,
            'type': self.type,
            'location': self.location,
            'serial': self.serial,
            'subtype': self.subtype,
            'zoneSecurityType': self.zoneSecurityType
        }

    # Device properties

    @property
    def id(self):
        return self.__id

    @property
    def partitions(self):
        return self.__partitions

    @property
    def type(self):
        return self.__type
    
    @property
    def location(self):
        return self.__location
    
    @property
    def serial(self):
        return self.__serial
    
    @property
    def subtype(self):
        return self.__subtype
    
    @property
    def zoneSecurityType(self):
        return self.__zoneSecurityType
    
class CurtainDetectorDevice(Device):
    """ Curtain detector device class definition. """
    """ Type = 3 """
    """ Subtype = 15 """

    def __init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType):
        Device.__init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType)

    def __str__(self):
        """ Define how the print() method should print the object. """

        object_type = type(self).__name__
        value_dict = self.as_dict()
        return object_type + ": " + str(value_dict)   
    
class DoorContactDevice(Device):
    """ Door/Window contact device class definition. """
    """ Type = 3 """
    """ Subtype = 42 """

    def __init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType):
        Device.__init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType)

    def __str__(self):
        """ Define how the print() method should print the object. """

        object_type = type(self).__name__
        value_dict = self.as_dict()
        return object_type + ": " + str(value_dict)   
    
class SmokeDevice(Device):
    """ Smoke device class definition. """
    """ Type = 3 """
    """ Subtype = 30 """

    def __init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType):
        Device.__init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType)

    def __str__(self):
        """ Define how the print() method should print the object. """

        object_type = type(self).__name__
        value_dict = self.as_dict()
        return object_type + ": " + str(value_dict)
    

class MotionDetectorWithCameraDevice(Device):
    """ Smoke device class definition. """
    """ Type = 3 """
    """ Subtype = 4 """
    __viewOnDemand = None

    def __init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType, viewOnDemand):
        Device.__init__(self, id, partitions, type, location, serial,
                 subtype, zoneSecurityType)
        self.__viewOnDemand = viewOnDemand

    def __str__(self):
        """ Define how the print() method should print the object. """

        object_type = type(self).__name__
        value_dict = self.as_dict()
        value_dict['viewOnDemand'] = self.__viewOnDemand
        return object_type + ": " + str(value_dict)
    
    @property
    def viewOnDemand(self):
        return self.__viewOnDemand
    