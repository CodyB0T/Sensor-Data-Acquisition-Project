import pyclariuscast

print(help(pyclariuscast))

NAME
    pyclariuscast

CLASSES
    Boost.Python.instance(builtins.object)
        Caster
        Imu

    class Caster(Boost.Python.instance)
     |  Class to wrap the Cast API.
     |
     |  Method resolution order:
     |      Caster
     |      Boost.Python.instance
     |      builtins.object
     |
     |  Static methods defined here:
     |
     |  __init__(...)
     |      __init__( (object)arg1, (object)arg2, (object)arg3, (object)arg4, (object)arg5, (object)arg6) -> None   
     |
     |  __reduce__ = <unnamed Boost.Python function>(...)
     |
     |  connect(...)
     |      connect( (Caster)arg1, (str)ipAddress, (int)portNumber, (str)certificate) -> bool :
     |          Makes a connection attempt to a scanner on the same Wi-Fi network
     |
     |  destroy(...)
     |      destroy( (Caster)arg1) -> bool :
     |          Destroys the cast library
     |
     |  disconnect(...)
     |      disconnect( (Caster)arg1) -> bool :
     |          Disconnects from an existing connection
     |
     |  enableParam(...)
     |      enableParam( (Caster)arg1, (str)prm, (bool)enable) -> bool :
     |          Enables or disables a level parameter
     |
     |  init(...)
     |      init( (Caster)arg1, (str)keysDir, (int)width, (int)height) -> bool :
     |          Initializes the cast library
     |
     |  isConnected(...)
     |      isConnected( (Caster)arg1) -> bool :
     |          Retrieves connected status of the caster
     |
     |  readRawData(...)
     |      readRawData( (Caster)arg1) -> object :
     |          Retrieves the raw data from a previous request, will be bundled as a compressed tar file
     |
     |  requestRawData(...)
     |      requestRawData( (Caster)arg1, (int)start, (int)end, (bool)lzo) -> int :
     |          Requests raw data from the device
     |
     |  separateOverlays(...)
     |      separateOverlays( (Caster)arg1, (bool)en) -> bool :
     |          Sets the flag to separate overlays into separate images
     |
     |  setFormat(...)
     |      setFormat( (Caster)arg1, (int)fmt) -> bool :
     |          Sets the image format
     |
     |  setOutputSize(...)
     |      setOutputSize( (Caster)arg1, (int)width, (int)height) -> bool :
     |          Sets the output size of the images
     |
     |  setParam(...)
     |      setParam( (Caster)arg1, (str)prm, (float)value) -> bool :
     |          Sets a low level parameter
     |
     |  setPulse(...)
     |      setPulse( (Caster)arg1, (str)prm, (str)shape) -> bool :
     |          Sets the pulse shape for a low level parameter
     |
     |  userFunction(...)
     |      userFunction( (Caster)arg1, (int)fn, (float)value) -> bool :
     |          Calls a user function to control parameters
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __instance_size__ = 112
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from Boost.Python.instance:
     |
     |  __new__(*args, **kwargs) from Boost.Python.class
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Boost.Python.instance:
     |
     |  __dict__
     |
     |  __weakref__

    class Imu(Boost.Python.instance)
     |  Method resolution order:
     |      Imu
     |      Boost.Python.instance
     |      builtins.object
     |
     |  Static methods defined here:
     |
     |  __init__(...)
     |      __init__( (object)arg1) -> None
     |
     |  __reduce__ = <unnamed Boost.Python function>(...)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  ax
     |      accelerometer x
     |
     |  ay
     |      accelerometer y
     |
     |  az
     |      accelerometer z
     |
     |  gx
     |      gyroscope x
     |
     |  gy
     |      gyroscope y
     |
     |  gz
     |      gyroscope z
     |
     |  mx
     |      magnetometer x
     |
     |  my
     |      magnetometer y
     |
     |  mz
     |      magnetometer z
     |
     |  qw
     |      quaternion w
     |
     |  qx
     |      quaternion x
     |
     |  qy
     |      quaternion y
     |
     |  qz
     |      quaternion z
     |
     |  tm
     |      timestamp
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __instance_size__ = 136
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from Boost.Python.instance:
     |
     |  __new__(*args, **kwargs) from Boost.Python.class
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Boost.Python.instance:
     |
     |  __dict__
     |
     |  __weakref__

FUNCTIONS
    version(...)
        version() -> str :
            Version of this library

