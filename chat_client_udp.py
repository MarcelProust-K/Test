import threading
import socket


class SendMsg(threading.Thread):

    def __init__(self, udp_socket):
        super(SendMsg, self).__init__()
        self.udp_socket = udp_socket
    
    def run(self):
        while True:
            msg = input("请输入要发送的内容:")
            ip_addr = input("请输入对方ip:")
            ip_port = input("请输入对方port:")
            self.udp_socket.sendto(msg.encode("utf-8"), (ip_addr, ip_port))


class RecvMsg(threading.Thread):

    def __init__(self, udp_socket):
        super(RecvMsg, self).__init__()
        self.udp_socket = udp_socket

    def run(self):
        while True:
            recv_data = self.udp_socket.recvfrom(1024)
            print("接收到的消息:%s" %recv_data[0].decode("utf-8"))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ("", 8989)
    udp_socket.bind(local_addr)

    # while True:
    #     send_thread = threading.Thread(target=send_msg, args=(udp_socket,))
    #     recv_thread = threading.Thread(target=recv_msg, args=(udp_socket,))

    send_msg = SendMsg(udp_socket)
    recv_msg = RecvMsg(udp_socket)
    send_msg.start()
    recv_msg.start()


if __name__ == "__main__":
    main()