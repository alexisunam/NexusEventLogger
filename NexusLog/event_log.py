import re
from datetime import datetime, timezone


class EventLog:
    _instance = None
    _types: list[str] = ["INFO", "WARNING", "ERROR", "CRITICAL"]
    _event_pattern: re.Pattern = re.compile(r'\[(INFO|WARNING|ERROR|CRITICAL)]')
    _date_pattern: re.Pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    _handler = None
    _is_file_output: bool = False
    _type_file_output: str = ""

    events: list[str] = []

    def __new__(cls, event_handler=None):
        if cls._instance is None:
            cls._instance = super(EventLog, cls).__new__(cls)
            cls._instance._handler = event_handler
        return cls._instance

    def add_info_event(self, event_message: str) -> None:
        self.create_type_event("INFO", event_message)

    def add_warning_event(self, event_message: str) -> None:
        self.create_type_event("WARNING", event_message)

    def add_error_event(self, event_message: str) -> None:
        self.create_type_event("ERROR", event_message)

    def add_critical_event(self, event_message: str) -> None:
        self.create_type_event("CRITICAL", event_message)

    def refresh_event_types(self, event_types: list[str]) -> None:
        for event_type in event_types:
            if event_type not in self._types:
                self._types.append(event_type.upper())
        # self._types = event_types
        self._event_pattern = re.compile(r'\[' + '|'.join(self._types) + ']')

    def create_type_event(self, event_type: str, event_message: str) -> None:
        time_stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
        self.events.append(f'{time_stamp} - [{event_type.upper()}]: {event_message}')
        self.refresh_event_types([event_type.upper()])
        print(f'{time_stamp} - [{event_type.upper()}]: {event_message}')

    def get_events(self) -> list[str]:
        return self.events

    def get_events_by_date(self, date: str) -> list[str]:
        # date_pattern: re.Pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        if not self._date_pattern.match(date):
            raise ValueError('Invalid date format. Date should be in the format "YYYY MM DD"')
        return [event for event in self.events if event.split(" ")[0] == date]

    def get_events_by_type(self, event_type: str):
        # event_pattern: re.Pattern = re.compile(r'\[(INFO|WARNING|ERROR|CRITICAL)]')

        print(f'Execution: {event_type}')
        event_type = '[' + event_type.upper() + ']:'
        if not self._event_pattern.match(event_type):
            raise ValueError('Invalid event type. Event type should be one of "INFO", "WARNING", "ERROR", "CRITICAL"')

        return [event for event in self.events if event.split(" ")[3] == event_type]

    def get_events_by_date_and_type(self, date: str, event_type: str) -> list[str]:
        # event_pattern: re.Pattern = re.compile(r'\[(INFO|WARNING|ERROR|CRITICAL)]')
        # date_pattern: re.Pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not self._date_pattern.match(date):
            raise ValueError('Invalid date format. Date should be in the format "YYYY MM DD"')

        event_type = '[' + event_type.upper() + ']:'

        if not self._event_pattern.match(event_type):
            raise ValueError('Invalid event type. Event type should be one of "INFO", "WARNING", "ERROR", "CRITICAL"')

        return [event for event in self.events if event.split(" ")[0] == date and event.split(" ")[3] == event_type]

    def get_events_by_date_range(self, start_date: str, end_date: str) -> list[str]:
        # date_pattern: re.Pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        if not self._date_pattern.match(start_date) or not self._date_pattern.match(end_date):
            raise ValueError('Invalid date format. Date should be in the format "YYYY MM DD"')

        return [event for event in self.events if datetime.strptime(start_date, '%Y-%m-%d')
                <= datetime.strptime(event.split(" ")[0], '%Y-%m-%d')
                <= datetime.strptime(end_date, '%Y-%m-%d')]

    def get_events_by_date_range_and_type(self, start_date: str, end_date: str, event_type: str) -> list[str]:
        # event_pattern: re.Pattern = re.compile(r'\[(INFO|WARNING|ERROR|CRITICAL)]')
        # date_pattern: re.Pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

        if not self._date_pattern.match(start_date) or not self._date_pattern.match(end_date):
            raise ValueError('Invalid date format. Date should be in the format "YYYY MM DD"')

        event_type = '[' + event_type.upper() + ']:'

        if not self._event_pattern.match(event_type):
            raise ValueError('Invalid event type. Event type should be one of "INFO", "WARNING", "ERROR", "CRITICAL"')

        return [event for event in self.events if datetime.strptime(start_date, '%Y-%m-%d')
                <= datetime.strptime(event.split(" ")[0], '%Y-%m-%d')
                <= datetime.strptime(end_date, '%Y-%m-%d') and event.split(" ")[3] == event_type]
