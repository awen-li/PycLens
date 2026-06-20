# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_add_that_raises_leaves_mailbox_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raiser(*args, **kw):
        raise Exception('a fake error')
    support.patch(self, email.generator.BytesGenerator, 'flatten', raiser)
    with self.assertRaises(Exception):
        self._box.add(email.message_from_string('From: Alphöso'))
    self.assertEqual(len(self._box), 0)
    self._box.close()
    self.assertMailboxEmpty()
