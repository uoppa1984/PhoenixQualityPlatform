def can_release(total_tests, failed_tests):
    return total_tests > 0 and failed_tests == 0
