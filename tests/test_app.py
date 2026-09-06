from app import create_app


def test_home_page():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_api_status():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json["status"] == "running"