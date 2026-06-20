# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMH_test_issue2625

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg0 = mailbox.MHMessage(self._template % 0)
    msg0.add_sequence('foo')
    key0 = self._box.add(msg0)
    refmsg0 = self._box.get_message(key0)
