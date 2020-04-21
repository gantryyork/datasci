import unittest
import random

import number
import matrix
import gps.convert 
import gps.math

import pprint
pp = pprint.PrettyPrinter(indent=4)


class TestNumber(unittest.TestCase):

    def test_is_number_pos(self):
        self.assertTrue(number.is_number(5))

    def test_is_number_zero(self):
        self.assertTrue(number.is_number(0))

    def test_is_number_neg(self):
        self.assertTrue(number.is_number(-5))

    def test_is_number_float(self):
        self.assertTrue(number.is_number(-5.5))

    def test_is_number_alpha(self):
        self.assertFalse(number.is_number('A'))

    def test_is_prime_7(self):
        self.assertTrue(number.is_prime(7))

    def test_is_prime_2(self):
        self.assertTrue(number.is_prime(2))

    def test_is_prime_4(self):
        self.assertFalse(number.is_prime(4))

    def test_is_odd_3(self):
        self.assertTrue(number.is_odd(3))

    def test_is_odd_2(self):
        self.assertFalse(number.is_odd(2))

    def test_is_odd_0(self):
        self.assertFalse(number.is_odd(0))

    def test_is_even_2(self):
        self.assertTrue(number.is_even(2))

    def test_is_even_3(self):
        self.assertFalse(number.is_even(3))

    def test_is_even_0(self):
        self.assertTrue(number.is_even(0))

    def test_fib_4(self):
        self.assertEqual(number.fibinacci(4), 5)

    def test_is_fibinacci_1(self):
        self.assertTrue(number.is_fibinacci(1))

    def test_is_fibinacci_34(self):
        self.assertTrue(number.is_fibinacci(34))

    def test_is_fibinacci_17(self):
        self.assertFalse(number.is_fibinacci(17))

    def test_fib_score_1(self):
        self.assertGreater(number.fibinacci_score(1), 0.94)

    def test_fib_score_34(self):
        self.assertGreater(number.fibinacci_score(34), 0.94)

    def test_fib_score_17(self):
        self.assertLess(number.fibinacci_score(17), 0.94)

    def test_fib_series_1(self):
        self.assertEqual(number.fibinacci_series(1), [1])

    def test_fib_series_2(self):
        self.assertEqual(number.fibinacci_series(2), [1, 2])

    def test_fib_series_5(self):
        self.assertEqual(number.fibinacci_series(5), [1, 2, 3, 5, 8])

    def test_prime_series_0(self):
        self.assertEqual(number.prime_series(0), [0])

    def test_prime_series_0(self):
        self.assertEqual(number.prime_series(1), [0, 1])

    def test_prime_series_20(self):
        self.assertEqual(number.prime_series(
            20), [0, 1, 2, 3, 5, 7, 11, 13, 17, 19])

    def test_factoral_4(self):
        self.assertEqual(number.factoral(4), 24)


