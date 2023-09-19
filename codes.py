scaling_matrix = '''
import numpy as np

def hmatrix_scale(s:np.ndarray) -> np.ndarray:
    """
    Example:
    >>> scaling_factors = np.array([2.0, 1.5, 0.5])
    >>> transformation_matrix = hmatrix_scale(scaling_factors)
    """
    sr = len(s)
    out = np.eye(sr + 1)
    out[:sr, :sr] = np.diag(s)
    return out

'''

translate_matrix = '''
import numpy as np

def hmatrix_translate(t:np.ndarray) -> np.ndarray:
    """
    Example:
    >>> translation_vector = np.array([1.0, 2.0, 3.0])
    >>> transformation_matrix = hmatrix_translate(translation_vector)
    """
    t = np.asarray(t)
    sr = t.shape[0] if len(t.shape) > 1 else t.size
    th = np.eye(sr + 1)
    th[:-1, -1] = t
    return th

'''

rotation_x_matrix = '''
import numpy as np

def hmatrix_rotate_x(theta:float) -> np.ndarray:
    """
    >>> rotation_matrix = hmatrix_rotate_x(45)
    """
    tr = np.radians(theta)
    st, ct = np.sin(tr), np.cos(tr)

    rh = np.eye(4)

    rh[1, 1] = ct
    rh[1, 2] = st
    rh[2, 1] = -st
    rh[2, 2] = ct

    return rh
'''
rotation_y_matrix = '''
import numpy as np

def hmatrix_rotate_y(theta:float) -> np.ndarray:
    """
    >>> rotation_matrix = hmatrix_rotate_y(45)
    """
    tr = np.radians(theta)
    st, ct = np.sin(tr), np.cos(tr)

    rh = np.eye(4)

    rh[0, 0] = ct
    rh[0, 2] = -st
    rh[2, 0] = st
    rh[2, 2] = ct

    return rh
'''


rotation_z_matrix = '''
import numpy as np

def hmatrix_rotate_z(theta:float) -> np.ndarray:
    """
    >>> rotation_matrix = hmatrix_rotate_z(45.0)
    """
    tr = np.radians(theta)
    st, ct = np.sin(tr), np.cos(tr)

    rh = np.eye(4)

    rh[0, 0] = ct
    rh[0, 1] = st
    rh[1, 0] = -st
    rh[1, 1] = ct

    return rh
'''