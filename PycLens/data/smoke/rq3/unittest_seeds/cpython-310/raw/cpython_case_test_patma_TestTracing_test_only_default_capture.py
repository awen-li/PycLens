# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestTracing_test_only_default_capture

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(command):
        match command.split():
            case x:
                return x
    self.assertListEqual(self._trace(f, 'go n'), [1, 2, 3])
    self.assertListEqual(self._trace(f, 'go x'), [1, 2, 3])
    self.assertListEqual(self._trace(f, 'spam'), [1, 2, 3])
