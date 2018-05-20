import numpy as np
import pytest
import vibration_toolbox as vtb
from numpy.testing import assert_allclose


@pytest.fixture
def _normalize_vect():
    X = np.array([[0.84 + 0.j,  0.14 - 0.j,  0.84 - 0.j,  0.14 + 0.j],
                  [0.01 - 0.3j,  0.00 + 0.15j,  0.01 + 0.3j,  0.00 - 0.15j],
                  [-0.09 + 0.42j, -0.01 + 0.65j, -0.09 - 0.42j, -0.01 - 0.65j],
                  [0.15 + 0.04j, -0.74 + 0.j,  0.15 - 0.04j, -0.74 - 0.j]])
    Y = np.array([[-0.03 - 0.41j,  0.04 + 0.1j, -0.03 + 0.41j,  0.04 - 0.1j],
                  [0.88 + 0.j,  0.68 + 0.j,  0.88 - 0.j,  0.68 - 0.j],
                  [-0.21 - 0.j,  0.47 + 0.05j, -0.21 + 0.j,  0.47 - 0.05j],
                  [0.00 - 0.08j,  0.05 - 0.54j,  0.00 + 0.08j,  0.05 + 0.54j]])
    Yn = vtb.mdof._normalize(X, Y)
    print(Yn)
    return Yn


def test_normalise(_normalize_vect):
    Yn = np.array([[0.57822773 - 4.69882840e-02j,  0.11696967 - 5.85231773e-02j,
                    0.57822773 + 4.69882840e-02j,  0.11696967 + 5.85231773e-02j],
                   [0.00998912 + 1.24180506e+00j, -0.0687932 - 8.22911025e-01j,
                    0.00998912 - 1.24180506e+00j, -0.0687932 + 8.22911025e-01j],
                   [-0.00238377 - 2.96339843e-01j,  0.01295993 - 5.73835061e-01j,
                    -0.00238377 + 2.96339843e-01j,  0.01295993 + 5.73835061e-01j],
                   [0.11289137 - 9.08101611e-04j, -0.65854649 - 5.87827297e-03j,
                    0.11289137 + 9.08101611e-04j, -0.65854649 + 5.87827297e-03j]])
    assert_allclose(_normalize_vect, Yn)
