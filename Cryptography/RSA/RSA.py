import socketserver
import rsa
import logging

class RSASocket(socketserver.BaseRequestHandler):

    def setup(self):
        self.publicKey, self.privateKey = rsa.newkeys(512)
        self.flag = b'BTU{I_AM_A_TEST}'
        self.c = rsa.encrypt(self.flag, self.publicKey).hex()

        self.logger = logging.getLogger('RSASocketServer')
        self.logger.info(f'Connection from {self.client_address} received: {self.publicKey}, {self.privateKey}')

    def handle(self) -> None:
        self.data = bytes(f'N: {self.publicKey.n}\ne: {self.publicKey.e}\nq: {self.privateKey.q}\nFlag: {self.c}\n', 'UTF-8')
        self.request.sendall(self.data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    HOST, PORT = "0.0.0.0", 3434

    with socketserver.TCPServer((HOST, PORT), RSASocket) as server:
        server.serve_forever()
