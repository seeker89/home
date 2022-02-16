import http.server
import socketserver

class GithubPagesHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path[-1] != '/' and "." not in self.path:
            self.path += ".html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

my_server = socketserver.TCPServer(("", 8888), GithubPagesHandler)
my_server.serve_forever()
