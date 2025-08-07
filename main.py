from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8080


class Myserver(BaseHTTPRequestHandler):
    """ Класс обрабатывает методы GET и POST HTTP сервера """

    def do_GET(self):
        """ Метод GET - получение данных с HTTP сервера """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("contact.html", mode="r", encoding="utf-8") as file:
            data = file.read()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        """ Метод POST - посылка данных на HTTP Сервер """
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        result = body.decode("utf-8")
        print(result)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    """ Основная программа - запуск HTTP Сервера """

    webserver = HTTPServer((host, port), Myserver)
    print("Веб сервер запущен http://%s:%s" % (host, port))
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Веб сервер остановлен")
