

class LoggBook:
    _instance = None
    event_types: list[str] = ["INFO", "IMPORTANT", "BD", "USER", "API", "SYSTEM", "SECURITY"]
    events = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggBook, cls).__new__(cls)
        return cls._instance

    def add_entry(self, entry):
        self.events.append(entry)

    def get_entries(self):
        return self.events

    def get_entry_count(self):
        return len(self.events)
