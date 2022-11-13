import re
import time
import serial
from threading import Thread
from datetime import datetime
from MISC.ExceptAPI import ExceptAPI


class UartAPI:

    def __Threaded(func):
        def wrap(*args, **kwargs):
            thread = Thread(target=func, args=args, kwargs=kwargs)
            thread.start()
            return thread
        return wrap

    @__Threaded
    @ExceptAPI.Catch
    def __Open(self, com):
        patterns = ["[\u001b\u0007]", "\[\d;\d\dm",
                    "\[\d;\d\d;\d\dm", "\[m", "x1b"]
        rp = re.compile("|".join(patterns))

        sp = serial.Serial(com, 115200)
        strBuild = []
        self._udt[com] = (sp, strBuild)

        strBuild.append(str.format(
            "{} {}",
            datetime.now().strftime(
                "[%Y-%m-%d %H:%M:%S.%f")[:-3] + "]",
            "**********"+com+" OPEN**********\n"))
        print(strBuild[0])

        while True:
            try:
                if sp.in_waiting > 0:
                    buf = re.sub(rp, "", str(
                        sp.readline().decode("utf-8", "ignore").strip()))
                    log = str.format(
                        "{} {}",
                        datetime.now().strftime(
                            "[%Y-%m-%d %H:%M:%S.%f")[:-3] + "]",
                        buf + "\n",
                    )
                    strBuild.append(log)
                    print(log)
            except (serial.SerialException):
                print(str.format(
                    "{} {}",
                    datetime.now().strftime(
                        "[%Y-%m-%d %H:%M:%S.%f")[:-3] + "]",
                    "**********"+com+" CLOSE**********\n"))
                break

    @ExceptAPI.Catch
    def __Close(self, com, **kwargs):
        if "NAME" in list(kwargs.keys()):
            name = str(kwargs["NAME"])
        else:
            name = "Default"

        if "CYCLE" in list(kwargs.keys()):
            cycle = str(kwargs["CYCLE"])
        else:
            cycle = "0"

        sp = self._udt[com][0]
        strBuild = self._udt[com][1]
        sp.close()
        strBuild.append(str.format(
                        "{} {}",
                        datetime.now().strftime(
                            "[%Y-%m-%d %H:%M:%S.%f")[:-3] + "]",
                        "**********"+com+" CLOSE**********\n"))
        with open("./logs/" + name + " "+com + " CYCLE" + cycle + ".log", "w") as f:
            f.write("".join(strBuild))

    @ExceptAPI.Catch
    def UartWrite(self, cmd, *args):
        for com in args:
            if isinstance(com, str) and com.startswith("COM") | com.startswith("/dev/tty.usbserial-"):
                sp = self._udt[com][0]
                for i in list(cmd):
                    sp.write(i.encode())
                    # DON'T remove this line, or long cmd may loss bytes.
                    time.sleep(1/1000)
                sp.write(("\n").encode())

    @ExceptAPI.Catch
    def UartSearch(self, *args):
        log = []
        for com in args:
            if isinstance(com, str) and com.startswith("COM") | com.startswith("/dev/tty.usbserial-"):
                log.append(''.join(self._udt[com][1]))
        return log

    def __Record(self, func, *args):
        # self.sp = [serial.Serial for i in range(len(args))]
        # self.strBuild = [[] for i in range(len(args))]
        pass

    def Record(func):
        def warp(self, *args, **kwargs):
            self._udt = dict()
            for com in args:
                if isinstance(com, str) and com.startswith("COM") | com.startswith("/dev/tty.usbserial-"):
                    self.__Open(com)
                    time.sleep(1)
            err = func(self, *args, **kwargs)
            for com in args:
                if isinstance(com, str) and com.startswith("COM") | com.startswith("/dev/tty.usbserial-"):
                    self.__Close(com, **kwargs)
            return err
        return warp

    # @Record
    # @ExceptAPI.Catch
    # def dogbark(self, *args, **kwargs):
    #     print(args)
    #     print("start")
    #     # self.UartWrite("Hello?????", 1, *args)
    #     # self.UartWrite("paswd tkbfTrefzFBnqgD5HIODecH5SBMwiUNJ",*args)
    #     self.UartWrite("nvram show usr", *args)
    #     time.sleep(3)
    #     log = self.UartSearch(*args)
    #     if(re.search(r"NvmVersion", log[0])):
    #         time.sleep(1)
    #     time.sleep(10)
    #     print(args)
    #     print("End")
    #     return -1
