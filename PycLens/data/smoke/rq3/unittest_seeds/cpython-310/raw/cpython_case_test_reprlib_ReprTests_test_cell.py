# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_cell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def get_cell():
        x = 42

        def inner():
            return x
        return inner
    x = get_cell().__closure__[0]
    self.assertRegex(repr(x), '<cell at 0x[0-9A-Fa-f]+: int object at 0x[0-9A-Fa-f]+>')
    self.assertRegex(r(x), '<cell at 0x.*\\.\\.\\..*>')
