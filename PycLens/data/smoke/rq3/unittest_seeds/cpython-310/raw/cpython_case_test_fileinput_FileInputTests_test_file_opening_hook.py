# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_file_opening_hook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        fi = FileInput(inplace=1, openhook=lambda f, m: None)
        self.fail('FileInput should raise if both inplace and openhook arguments are given')
    except ValueError:
        pass
    try:
        fi = FileInput(openhook=1)
        self.fail('FileInput should check openhook for being callable')
    except ValueError:
        pass

    class CustomOpenHook:

        def __init__(self):
            self.invoked = False

        def __call__(self, *args, **kargs):
            self.invoked = True
            return open(*args, encoding='utf-8')
    t = self.writeTmp('\n')
    custom_open_hook = CustomOpenHook()
    with FileInput([t], openhook=custom_open_hook) as fi:
        fi.readline()
    self.assertTrue(custom_open_hook.invoked, 'openhook not invoked')
