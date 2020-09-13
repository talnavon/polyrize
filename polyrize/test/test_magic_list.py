import pytest
from polyrize.magic_list import MagicList


def test_simple():
    a = MagicList()
    a[0] = 5
    print(a)
    assert a[0] == 5



