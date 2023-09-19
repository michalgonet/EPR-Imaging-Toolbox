import os

import streamlit as st


from utils import create_zip_of_sample_data
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


def transformation_matrix(title, left, right):
    mapping_type = {'Scaling': scaling_matrix,
                    'Translate': translation_matrix,
                    'Rotation X': rotation_x,
                    'Rotation Y': rotation_y,
                    'Rotation Z': rotation_z
                    }

    col1, col2 = st.columns([1, 1], gap='large')
    with col1:
        st.header(title, divider='blue')
        st.write(left)
        st.latex(mapping_type[title])
    with col2:
        for _ in range(4):
            st.text("")
        st.code(right, language='python')


def sample_data(data_title, data_desc, filepath):
    col1, col2 = st.columns([1, 1], gap='large')

    with col1:
        st.header(data_title, divider='blue')
        st.write(data_desc)
    with col2:
        for _ in range(6):
            st.text("")

        if not os.path.exists(filepath):
            create_zip_of_sample_data()

        with open(filepath, 'rb') as file:
            st.download_button(
                label='Download .zip of sample data',
                data=file.read(),
                file_name='sample_data.zip',
                key='zipfile'
            )
