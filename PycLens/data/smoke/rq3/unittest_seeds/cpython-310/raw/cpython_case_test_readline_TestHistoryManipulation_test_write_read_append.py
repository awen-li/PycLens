# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_readline.py
# case: TestHistoryManipulation_test_write_read_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hfile = tempfile.NamedTemporaryFile(delete=False)
    hfile.close()
    hfilename = hfile.name
    self.addCleanup(unlink, hfilename)
    readline.clear_history()
    readline.add_history('first line')
    readline.add_history('second line')
    readline.write_history_file(hfilename)
    readline.clear_history()
    self.assertEqual(readline.get_current_history_length(), 0)
    readline.read_history_file(hfilename)
    self.assertEqual(readline.get_current_history_length(), 2)
    self.assertEqual(readline.get_history_item(1), 'first line')
    self.assertEqual(readline.get_history_item(2), 'second line')
    readline.append_history_file(1, hfilename)
    readline.clear_history()
    readline.read_history_file(hfilename)
    self.assertEqual(readline.get_current_history_length(), 3)
    self.assertEqual(readline.get_history_item(1), 'first line')
    self.assertEqual(readline.get_history_item(2), 'second line')
    self.assertEqual(readline.get_history_item(3), 'second line')
    os.unlink(hfilename)
    try:
        readline.append_history_file(1, hfilename)
    except FileNotFoundError:
        pass
    else:
        os.unlink(hfilename)
    readline.write_history_file(hfilename)
