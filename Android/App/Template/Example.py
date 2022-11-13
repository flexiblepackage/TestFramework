from Android.App.Template.TemplateAPI import TemplateAPI
from MISC.UartAPI import UartAPI
import time


class Example(TemplateAPI, UartAPI):

    def __InitApp(self, caps, implicit):
        return super().InitApp(caps, implicit)

    def __Login(self, account, password):
        return super().Login(account, password)

    def __Example(self, targetDUT, router, routerPW, **kwargs):
        err = self.ClickLabel("add_device")
        err = self.Quit()
        return err

    @UartAPI.Record
    @TemplateAPI.Except
    def Example(self, caps, implicit, targetDUT, router, routerPW, delay, *args, **kwargs):
        err = self.__InitApp(caps, implicit)
        # err = self.__Login(account, password)
        err = self.__Provision(targetDUT, router, routerPW, **kwargs)

        time.sleep(int(delay))
        return err

