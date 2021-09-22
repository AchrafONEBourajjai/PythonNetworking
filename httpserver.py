from BaseHTTPServer import BaseHTTPServerRequestHandler,HTTPServer
#just change version of python to 2.7
HOST='127.0.0.1'
PORT='6000'
class RequestHandler(BaseHTTPServerRequestHandle): #to write into web page and send header of http
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("hello i'm python web server")#write file
class CHTTPserver(HTTPServer): #to use your customise host and port
    def __init__(self,host,port):
        server_addrs = (host,port)
        HTTPServer.__init__(self,server_addrs,RequestHandler)
def run_server(port):
    try:
        server = CHTTPserver(HOST,port)
        print('listening at %s on port %s'%(HOST,PORT))
        server.serve_forever()
        server.socket.close()
    except Exception as err:
        print ("Error: %s"%err)
    except KeyboardInterrupt:
        print ("Server is shutting down...")
        server.socket.close()
run_server(7000)