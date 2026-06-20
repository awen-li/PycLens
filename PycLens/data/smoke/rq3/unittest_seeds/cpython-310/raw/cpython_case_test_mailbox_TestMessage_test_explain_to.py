# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessage_test_explain_to

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = self._factory()
    for class_ in self.all_mailbox_types:
        other_msg = class_()
        msg._explain_to(other_msg)
    other_msg = email.message.Message()
    self.assertRaises(TypeError, lambda : msg._explain_to(other_msg))
