# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMaildir_test_add_MM

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = mailbox.MaildirMessage(self._template % 0)
    msg.set_subdir('cur')
    msg.set_info('foo')
    key = self._box.add(msg)
    self.assertTrue(os.path.exists(os.path.join(self._path, 'cur', '%s%sfoo' % (key, self._box.colon))))
