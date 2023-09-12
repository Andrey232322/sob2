import pytest

from zada4i import triangle,krug


@pytest.mark.parametrize('a, res',[(2,12.56),(3,28.26),(-3,28.26)])
def test_main_krug(a,res):
    assert krug(a) == res

@pytest.mark.parametrize('a,b,c, res',[(2,2,2,1.7320508075688772),(4,2,2,0),(4,3,2,0),
                                       (4,5,7,9.797958971132712)])
def test_main_treangle(a,b,c,res):
    assert triangle(a,b,c) == res