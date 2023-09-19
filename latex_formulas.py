general_linear_transformation_short = r'''
    \vec{r} = \vec{r}A
'''

general_linear_transformation_long = r'''
    \begin{bmatrix}x^{'} & y^{'} & z^{'} & 1 \\ \end{bmatrix}=
    \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
    \begin{bmatrix}
    R_{11} & R_{11} & R_{11} & 0 \\
    R_{11} & R_{11} & R_{11} & 0 \\
    R_{11} & R_{11} & R_{11} & 0 \\
    T_1 & T_2 & T_3 & 1
    \end{bmatrix}
'''
scaling_matrix = r'''
    A = \begin{bmatrix}
    S{1} & 0 & 0 & 0 \\
    0 & S{2} & 0 & 0 \\
    0 & 0 & S_{3} & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
'''
translation_matrix = r'''
    A = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    T_1 & T_2 & T_3 & 1
    \end{bmatrix}
'''
rotation_x = r'''
    A = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & \cos(\theta) & \sin(\theta) & 0 \\
    0 & -\sin(\theta) & \cos(\theta) & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
'''

rotation_y = r'''
    A = \begin{bmatrix}
    \cos(\theta) & 0 & -\sin(\theta) & 0 \\
    0 & 1 & 0 & 0 \\
    \sin(\theta) & 0 & \cos(\theta) & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
'''

rotation_z = r'''
    A = \begin{bmatrix}
    \cos(\theta) & \sin(\theta) & 0 & 0 \\
    -\sin(\theta) & \cos(\theta) & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix}
'''
