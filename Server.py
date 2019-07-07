import SimpleHTTPServer;
import SocketServer;
PORT = 8000; #指定服务器端口号
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler;
httpd = SocketServer.TCPServer(("", PORT), Handler);
httpd.serve_forever();
