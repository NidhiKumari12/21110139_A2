# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.tree.avl.avl as module_0


def test_case_0():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.insert(avl_tree_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0


def test_case_1():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.re_balance()


@pytest.mark.xfail(strict=True)
def test_case_2():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    list_0 = []
    var_0 = avl_tree_0.insert(list_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_1 = avl_tree_0.update_balances()
    var_2 = avl_tree_0.update_heights()
    var_3 = avl_tree_0.insert(list_0)
    var_4 = avl_tree_0.insert(list_0)
    avl_tree_0.in_order_traverse()


def test_case_3():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.in_order_traverse()


@pytest.mark.xfail(strict=True)
def test_case_4():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    avl_tree_1 = module_0.AvlTree()
    assert avl_tree_1.height == -1
    assert avl_tree_1.balance == 0
    avl_tree_1.rotate_right()


@pytest.mark.xfail(strict=True)
def test_case_5():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.re_balance()
    avl_tree_1 = module_0.AvlTree()
    assert avl_tree_1.height == -1
    assert avl_tree_1.balance == 0
    avl_tree_1.rotate_left()


def test_case_6():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.insert(avl_tree_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_1 = avl_tree_0.update_heights(avl_tree_0)


def test_case_7():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.insert(avl_tree_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_1 = avl_tree_0.update_balances()


@pytest.mark.xfail(strict=True)
def test_case_8():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.insert(avl_tree_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    avl_tree_0.insert(var_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    set_0 = set()
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.insert(set_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_1 = avl_tree_0.insert(set_0)
    var_1.rotate_right()


def test_case_10():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.in_order_traverse()
    list_0 = [var_0, avl_tree_0]
    var_1 = avl_tree_0.insert(var_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_2 = avl_tree_0.update_balances()
    var_3 = avl_tree_0.update_heights()
    var_4 = avl_tree_0.insert(list_0)
    assert avl_tree_0.height == 1
    assert avl_tree_0.balance == -1


def test_case_11():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.in_order_traverse()
    list_0 = [var_0, avl_tree_0]
    var_1 = avl_tree_0.insert(list_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_2 = avl_tree_0.insert(var_0)
    assert avl_tree_0.height == 1
    assert avl_tree_0.balance == 1


@pytest.mark.xfail(strict=True)
def test_case_12():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.in_order_traverse()
    list_0 = [var_0, avl_tree_0]
    var_1 = avl_tree_0.insert(list_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_2 = avl_tree_0.insert(var_0)
    assert avl_tree_0.height == 1
    assert avl_tree_0.balance == 1
    var_3 = avl_tree_0.rotate_right()
    avl_tree_0.insert(list_0)


def test_case_13():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.in_order_traverse()
    list_0 = [var_0, avl_tree_0]
    var_1 = avl_tree_0.insert(list_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_2 = avl_tree_0.insert(var_0)
    assert avl_tree_0.height == 1
    assert avl_tree_0.balance == 1
    list_1 = [var_0]
    var_3 = avl_tree_0.insert(list_1)
    assert avl_tree_0.balance == 0


@pytest.mark.xfail(strict=True)
def test_case_14():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.in_order_traverse()
    list_0 = [var_0, avl_tree_0]
    var_1 = avl_tree_0.insert(var_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    var_2 = avl_tree_0.insert(list_0)
    assert avl_tree_0.height == 1
    assert avl_tree_0.balance == -1
    var_3 = module_0.AvlTree()
    assert var_3.height == -1
    assert var_3.balance == 0
    list_1 = [list_0, var_0, avl_tree_0]
    var_4 = avl_tree_0.insert(list_1)
    assert avl_tree_0.balance == 0
    var_1.update_heights()


@pytest.mark.xfail(strict=True)
def test_case_15():
    avl_tree_0 = module_0.AvlTree()
    assert avl_tree_0.height == -1
    assert avl_tree_0.balance == 0
    var_0 = avl_tree_0.in_order_traverse()
    list_0 = [var_0, avl_tree_0]
    var_1 = avl_tree_0.insert(list_0)
    assert (
        f"{type(avl_tree_0.node).__module__}.{type(avl_tree_0.node).__qualname__}"
        == "algorithms.tree.tree.TreeNode"
    )
    assert avl_tree_0.height == 0
    list_1 = [var_0]
    var_2 = avl_tree_0.insert(list_1)
    assert avl_tree_0.height == 1
    assert avl_tree_0.balance == 1
    var_3 = avl_tree_0.insert(var_0)
    assert avl_tree_0.balance == 0
    var_1.rotate_left()
