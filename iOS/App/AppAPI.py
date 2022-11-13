from iOS.iOSAPI import iOSAPI
import time


class AppAPI(iOSAPI):

    def Login(self, account, password):
        self.KeyLabel("login_email_input", account)
        self.KeyLabel("password_input", password)
        self.ClickLabel("submit_button")


    def Deletion(self, target, **kwargs):
        self.ClickName("xxx")
        self.ClickLabel("xxx")
        self.ClickLabel(target)    
        ...
        ...
        self.ClickValue("delete")
