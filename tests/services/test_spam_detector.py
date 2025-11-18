import pytest
from app.services.spam_detector import SpamDetector


@pytest.fixture
def detector():
    """Fixture que crea una instancia de SpamDetector para reutilizar en los tests."""
    return SpamDetector()


def test_is_spam_with_spam_message(detector):
    """Test que verifica la detección de un mensaje spam."""
    spam_text = "Congratulations! You've won a free lottery ticket. Click here to claim your prize."

    is_spam, _ = detector.is_spam(spam_text)

    assert is_spam is True, "El mensaje debería ser detectado como spam"


def test_is_spam_with_legitimate_message(detector):
    """Test que verifica la detección de un mensaje legítimo."""
    legitimate_text = "Hi, I hope you're doing well. Let's schedule our meeting for next Tuesday at 3 PM."

    is_spam, _ = detector.is_spam(legitimate_text)

    assert is_spam is False, "El mensaje debería ser detectado como legítimo (no spam)"


def test_is_spam_with_empty_message(detector):
    """Test que verifica la detección de un mensaje vacío."""
    empty_text = ""

    is_spam, _ = detector.is_spam(empty_text)

    assert is_spam is False, "Un mensaje vacío no debería ser detectado como spam"
