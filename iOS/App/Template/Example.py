from iOS.App.Template.TemplateAPI import TemplateAPI
from MISC.UartAPI import UartAPI
import time


class Example(TemplateAPI, UartAPI):

    def __InitApp(self, caps, implicit):
        super().InitApp(caps, implicit)

    def __Login(self, account, password):
        super().Login(account, password)

    @UartAPI.Record  # for embedded system log record
    @TemplateAPI.Catch  # for exception return
    def TestExample(self, *args, **kwargs):
        ...
        ...
        ...
        print("it's a test script")
        return str(0)
