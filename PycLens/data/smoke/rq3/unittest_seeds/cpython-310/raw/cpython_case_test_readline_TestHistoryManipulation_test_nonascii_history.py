# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_readline.py
# case: TestHistoryManipulation_test_nonascii_history

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    readline.clear_history()
    try:
        readline.add_history('entrée 1')
    except UnicodeEncodeError as err:
        self.skipTest('Locale cannot encode test data: ' + format(err))
    readline.add_history('entrée 2')
    readline.replace_history_item(1, 'entrée 22')
    readline.write_history_file(TESTFN)
    self.addCleanup(os.remove, TESTFN)
    readline.clear_history()
    readline.read_history_file(TESTFN)
    if is_editline:
        readline.add_history('dummy')
    self.assertEqual(readline.get_history_item(1), 'entrée 1')
    self.assertEqual(readline.get_history_item(2), 'entrée 22')
