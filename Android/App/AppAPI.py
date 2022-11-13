from Android.AndroidAPI import AndroidAPI
import time


class AppAPI(AndroidAPI):

    def Login(self, account, password):
        self.KeyLabel("login_email_input", account)
        self.KeyLabel("password_input", password)
        return self.ClickLabel("submit_button")


    def Deletion(self, target, **kwargs):
        self.ClickName("xxx")
        self.ClickLabel("xxx")
        self.ClickLabel(target)    
        ...
        ...
        return self.ClickValue("delete")
