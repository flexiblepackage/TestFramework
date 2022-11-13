from selenium.common.exceptions import WebDriverException
import serial


class ExceptAPI:

    def Catch(func):
        def wrap(*args, **kwargs):
            try:
                f = func(*args, **kwargs)
            except serial.PortNotOpenError as e:
                print("PortNotOpenError " + str(e))
                return str("PortNotOpenError" + str(e))

            except serial.SerialTimeoutException as e:
                print("SerialTimeoutException " + str(e))
                return str("SerialTimeoutException" + str(e))

            except serial.SerialException as e:
                print("SerialException " + str(e))
                return str("SerialException" + str(e))

            except WebDriverException as e:
                print("WebDriverException" + str(e) + "\nargs\n" + str(args))
                return str("WebDriverException" + str(e) + "args" + str(args))

            except AttributeError as e:
                print("AttributeError " + str(e))
                return str("AttributeError " + str(e))

            except Exception as e:
                print("Exception " + str(e))
                return str("Exception " + str(e))
            return f
        return wrap