class TestMatrix(unittest.TestCase):

    def test_is_matrix_natural_valid(self):
        M = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.assertTrue(matrix.is_matrix(M))

    def test_is_matrix_unatural_valid(self):
        M = [
            [-1, 2, 3],
            [4, 5, 6.2],
            [7, 8, 0]
        ]

        self.assertTrue(matrix.is_matrix(M))

    def test_is_matrix_invalid(self):
        M = [
            [1, 'a', 3],
            [4, 5, 6],
            [7, 8, 'b']
        ]

        self.assertFalse(matrix.is_matrix(M))

    def test_same_dims(self):
        A = [
            [1, 2],
            [3, 4]
        ]
        B = [
            [8, 9],
            [0, 6]
        ]
        self.assertTrue(matrix.same_dimensions(A, B))

    def test_diff_dims(self):
        A = [
            [1, 2],
            [3, 4]
        ]
        B = [
            [8, 9, 1],
            [0, 6, 2],
            [0, 8, 2]
        ]
        self.assertFalse(matrix.same_dimensions(A, B))

    def test_Identity(self):
        N = 10
        M = matrix.Identity(N)

        self.assertEqual(M[0][0], 1)
        self.assertEqual(M[0][1], 0)

    def test_multiply(self):
        M = [
            [1, 2.2],
            [-3, 0]
        ]

        kM = matrix.multiply(2.5, M)
        self.assertEqual(kM[0][0], 2.5)
        self.assertEqual(kM[1][1], 0)
        self.assertEqual(kM[1][0], -7.5)

    def test_neg(self):
        M = [
            [1, 2],
            [-3, 0]
        ]

        neg_M = matrix.neg(M)
        self.assertEqual(neg_M[0][0], -1)
        self.assertEqual(neg_M[1][1], 0)
        self.assertEqual(neg_M[1][0], 3)

    def test_concat_equalx(self):
        A = [
            [1.1, 2],
            [0, 4]
        ]
        B = [
            [8, 9],
            [7, -1]
        ]
        Z = matrix.concat(A, B)

        self.assertEqual(len(Z[0]), 4)
        self.assertEqual(len(Z), 2)

    def test_concat_nonequalx(self):
        A = [
            [1.1, 2, 3],
            [0, 4, 6]
        ]
        B = [
            [8, 9],
            [7, -1]
        ]
        Z = matrix.concat(A, B)

        self.assertEqual(len(Z[0]), 5)
        self.assertEqual(len(Z), 2)

    def test_concat_nonequaly(self):
        A = [
            [1.1, 2],
            [0, 4],
            [6, 7]
        ]
        B = [
            [8, 9],
            [7, -1]
        ]
        Z = matrix.concat(A, B)

        self.assertEqual(Z, None)

    def test_append_2x2_2x2(self):
        A = [
            [1.1, 2],
            [0, 4],
            [6, 7]
        ]
        B = [
            [8, 9],
            [7, -1]
        ]

        Z = matrix.append(A, B)
        self.assertEqual(len(Z), 4)
        self.assertEqual(Z[5][1], -1)

    def test_hadamard_2(self):
        H2 = matrix.Hadamard(2)
        self.assertTrue(True)


class TestGPS(unittest.TestCase):

    def test_precision_4(self):
        n = gps.convert.precision(8.3333333, 4)
        self.assertEqual(n, 8.3333)

    def test_ddeg(self):
        ddeg = gps.convert.ddeg(45, 30, 30)
        self.assertEqual(ddeg, 45.5083)

    def test_dms(self):
        p = gps.convert.dms(145.5056)
        self.assertEqual([145, 30, 20], p)

    def test_nm(self):
        self.assertEqual(gps.convert.nm(50), 26.9979)

    def test_mi(self):
        self.assertEqual(gps.convert.mi(50), 31.0686)

    def test_lon_pos(self):
        self.assertEqual(gps.convert.longitude(135), 135)

    def test_lon_neg(self):
        self.assertEqual(gps.convert.longitude(-45), -45)

    def test_lon_pos_big(self):
        self.assertEqual(gps.convert.longitude(190), -170)

    def test_lon_neg_big(self):
        self.assertEqual(gps.convert.longitude(-270), 90)

    def test_lat_pos(self):
        self.assertEqual(gps.convert.latitude(75), 75)

    def test_lat_neg(self):
        self.assertEqual(gps.convert.latitude(-30), -30)

    def test_lat_pos_big(self):
        self.assertEqual(gps.convert.latitude(135), 45)

    def test_lat_neg_big(self):
        self.assertEqual(gps.convert.latitude(-110), -70)

class DontRunELK(unittest.TestCase):

    def xtest_simple(self):

        struct1 = {
            'a': '1',
            'b': '2',
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual(len(docs), 1)
        self.assertEqual(docs[0]['a'], '1')
        self.assertEqual(docs[0]['b'], '2')

    def xtest_with_list(self):

        struct1 = {
            'a': '1',
            'b': ['21', '22'],
            'c': {'c1': '31'}
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual((len(docs), 2))

    def xtest_with_2list(self):
        struct1 = {
            'a': '1',
            'b': ['21', '22'],
            'c': ['31', '32']
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual((len(docs), 4))

    def xtest_with_nestedlist(self):
        struct1 = {
            'a': '11',
            'b': ['22', '23'],
            'c': [['33', '32'], ['44', '41']]
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual((len(docs), 8))

    def xtest_complex(self):
        self.assertTrue(True)
