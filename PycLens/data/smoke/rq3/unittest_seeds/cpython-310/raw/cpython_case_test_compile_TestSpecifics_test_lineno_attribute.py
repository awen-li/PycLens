# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_lineno_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def load_attr():
        return o.a
    load_attr_lines = [2, 3, 1]

    def load_method():
        return o.m(0)
    load_method_lines = [2, 3, 4, 3, 1]

    def store_attr():
        o.a = v
    store_attr_lines = [5, 2, 3]

    def aug_store_attr():
        o.a += v
    aug_store_attr_lines = [2, 3, 5, 1, 3]
    funcs = [load_attr, load_method, store_attr, aug_store_attr]
    func_lines = [load_attr_lines, load_method_lines, store_attr_lines, aug_store_attr_lines]
    for (func, lines) in zip(funcs, func_lines, strict=True):
        with self.subTest(func=func):
            code_lines = [line - func.__code__.co_firstlineno for (_, _, line) in func.__code__.co_lines()]
            self.assertEqual(lines, code_lines)
