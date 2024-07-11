from datetime import datetime, timezone


class NexusEvent:
    _instance = None
    _event_type: str = None
    _event_message: str = None
    _event_date: str = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
    # def __init__(self, event_type: str = "Normal", event_message: str = "No message"):
    #     self.event_type = event_type
    #     self.eventDate = datetime.now(timezone.utc)
    #     self.event_data = event_data

    def __new__(cls, event_type: str = "Normal", event_message: str = "No message"):
        if cls._instance is None:
            cls._instance = super(NexusEvent, cls).__new__(cls)
            cls._instance._event_type = event_type
            cls._instance._event_message = event_message
            cls._instance._event_date = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')

    def __str__(self):
        return f"[{self._event_type}]: {self._event_date} - {self._event_message}"

    def get_all_date(self):
        return self._event_date

    def get_date(self):
        return self._event_date.split(" ")[0]

    def get_time(self):
        return self._event_date.split(" ")[1]

    def get_event_type(self):
        return self._event_type
