# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestTracing_test_no_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(command):
        match command.split():
            case ['go', direction] if direction in 'nesw':
                return f'go {direction}'
            case ['go', _]:
                return 'no go'
    self.assertListEqual(self._trace(f, 'go n'), [1, 2, 3])
    self.assertListEqual(self._trace(f, 'go x'), [1, 2, 4, 5])
    self.assertListEqual(self._trace(f, 'spam'), [1, 2, 4])
