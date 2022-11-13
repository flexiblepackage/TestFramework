from iOS.App.Template.TemplateAPI import TemplateAPI
from MISC.UartAPI import UartAPI
import time


class Example(TemplateAPI, UartAPI):

    def __InitApp(self, caps, implicit):
        super().InitApp(caps, implicit)

    def __Login(self, account, password):
        super().Login(account, password)


    # @UartAPI.Record #for embedded system log record
    @TemplateAPI.Catch
    def TestExample(self, caps, implicit, targetDUT, router, routerPW, delay, *args, **kwargs):
        self.__InitApp(caps, implicit)
        self.__Login(targetDUT, router, routerPW, **kwargs)

        time.sleep(int(delay))
        return str(0)

