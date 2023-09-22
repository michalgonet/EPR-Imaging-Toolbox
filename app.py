import streamlit as st

import numpy as np

import latex_formulas
import codes
import descriptions
import body
import constants


def main():
    st.set_page_config(layout="wide")
    st.sidebar.title('EPR Imaging Toolbox')
    main_choice = st.sidebar.radio('Menu', ['Pre-processing', 'Data Sample', 'Algebra'])

    if main_choice == 'Algebra':
        handle_algebra()
    if main_choice == 'Data Sample':
        handle_data_sample()

    if main_choice == 'Pre-processing':
        sino, ref, par = handle_load_data()
        handle_deconvolution(sino, ref, par)


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
    body.sample_data(data_title='3D dataset', data_desc=descriptions.sample_data_3d,
                     filepath=constants.PATH_TO_SAMPLE_DATA)


def handle_load_data():
    sino, ref, pars = body.load_data()
    return sino, ref, pars


def handle_deconvolution(sino, ref, pars):
    st.title('Deconvolution')
    st.write(descriptions.deconvolution)
    filter_val = st.slider('# Deconvolution filter :', 1, 128, 15)
    sino_deco = body.deconvolution(sino, ref, filter_val)
    np.save('Example_data/temp_data/sinogram_deco.npy', sino_deco, allow_pickle=True)
    with open('Example_data/temp_data/sinogram_deco.npy', 'rb') as f:
        st.download_button(
            label='Download sinogram as npy',
            data=f,
            file_name='sinogram_after_deconvolution.npy',
            key='npy'
        )


if __name__ == "__main__":
    main()
