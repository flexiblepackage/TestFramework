from http.server import BaseHTTPRequestHandler
import robot


class store():
    def __init__(self):
        self.value = ""


result = store()


class listen():

    ROBOT_LISTENER_API_VERSION = 2

    def end_test(self, name, attrs):
        result.value = str.format("{}\n{}\n{}\n{}\n{}",
                                  "This is a example which execute web.robot and shows result",
                                  "StartTime: "+attrs['starttime'],
                                  "TestCase: "+name,
                                  "Result: " + attrs['status'],
                                  "EndTime: "+attrs['endtime']
                                  )


class handler(BaseHTTPRequestHandler):  

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        robot.run("./RobotExample/TestCase/web.robot", listener=listen(), pythonpath='./',
                  output='NONE', report='NONE', log='NONE')

        self.wfile.write(result.value.encode())



