import pytest
import random

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin


# a simple tests for equal masses (balls should exchange velocities)


def get_energy(m1, m2, v1, v2):
    return 0.5*(m1*v1**2+m2*v2**2)


def get_momentum(m1, m2, v1, v2):
    return m1*v1+m2*v2


class Test1d:
    # using default values of m1 and m2
    def test_collision_1d_1(self):
        v1_i, v2_i = 1, -2
        v1_f, v2_f = ec.collision_1d(v1_i=v1_i, v2_i=v2_i)

        assert (v1_f, v2_f) == (v2_i, v1_i)

    def test_collision_1d_momentum(self):
        v1_i = random.randint(-100, 100)
        v2_i = random.randint(-100, 100)
        m1 = random.randint(1, 100)
        m2 = random.randint(1, 100)

        momentum_initial = get_momentum(m1, m2, v1_i, v2_i)

        v1_f, v2_f = ec.collision_1d(v1_i=v1_i, v2_i=v2_i, m1=m1, m2=m2)
        momentum_final = get_momentum(m1, m2, v1_f, v2_f)

        assert momentum_initial == pytest.approx(momentum_final)

    def test_collision_1d_energy(self):
        v1_i = random.randint(-100, 100)
        v2_i = random.randint(-100, 100)
        m1 = random.randint(1, 100)
        m2 = random.randint(1, 100)

        e_initial = get_energy(m1, m2, v1_i, v2_i)

        v1_f, v2_f = ec.collision_1d(v1_i=v1_i, v2_i=v2_i, m1=m1, m2=m2)
        e_final = get_energy(m1, m2, v1_f, v2_f)

        assert e_initial == pytest.approx(e_final)




