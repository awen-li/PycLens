# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_classmethods_in_c

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import xxsubtype as spam
    a = (1, 2, 3)
    d = {'abc': 123}
    (x, a1, d1) = spam.spamlist.classmeth(*a, **d)
    self.assertEqual(x, spam.spamlist)
    self.assertEqual(a, a1)
    self.assertEqual(d, d1)
    (x, a1, d1) = spam.spamlist().classmeth(*a, **d)
    self.assertEqual(x, spam.spamlist)
    self.assertEqual(a, a1)
    self.assertEqual(d, d1)
    spam_cm = spam.spamlist.__dict__['classmeth']
    (x2, a2, d2) = spam_cm(spam.spamlist, *a, **d)
    self.assertEqual(x2, spam.spamlist)
    self.assertEqual(a2, a1)
    self.assertEqual(d2, d1)

    class SubSpam(spam.spamlist):
        pass
    (x2, a2, d2) = spam_cm(SubSpam, *a, **d)
    self.assertEqual(x2, SubSpam)
    self.assertEqual(a2, a1)
    self.assertEqual(d2, d1)
    with self.assertRaises(TypeError) as cm:
        spam_cm()
    self.assertEqual(str(cm.exception), "descriptor 'classmeth' of 'xxsubtype.spamlist' object needs an argument")
    with self.assertRaises(TypeError) as cm:
        spam_cm(spam.spamlist())
    self.assertEqual(str(cm.exception), "descriptor 'classmeth' for type 'xxsubtype.spamlist' needs a type, not a 'xxsubtype.spamlist' as arg 2")
    with self.assertRaises(TypeError) as cm:
        spam_cm(list)
    expected_errmsg = "descriptor 'classmeth' requires a subtype of 'xxsubtype.spamlist' but received 'list'"
    self.assertEqual(str(cm.exception), expected_errmsg)
    with self.assertRaises(TypeError) as cm:
        spam_cm.__get__(None, list)
    self.assertEqual(str(cm.exception), expected_errmsg)
