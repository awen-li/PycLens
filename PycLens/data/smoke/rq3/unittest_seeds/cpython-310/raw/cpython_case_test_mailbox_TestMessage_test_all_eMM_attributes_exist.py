# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessage_test_all_eMM_attributes_exist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eMM = email.message_from_string(_sample_message)
    msg = self._factory(_sample_message)
    for attr in eMM.__dict__:
        self.assertIn(attr, msg.__dict__, '{} attribute does not exist'.format(attr))
