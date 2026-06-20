# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: FormatterTest_test_defaults_parameter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmts = ['%(custom)s %(message)s', '{custom} {message}', '$custom $message']
    styles = ['%', '{', '$']
    for (fmt, style) in zip(fmts, styles):
        f = logging.Formatter(fmt, style=style, defaults={'custom': 'Default'})
        r = self.get_record()
        self.assertEqual(f.format(r), 'Default Message with 2 placeholders')
        r = self.get_record('custom')
        self.assertEqual(f.format(r), '1234 Message with 2 placeholders')
        f = logging.Formatter(fmt, style=style)
        r = self.get_record()
        self.assertRaises(ValueError, f.format, r)
        f = logging.Formatter(fmt, style=style, defaults={'Non-existing': 'Default'})
        r = self.get_record('custom')
        self.assertEqual(f.format(r), '1234 Message with 2 placeholders')
