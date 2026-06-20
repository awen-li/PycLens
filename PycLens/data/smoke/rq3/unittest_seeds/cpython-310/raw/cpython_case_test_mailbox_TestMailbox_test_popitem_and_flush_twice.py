# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_popitem_and_flush_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._box.add(self._template % 0)
    self._box.add(self._template % 1)
    self._box.flush()
    self._box.popitem()
    self._box.flush()
    self._box.popitem()
    self._box.flush()
