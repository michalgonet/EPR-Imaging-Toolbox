import streamlit as st

import latex_formulas
import codes
import descriptions
import body
import constants


def main():
    st.set_page_config(layout="wide")
    st.sidebar.title('EPR Imaging Toolbox')
    main_choice = st.sidebar.radio('Menu', ['Data Sample', 'Algebra'])

    if main_choice == 'Algebra':
        handle_algebra()
    elif main_choice == 'Data Sample':
        handle_data_sample()


def handle_algebra():
    st.title("Linear Algebra")
    st.write(descriptions.linear_algebra_intro)
    st.latex(latex_formulas.general_linear_transformation_short)
    st.latex(latex_formulas.general_linear_transformation_long)
    body.transformation_matrix(title='Scaling', left=descriptions.scaling, right=codes.scaling_matrix)
    body.transformation_matrix(title='Translate', left=descriptions.translation, right=codes.translate_matrix)
    body.transformation_matrix(title='Rotation X', left=descriptions.rotation_x, right=codes.rotation_x_matrix)
    body.transformation_matrix(title='Rotation Y', left=descriptions.rotation_y, right=codes.rotation_y_matrix)
    body.transformation_matrix(title='Rotation Z', left=descriptions.rotation_z, right=codes.rotation_z_matrix)


def handle_data_sample():
    st.title("Sample Data")
    body.sample_data(data_title='3D dataset', data_desc=descriptions.sample_data_3d, filepath=constants.PATH_TO_SAMPLE_DATA)


if __name__ == "__main__":
    main()
