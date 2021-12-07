import socket
from do import do
import urllib.parse

hostName = socket.gethostname()
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.strip("/").split("/")
        if path[0] == "":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("index.html", "r") as f:
                self.wfile.write(bytes(f.read(), "utf-8"))

        elif path[0] == "break":
            print("Yay")

            md5hash = urllib.parse.unquote(path[1])
            num_workers = int(path[2])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            do(md5hash,num_workers)

if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
