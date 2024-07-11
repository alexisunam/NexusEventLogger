from abc import ABC, abstractmethod


class FileEventHandler(ABC):

    def __init__(self):
        self._is_file_output = False
        self._is_event_type_for_file = False
        self._type_file = ""
        self._file_path = ""
        self._dir_name = ""
        self._file_extension = ""

    @abstractmethod
    def get_events(self):
        pass

    @abstractmethod
    def get_events_by_date(self, date: str) -> list[str]:
        pass

    @abstractmethod
    def get_events_by_type(self, event_type: str):
        pass

    @abstractmethod
    def get_events_by_date_and_type(self, date: str, event_type: str) -> list[str]:
        pass

    @abstractmethod
    def get_events_by_date_range(self, start_date: str, end_date: str) -> list[str]:
        pass

    @abstractmethod
    def get_events_by_date_range_and_type(self, start_date: str, end_date: str, event_type: str) -> list[str]:
        pass
