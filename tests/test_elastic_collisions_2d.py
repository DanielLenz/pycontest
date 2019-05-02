import pytest

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin

def get_energy(m1, m2, v1, v2):
    return 0.5*(m1*v1**2+m2*v2**2)


def get_momentum(m1, m2, v1, v2):
    return m1*v1+m2*v2

# 2d are more complicated, depends on the vector r12
# but we can always check the simplest cases, that are basically 1d cases
class Test2d:
    # let's start from 2 balls that have only x velocity, and r12 also has only x component
    def test_collision_2d_1(self):
        v1_f, v2_f = ec.collision_2d(v1=[1, 0], v2=[-2, 0], r12=[1, 0], m1=1, m2=1)
        assert (v1_f == [-2, 0]).all()
        assert (v2_f == [1, 0]).all()

    # you cannow do the same for y components
    def test_collision_2d_2(self):
        v1_f, v2_f = ec.collision_2d(
            v1=[0, 1], v2=[0, -2], r12=[0, 1], m1=1, m2=1)
        assert (v1_f == [0, -2]).all()
        assert (v2_f == [0, 1]).all()

    # you can also check the energy and momentum



