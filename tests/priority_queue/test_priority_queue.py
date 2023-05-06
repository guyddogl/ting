from ting_file_management.priority_queue import PriorityQueue
import pytest
from tests.priority_queue.arquivos import mock


def test_basic_priority_queueing():
    test = PriorityQueue()

    test.enqueue(mock[0])
    assert len(test.high_priority) == 1

    test.enqueue(mock[1])
    assert len(test.regular_priority) == 1

    assert test.search(1) == mock[1]

    test.dequeue()
    assert len(test.high_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        test.search(3)
