# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_writer_arg_valid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_arg_valid(csv.writer, StringIO())

    class BadWriter:

        @property
        def write(self):
            raise OSError
    self.assertRaises(OSError, csv.writer, BadWriter())
