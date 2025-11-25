from os import environ


class Config(object):
    database: "Database"
    api: "Api"

    def __init__(self) -> None:
        self.database = Database()
        self.api = Api()


class Database(object):
    url: str

    def __init__(self) -> None:
        DATABASE_URL = environ.get("DATABASE_URL")

        assert type(DATABASE_URL) is str, "DATABASE_URL is not set"

        self.url = DATABASE_URL


class Api(object):
    host: str
    port: int

    def __init__(self) -> None:
        API_HOST = environ.get("API_HOST")
        API_PORT = environ.get("API_PORT")

        if type(API_HOST) is not str:
            self.host = "127.0.0.1"
        else:
            self.host = API_HOST

        if type(API_PORT) is not str:
            self.port = 5000
        else:
            self.port = int(API_PORT)


config = Config()
