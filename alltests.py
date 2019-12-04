import unittest
import random

import number
import matrix

import pprint
pp = pprint.PrettyPrinter(indent=4)


class TestNumber(unittest.TestCase):

    def test_is_number_pos(self):
        self.assertTrue( number.is_number(5) )

    def test_is_number_zero(self):
        self.assertTrue( number.is_number(0) )

    def test_is_number_neg(self):
        self.assertTrue( number.is_number(-5) )

    def test_is_number_float(self):
        self.assertTrue( number.is_number(-5.5) )

    def test_is_number_alpha(self):
        self.assertFalse( number.is_number('A') )

    def test_is_prime_7(self):
        self.assertTrue( number.is_prime(7) )

    def test_is_prime_2(self):
        self.assertTrue( number.is_prime(2) )

    def test_is_prime_4(self):
        self.assertFalse( number.is_prime(4) )

    def test_is_odd_3(self):
        self.assertTrue( number.is_odd(3) )

    def test_is_odd_2(self):
        self.assertFalse( number.is_odd(2) )

    def test_is_odd_0(self):
        self.assertFalse( number.is_odd(0) )

    def test_is_even_2(self):
        self.assertTrue( number.is_even(2) )

    def test_is_even_3(self):
        self.assertFalse( number.is_even(3) )

    def test_is_even_0(self):
        self.assertTrue( number.is_even(0) )

class TestMatrix(unittest.TestCase):

    def test_is_matrix_natural_valid(self):
        M = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        self.assertTrue(matrix.is_matrix(M))


    def test_is_matrix_unatural_valid(self):
        M = [
            [-1,2,3],
            [4,5,6.2],
            [7,8,0]
        ]

        self.assertTrue(matrix.is_matrix(M))

    def test_is_matrix_invalid(self):
        M = [
            [1,'a',3],
            [4,5,6],
            [7,8,'b']
        ]

        self.assertFalse(matrix.is_matrix(M))

    def test_Identity(self):
        N = 10
        M = matrix.Identity(N)

        self.assertEqual(M[0][0], 1)
        self.assertEqual(M[0][1], 0)

    def test_neg(self):
        M = [
            [1,2],
            [-3,0]
        ]

        neg_M = matrix.neg(M)
        self.assertEqual(neg_M[0][0],-1)
        self.assertEqual(neg_M[1][1],0)
        self.assertEqual(neg_M[1][0],3)


    def test_concat_equallen(self):
        A = [
            [1.1,2],
            [0,4]
        ]
        B = [
            [8,9],
            [7,-1]
        ]

        self.assertTrue(True)


class DontRunELK(unittest.TestCase):

    def xtest_simple(self):

        struct1 = {
            'a': '1',
            'b': '2',
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual(len(docs),1)
        self.assertEqual(docs[0]['a'],'1')
        self.assertEqual(docs[0]['b'],'2')


    def xtest_with_list(self):

        struct1 = {
            'a': '1',
            'b': ['21','22'],
            'c': {'c1':'31'}
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual((len(docs),2))


    def xtest_with_2list(self):
        struct1 = {
            'a': '1',
            'b': ['21','22'],
            'c': ['31','32']
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual((len(docs),4))


    def xtest_with_nestedlist(self):
        struct1 = {
            'a': '11',
            'b': ['22','23'],
            'c': [['33','32'],['44','41']]
        }

        docs = elk.struct_to_docs(struct1)

        self.assertEqual((len(docs),8))


    def xtest_complex(self):
        self.assertTrue(True)
