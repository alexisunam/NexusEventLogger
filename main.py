from NexusLog.event_log import EventLog


from datetime import datetime, timezone, timedelta

# Generar mensajes de log con diferentes tipos de eventos y fechas
base_date = datetime(2023, 7, 9, 12, 0, 0, tzinfo=timezone.utc)
event_types = ['[CRITICAL]', '[INFO]', '[WARNING]', '[ERROR]']
messages_per_type = 10
log_messages = []

for i in range(messages_per_type * len(event_types) * 3):
    event_type = event_types[i % len(event_types)]
    event_date = base_date + timedelta(days=i // len(event_types))
    log_messages.append(f'{event_date.strftime("%Y-%m-%d %H:%M:%S.%f")} - {event_type}: Event {i + 1}')


if __name__ == '__main__':
    # Crear una instancia de EventLog
    event_log = EventLog()
    event_log.events = log_messages

    # Obtener todos los eventos
    print('All events:')
    for event in event_log.get_events():
        print(event)

    # Obtener eventos por fecha
    # date = '2023-07-11'
    # print(f'\nEvents on {date}:')
    # for event in event_log.get_events_by_date(date):
    #     print(event)

    # # Obtener eventos por tipo
    # event_type = 'INFO'
    # print(f'\n{event_type} events:')
    # for event in event_log.get_events_by_type(event_type):
    #     print(event)

    # # Obtener eventos por fecha y tipo
    # date = '2023-07-11'
    # event_type = 'ERROR'
    # print(f'\n{event_type} events on {date}:')
    # for event in event_log.get_events_by_date_and_type(date, event_type):
    #     print(event)


    # # Obtener eventor por rango de fecha
    # start_date = '2023-07-11'
    # end_date = '2023-07-13'
    # print(f'\nEvents between {start_date} and {end_date}:')
    # for event in event_log.get_events_by_date_range(start_date, end_date):
    #     print(event)

    # Obtener eventos por rango de fecha y tipo
    start_date = '2023-07-11'
    end_date = '2023-07-13'
    event_type = 'ERROR'
    print(f'\n{event_type} events between {start_date} and {end_date}:')
    for event in event_log.get_events_by_date_range_and_type(start_date, end_date, event_type):
        print(event)


