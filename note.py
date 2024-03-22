from datetime import datetime


class Note:

    __header: str
    __text: str
    __created_at: datetime = datetime.now()
    __updated_at: datetime | None = None

    def get_header(self):
        return self.__header

    def set_header(self, new_header: str):
        self.__header = new_header

    def get_text(self):
        return self.__text

    def set_text(self, new_text: str):
        self.__text = new_text

    def get_created_at(self):
        return self.__created_at

    def set_created_at(self, created_at: datetime):
        self.__created_at = created_at

    def get_updated_at(self):
        return self.__updated_at

    def set_updated_at(self, update_at: datetime):
        self.__updated_at = update_at


