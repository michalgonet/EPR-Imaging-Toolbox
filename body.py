import streamlit as st
from latex_formulas import scaling_matrix, translation_matrix, rotation_x, rotation_y, rotation_z


def matrix_augment(title, left, right):
    col1, col2 = st.columns([1, 1], gap='large')
    with col1:
        st.header(title, divider='blue')
        st.write(left)
    with col2:
        for _ in range(4):
            st.text("")
        st.code(right, language='python')


def transformation_matrix(title, matrix_type, left, right):
    mapping_type = {'S': scaling_matrix,
                    'T': translation_matrix,
                    'Rx': rotation_x,
                    'Ry': rotation_y,
                    'Rz': rotation_z
                    }

    col1, col2 = st.columns([1, 1], gap='large')
    with col1:
        st.header(title, divider='blue')
        st.write(left)
        st.latex(mapping_type[matrix_type])
    with col2:
        for _ in range(4):
            st.text("")
        st.code(right, language='python')
