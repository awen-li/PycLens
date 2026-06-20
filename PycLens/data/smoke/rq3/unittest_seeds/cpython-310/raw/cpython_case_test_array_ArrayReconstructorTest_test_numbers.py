# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: ArrayReconstructorTest_test_numbers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testcases = ((['B', 'H', 'I', 'L'], UNSIGNED_INT8, '=BBBB', [128, 127, 0, 255]), (['b', 'h', 'i', 'l'], SIGNED_INT8, '=bbb', [-128, 127, 0]), (['H', 'I', 'L'], UNSIGNED_INT16_LE, '<HHHH', [32768, 32767, 0, 65535]), (['H', 'I', 'L'], UNSIGNED_INT16_BE, '>HHHH', [32768, 32767, 0, 65535]), (['h', 'i', 'l'], SIGNED_INT16_LE, '<hhh', [-32768, 32767, 0]), (['h', 'i', 'l'], SIGNED_INT16_BE, '>hhh', [-32768, 32767, 0]), (['I', 'L'], UNSIGNED_INT32_LE, '<IIII', [1 << 31, (1 << 31) - 1, 0, (1 << 32) - 1]), (['I', 'L'], UNSIGNED_INT32_BE, '>IIII', [1 << 31, (1 << 31) - 1, 0, (1 << 32) - 1]), (['i', 'l'], SIGNED_INT32_LE, '<iii', [-1 << 31, (1 << 31) - 1, 0]), (['i', 'l'], SIGNED_INT32_BE, '>iii', [-1 << 31, (1 << 31) - 1, 0]), (['L'], UNSIGNED_INT64_LE, '<QQQQ', [1 << 31, (1 << 31) - 1, 0, (1 << 32) - 1]), (['L'], UNSIGNED_INT64_BE, '>QQQQ', [1 << 31, (1 << 31) - 1, 0, (1 << 32) - 1]), (['l'], SIGNED_INT64_LE, '<qqq', [-1 << 31, (1 << 31) - 1, 0]), (['l'], SIGNED_INT64_BE, '>qqq', [-1 << 31, (1 << 31) - 1, 0]), (['L'], UNSIGNED_INT64_LE, '<QQQQ', [1 << 63, (1 << 63) - 1, 0, (1 << 64) - 1]), (['L'], UNSIGNED_INT64_BE, '>QQQQ', [1 << 63, (1 << 63) - 1, 0, (1 << 64) - 1]), (['l'], SIGNED_INT64_LE, '<qqq', [-1 << 63, (1 << 63) - 1, 0]), (['l'], SIGNED_INT64_BE, '>qqq', [-1 << 63, (1 << 63) - 1, 0]), (['f'], IEEE_754_FLOAT_LE, '<ffff', [16711938.0, float('inf'), float('-inf'), -0.0]), (['f'], IEEE_754_FLOAT_BE, '>ffff', [16711938.0, float('inf'), float('-inf'), -0.0]), (['d'], IEEE_754_DOUBLE_LE, '<dddd', [9006104071832581.0, float('inf'), float('-inf'), -0.0]), (['d'], IEEE_754_DOUBLE_BE, '>dddd', [9006104071832581.0, float('inf'), float('-inf'), -0.0]))
    for testcase in testcases:
        (valid_typecodes, mformat_code, struct_fmt, values) = testcase
        arraystr = struct.pack(struct_fmt, *values)
        for typecode in valid_typecodes:
            try:
                a = array.array(typecode, values)
            except OverflowError:
                continue
            b = array_reconstructor(array.array, typecode, mformat_code, arraystr)
            self.assertEqual(a, b, msg='{0!r} != {1!r}; testcase={2!r}'.format(a, b, testcase))
