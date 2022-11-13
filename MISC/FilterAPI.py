import re
import json
from MISC.ExceptAPI import ExceptAPI


class FilterAPI:

    def __WriteTemp(self, path, temp):
        with open(path, "w") as f:
            return f.write(temp)

    def __ReadFile(self, file):
        with open(file, "r") as f:
            return f.read()

    def __ReadPattern(self, ptrn):
        with open(ptrn, "r") as f:
            e = f.read().splitlines()
            return re.compile("|".join(e))

    def __ReadSearch(self, srch):
        with open(srch, "r") as f:
            return dict(json.load(f))

    @ExceptAPI.Catch
    def CompareLog(self, name: str, com: str, cycle: str, ptrn: str, srch: str):
        f = self.__ReadFile("./logs/"+name+" "+com +
                            " "+"CYCLE" + cycle + ".log")
        p = self.__ReadPattern("./logs/config/"+ptrn+".ini")
        s = self.__ReadSearch("./logs/config/"+srch+".json")

        t = re.sub(p, '', re.sub(p, '', f)).strip()
        self.__WriteTemp("./logs/config/ptrnTemp.log", t)

        r = dict()
        for i in s.keys():
            r[i] = str(len(re.findall(re.compile(i), t)))

        if s == r:
            print("CompareLog pass")
            return str(0)
        else:
            print("search\n"+str(s)+"\nuartlog\n"+str(r))
            return ("search\n"+str(s)+"\nuartlog\n"+str(r))
