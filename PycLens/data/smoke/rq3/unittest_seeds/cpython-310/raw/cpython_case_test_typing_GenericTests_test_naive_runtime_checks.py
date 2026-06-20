# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_naive_runtime_checks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def naive_dict_check(obj, tp):
        if len(tp.__parameters__) > 0:
            raise NotImplementedError
        if tp.__args__:
            (KT, VT) = tp.__args__
            return all((isinstance(k, KT) and isinstance(v, VT) for (k, v) in obj.items()))
    self.assertTrue(naive_dict_check({'x': 1}, typing.Dict[str, int]))
    self.assertFalse(naive_dict_check({1: 'x'}, typing.Dict[str, int]))
    with self.assertRaises(NotImplementedError):
        naive_dict_check({1: 'x'}, typing.Dict[str, T])

    def naive_generic_check(obj, tp):
        if not hasattr(obj, '__orig_class__'):
            raise NotImplementedError
        return obj.__orig_class__ == tp

    class Node(Generic[T]):
        ...
    self.assertTrue(naive_generic_check(Node[int](), Node[int]))
    self.assertFalse(naive_generic_check(Node[str](), Node[int]))
    self.assertFalse(naive_generic_check(Node[str](), List))
    with self.assertRaises(NotImplementedError):
        naive_generic_check([1, 2, 3], Node[int])

    def naive_list_base_check(obj, tp):
        return all((isinstance(x, tp.__orig_bases__[0].__args__[0]) for x in obj))

    class C(List[int]):
        ...
    self.assertTrue(naive_list_base_check([1, 2, 3], C))
    self.assertFalse(naive_list_base_check(['a', 'b'], C))
