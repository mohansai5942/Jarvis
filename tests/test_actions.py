from jarvis.actions import ActionRouter

def test_basic_intents():
    router = ActionRouter()
    assert "personal desktop AI assistant" in router.handle("who are you")
    assert "Today is" in router.handle("date")
    assert router.handle("hello") == "Hello. Systems are ready."
