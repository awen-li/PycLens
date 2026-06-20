# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_invalid_nonascii_header_as_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    subj = self._nonascii_msg.splitlines()[1]
    key = self._box.add(subj.encode('latin-1'))
    self.assertEqual(self._box.get_string(key), 'Subject: =?unknown-8bit?b?RmFsaW5hcHThciBo4Xpob3pzeuFsbO104XNzYWwuIE3hciByZW5kZWx06Ww/?=\n\n')
