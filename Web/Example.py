from Web.WebAPI import WebAPI


class Example(WebAPI):

    @WebAPI.Catch
    def TestExample(self, url, implicit=10):
        self.Init(url, implicit)
        
        return str(0)
    




