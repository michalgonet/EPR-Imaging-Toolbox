import streamlit as st

import latex_formulas
import codes
import descriptions
import body


def main():
    st.set_page_config(layout="wide")
    st.sidebar.title('EPR Imaging Toolbox')
    main_choice = st.sidebar.radio('Menu', ['Algebra'])

    if main_choice == 'Algebra':
        handle_algebra()


def handle_algebra():
    st.title("Linear Algebra")
    st.write(descriptions.linear_algebra_intro)
    st.latex(latex_formulas.general_linear_transformation_short)
    st.latex(latex_formulas.general_linear_transformation_long)
    body.transformation_matrix(
        title='Scaling',
        matrix_type='S',
        left=descriptions.scaling,
        right=codes.scaling_matrix)

    body.transformation_matrix(
        title='Translate',
        matrix_type='T',
        left=descriptions.translation,
        right=codes.translate_matrix)

    body.transformation_matrix(
        title='Rotation X',
        matrix_type='Rx',
        left=descriptions.rotation_x,
        right=codes.rotation_x_matrix)

    body.transformation_matrix(
        title='Rotation Y',
        matrix_type='Ry',
        left=descriptions.rotation_y,
        right=codes.rotation_y_matrix)

    body.transformation_matrix(
        title='Rotation Z',
        matrix_type='Rz',
        left=descriptions.rotation_z,
        right=codes.rotation_z_matrix)


if __name__ == "__main__":
    main()
