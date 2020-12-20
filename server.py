import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
from html_body import html_body
from dictionary import dictionary
import random
import json
import webbrowser

def make_html():
    item = random.choice(dictionary)
    item = item.replace('\n', '\\n').replace('■', '')
    item = json.loads(item)
    item = html_body.format(item[0], item[1], item[5][0].replace('\n','<br>'))
    item = item.replace('%%', '{').replace('&&', '}')
    return item
    

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        name = 'ThisJapaneseWordDoesNotExist'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components["name"][0]
        html = make_html()
        self.wfile.write(bytes(html, "utf8"))
        return


handler_object = MyHttpRequestHandler
PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)
webbrowser.open('http://127.0.0.1:' + str(PORT))
my_server.serve_forever()