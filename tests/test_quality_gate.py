from quality_gate import can_release


def test_allows_release_when_all_tests_pass():
    assert can_release(3, 0) is True


def test_blocks_release_when_a_test_fails():
    assert can_release(3, 1) is False


def test_blocks_release_when_no_tests_run():
    assert can_release(0, 0) is False
