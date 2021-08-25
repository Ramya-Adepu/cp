import os,sys
sys.path.append(os.getcwd())
from nth_palindromic_prime import fun_nth_palindromic_prime
import pytest


@pytest.mark.parametrize('a, result',[
    (0,2),(1,3),(10,313),(15,757),(20,10301),(25,12421)
])
def test_fun_nth_palindromic_prime(a, result):
    assert fun_nth_palindromic_prime(a) == result

    # (0,2),(1,3),(10,313),(15,757),(20,10301),(25,12421)

	# 0  1  2  3  4   5    6    7    8    9    10   11   12   13   14   15   16   17   18     19    20    25
	# 2  3  5  7  11  101  151  181  191  313  353  373  383  727  757  797  919  929  10301  10501 10601 12821
