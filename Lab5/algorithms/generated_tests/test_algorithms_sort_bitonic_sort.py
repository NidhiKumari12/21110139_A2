# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.sort.bitonic_sort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "cEg\n"
    module_0.bitonic_sort(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.bitonic_sort(bool_0, bool_0)


def test_case_2():
    bytes_0 = b"\x0f{\xe4\xe4\\\xc6/*v"
    float_0 = -255.7416
    with pytest.raises(ValueError):
        module_0.bitonic_sort(bytes_0, float_0)
