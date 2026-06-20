# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_write_arg_valid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._write_error_test(csv.Error, None)
    self._write_test((), '')
    self._write_test([None], '""')
    self._write_error_test(csv.Error, [None], quoting=csv.QUOTE_NONE)
    self._write_error_test(OSError, BadIterable())

    class BadList:

        def __len__(self):
            return 10

        def __getitem__(self, i):
            if i > 2:
                raise OSError
    self._write_error_test(OSError, BadList())

    class BadItem:

        def __str__(self):
            raise OSError
    self._write_error_test(OSError, [BadItem()])
