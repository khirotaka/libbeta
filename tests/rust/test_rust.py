from libbeta import rust


def test_rust_func():
    assert rust.rust_func(20) == 400
