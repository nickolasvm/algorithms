import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # with success
    message, key = "message", 3
    assert encrypt_message(message, key) == "sem_egas"
    message, key = "test_message", 4
    assert encrypt_message(message, key) == "egassem__tset"
    message, key = "my_message", 1
    assert encrypt_message(message, key) == "m_egassem_y"

    # with success when key is out of range
    message, key = "message", 7
    assert encrypt_message(message, key) == "egassem"

    # failing type validation
    message, key = 123, 3
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message, key)

    message, key = "message", "3"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, key)
