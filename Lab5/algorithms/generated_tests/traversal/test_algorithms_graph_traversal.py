# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.graph.traversal as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.dfs_traverse(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -930.43252
    module_0.bfs_traverse(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.dfs_traverse_recursive(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1086
    module_0.dfs_traverse_recursive(int_0, int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    str_0 = "t#[ k_4gz@v"
    module_0.dfs_traverse(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "3wG\x0bS"
    bool_0 = False
    module_0.bfs_traverse(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "J92H'E\t},sl/N"
    bool_0 = True
    module_0.dfs_traverse_recursive(str_0, bool_0)


def test_case_7():
    bool_0 = True
    bool_1 = True
    tuple_0 = (bool_1, bool_1)
    dict_0 = {bool_0: bool_0, bool_0: tuple_0, tuple_0: bool_1, tuple_0: tuple_0}
    var_0 = module_0.bfs_traverse(dict_0, tuple_0)


def test_case_8():
    bool_0 = True
    bool_1 = True
    tuple_0 = (bool_1, bool_1)
    dict_0 = {bool_0: bool_0, bool_0: tuple_0, tuple_0: bool_1, tuple_0: tuple_0}
    var_0 = module_0.dfs_traverse(dict_0, tuple_0)
    var_1 = module_0.bfs_traverse(dict_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    bool_0 = True
    bool_1 = False
    set_0 = {bool_0, bool_1, bool_0, bool_1}
    tuple_0 = (set_0,)
    module_0.dfs_traverse(tuple_0, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = True
    bool_1 = False
    dict_0 = {bool_0: bool_1, bool_0: bool_0}
    bool_2 = True
    tuple_0 = (bool_0, dict_0, bool_2)
    var_0 = module_0.dfs_traverse_recursive(tuple_0, bool_0)
    str_0 = "y[\rQhTR"
    none_type_0 = None
    module_0.dfs_traverse_recursive(str_0, none_type_0)
