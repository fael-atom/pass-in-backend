import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
  event = {
    "uuid": "Este é o uuid5",
    "title": "Evento de teste",
    "details": "Este é um evento testado por Pytest",
    "slug": "event-test",
    "maximumm_attendees": 20 
  }
  events_repository = EventsRepository()
  response = events_repository.insert_event(event)
  print(response)
  
def test_get_event_by_id():
  event_id = "Este é o uuid5"
  events_repository = EventsRepository()
  response = events_repository.get_event_by_id(event_id)
  print(response)