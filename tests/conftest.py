import pytest
from fastapi.testclient import TestClient

from src.social_links_service.create_app import create_app
from src.social_links_service.db import create_tables

app = create_app()


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c
