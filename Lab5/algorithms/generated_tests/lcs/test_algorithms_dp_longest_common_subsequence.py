# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.dp.longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = set()
    tuple_0 = (bool_0, bool_0, set_0)
    var_0 = module_0.longest_common_subsequence(tuple_0, set_0)
    assert var_0 == 0
    module_0.longest_common_subsequence(bool_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    module_0.longest_common_subsequence(set_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xce?\x9a\x1e\xb5Sg;`,7\x1bS\xba\xf8y"
    var_0 = module_0.longest_common_subsequence(bytes_0, bytes_0)
    assert var_0 == 16
    none_type_0 = None
    module_0.longest_common_subsequence(bytes_0, none_type_0)
