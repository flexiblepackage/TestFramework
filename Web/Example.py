from Web.WebAPI import WebAPI
from MISC.UartAPI import UartAPI


class Example(WebAPI, UartAPI):

    @UartAPI.Record  # for embedded system log record
    @WebAPI.Catch  # for exception return
    def TestExample(self, url, implicit, *args, **kwargs):
        self.Init(url, implicit)  # init web driver and testing page
        print("it's a test script")
        return str(0)
