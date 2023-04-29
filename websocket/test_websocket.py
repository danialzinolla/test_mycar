import pytest
import websocket


@pytest.fixture(scope="module")
def ws():
    ws = websocket.create_connection("wss://api.notification.sandbox.mycarpro.net/ws/notifications/")
    yield ws
    ws.close()


def test_websocket_connection(ws):
    assert ws.connected


def test_websocket_send_and_receive(ws):
    ws.send("Hello, server!")
    result = ws.recv()
    assert result == "Hello, client!"

