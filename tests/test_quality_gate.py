from quality_gate import can_release


def test_allows_release_when_no_tests_fail():
    assert can_release(0) is True


def test_blocks_release_when_a_test_fails():
    assert can_release(1) is False
