# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDF_test_add_mbox_or_mmdf_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        msg = class_('From foo@bar blah\nFrom: foo\n\n0\n')
        key = self._box.add(msg)
