import os
from pathlib import Path
import zipfile

import streamlit as st
import pandas as pd
import numpy as np

import utils
from utils import create_zip_of_sample_data, load_dsc_file, load_dta_file, get_acq_pars, create_sino2d, show_sinogram
import constants
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


def load_data():
    st.title('Upload Bruker Data (or use example)')
    col1, col2, col3 = st.columns(3)
    with col1:
        sino_files = st.file_uploader("Choose a sinogram", accept_multiple_files=True, type=["DSC", "DTA", "YGF"])
        for uploaded_file in sino_files:
            with open(os.path.join(constants.PATH_TO_STORE_TEMP_SINO_DATA, uploaded_file.name), 'wb') as f:
                f.write(uploaded_file.getbuffer())
        raw_files = os.listdir(constants.PATH_TO_STORE_TEMP_SINO_DATA)
        for file in raw_files:
            if file.endswith('.DTA'):
                raw_dta = load_dta_file(os.path.join(constants.PATH_TO_STORE_TEMP_SINO_DATA, file))
                sinogram = create_sino2d(raw_dta, pars)
            elif file.endswith('.DSC'):
                raw_dsc = load_dsc_file(Path(os.path.join(constants.PATH_TO_STORE_TEMP_SINO_DATA, file)))
                pars = get_acq_pars(raw_dsc)

    with col2:
        ref_files = st.file_uploader("Choose a reference", accept_multiple_files=True, type=["DSC", "DTA"])
        for uploaded_file in ref_files:
            with open(os.path.join(constants.PATH_TO_STORE_TEMP_REF_DATA, uploaded_file.name), 'wb') as f:
                f.write(uploaded_file.getbuffer())
        ref_files = os.listdir(constants.PATH_TO_STORE_TEMP_REF_DATA)
        for file in ref_files:
            if file.endswith('.DTA'):
                ref_dta = load_dta_file(os.path.join(constants.PATH_TO_STORE_TEMP_REF_DATA, file))

    with col3:
        for _ in range(3):
            st.text("")

        on = st.toggle('Use example data', value=True)
        if on:
            with zipfile.ZipFile(constants.PATH_TO_SAMPLE_DATA, 'r') as zip_ref:
                zip_ref.extractall(constants.PATH_TO_STORE_TEMP_SAMPLE)
            st.write('Use data loaded')

            raw_dta = load_dta_file(os.path.join(constants.PATH_TO_STORE_TEMP_SAMPLE, 'data.DTA'))
            raw_dsc = load_dsc_file(Path(os.path.join(constants.PATH_TO_STORE_TEMP_SAMPLE, 'data.DSC')))
            ref_dta = load_dta_file(os.path.join(constants.PATH_TO_STORE_TEMP_SAMPLE, 'ref.DTA'))
            pars = get_acq_pars(raw_dsc)
            sinogram = create_sino2d(raw_dta, pars)

    try:
        col1, col2 = st.columns([2, 1])
        with col1:
            with st.container():
                img_plt = show_sinogram(sinogram)
                st.text('Acquired sinogram')
                st.pyplot(img_plt)
        with col2:
            ref_data = pd.DataFrame(ref_dta, columns=['a'], dtype=float)
            st.text('Reference spectrum')
            st.line_chart(ref_data)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    return sinogram, ref_dta, pars


def deconvolution(sino, ref, filter_value):
    ref_interp = utils.spectrum_interpolation(ref, sino.shape[0])
    deco_sino = np.apply_along_axis(lambda x: utils.deconvolution(x, ref_interp, filter_value),
                                    axis=0, arr=sino)
    try:
        col1, col2 = st.columns([2, 1])
        with col1:
            with st.container():
                img_plt = show_sinogram(deco_sino)
                for _ in range(5):
                    st.text("")
                st.text('Sinogram after deconvolution')
                st.pyplot(img_plt)
        with col2:
            sl = st.slider('# Projection :', 1, deco_sino.shape[1], 1)
            st.text(f' Projection: {sl}')
            prj_sel = pd.DataFrame(deco_sino[:, sl - 1], columns=['a'], dtype=float)
            st.line_chart(prj_sel)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    return deco_sino
