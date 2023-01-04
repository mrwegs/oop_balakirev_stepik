class Data:
    def __init__(self, text: str, ip: int):
        self.data = text
        self.ip = ip


class Server:
    IP = 1

    def __init__(self):
        self.ip = self.IP
        self.__class__.IP += 1
        self.buffer: list = list()

    @staticmethod
    def send_data(data: Data):
        router = Router()
        router.buffer.append(data)

    def get_data(self):
        temp = self.buffer.copy()
        self.buffer.clear()
        return temp

    def get_ip(self):
        return self.ip


class Router:
    __instance = None
    arp_table = dict()
    buffer = list()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    @classmethod
    def link(cls, server: Server):
        cls.arp_table[server.ip] = server

    @classmethod
    def unlink(cls, server: Server):
        del cls.arp_table[server.ip]

    @classmethod
    def send_data(cls):
        while cls.buffer:
            data = cls.buffer.pop()
            if data.ip in cls.arp_table:
                server = cls.arp_table[data.ip]
                server.buffer.append(data)


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()