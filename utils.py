import os
import zipfile
import re
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import constants
from classes import AcqPars


def create_zip_of_sample_data():
    folder_to_zip = constants.PATH_TO_DATA_FOR_ZIP
    zip_filename = constants.PATH_TO_SAMPLE_DATA
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder_name, sub_folders, filenames in os.walk(folder_to_zip):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                arch_name = os.path.relpath(file_path, folder_to_zip)
                zipf.write(file_path, arcname=arch_name)


def load_dta_file(path) -> np.ndarray:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")
    try:
        with open(path, 'rb') as f:
            return np.frombuffer(f.read(), dtype='>d')
    except Exception as e:
        raise Exception(f"Error loading file: {path}. {e}")


def load_dsc_file(file_path: Path) -> dict[str, list[str]]:
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    data_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('#') or not line:
                continue

            match = re.match(r'([a-zA-Z0-9_]+)\s+([\w.]+)\s*(\w*)\s*(.*)', line)
            if match:
                key = match.group(1)
                value = match.group(2)
                unit = match.group(3)
                extra_info = match.group(4)

                try:
                    value = float(value)
                except ValueError:
                    try:
                        value = int(value)
                    except ValueError:
                        if value.lower() == 'true':
                            value = True
                        elif value.lower() == 'false':
                            value = False

                if key in data_dict:
                    data_dict[key].append(value)
                else:
                    data_dict[key] = [value]

                if unit:
                    data_dict[key].append(unit)

                if extra_info:
                    data_dict[key].append(extra_info)

    for key in data_dict:
        data_dict[key] = [str(value).strip("'") for value in data_dict[key]]

    return data_dict


def get_acq_pars(raw_pars: dict[str, list[str]]) -> AcqPars:
    return AcqPars(
        data=str(raw_pars["DATE"][0]),
        time=str(raw_pars["TIME"][0]),
        exp_type=str(raw_pars["EXPT"][0]),
        scan_time=str(raw_pars["SWTime"][0]),
        img_time=str(raw_pars["TotalTime"][0]),
        img_type=str(" ".join(raw_pars["ImageType"])),
        orient=str(raw_pars["ImageOrient"][0]),
        points=int(float(raw_pars["XPTS"][0])),
        alpha_no=int(float(raw_pars["NrOfAlpha"][0])),
        beta_no=int(float(raw_pars["NrOfBeta"][0])),
        gamma_no=int(float(raw_pars["NrOfPsi"][0])),
        first_alpha=float(raw_pars["FirstAlpha"][0]),
        max_gamma=float(raw_pars["MaxPsi"][0]),
        gradient=float(raw_pars["GRAD"][0] if "GRAD" in raw_pars else raw_pars["AnglePsi"][0]),
        sweep=float(raw_pars["SweepWidth"][0]),
        center_field=float(raw_pars["CenterField"][0]),
        mod_amp=float(raw_pars["ModAmp"][0]),
        mod_freq=float(raw_pars["ModFreq"][0]),
        power=float(raw_pars["Power"][0])
    )


def create_sino2d(raw_data: np.ndarray, acq_pars: AcqPars) -> np.ndarray:
    return np.reshape(raw_data, [acq_pars.points, -1], order='F')


def show_sinogram(data):
    fig, ax = plt.subplots()
    plt.imshow(data, cmap='jet')
    fig.set_facecolor(constants.PLOT_BG_COLOR)
    ax.set_facecolor(constants.PLOT_FG_COLOR)
    ax.xaxis.label.set_color(constants.PLOT_TICK_COLOR)
    ax.yaxis.label.set_color(constants.PLOT_TICK_COLOR)
    ax.tick_params(axis='x', colors=constants.PLOT_TICK_COLOR)
    ax.tick_params(axis='y', colors=constants.PLOT_TICK_COLOR)
    plt.xlabel('# Projection')
    plt.ylabel('# Pkt')
    plt.yticks(fontsize=constants.TICK_FONT_SIZE)
    plt.xticks(fontsize=constants.TICK_FONT_SIZE)
    plt.axis('tight')
    return fig


def show_ref(data):
    fig, ax = plt.subplots()
    ax.plot(data)
    fig.set_facecolor(constants.PLOT_BG_COLOR)
    ax.set_facecolor(constants.PLOT_FG_COLOR)
    return fig


def deconvolution(grad_spectrum, non_grad_spectrum, filt):
    non_grad_spectrum = non_grad_spectrum.T
    points = grad_spectrum.shape[0]
    axis = np.linspace(0, 1024, points)
    sigma = filt / np.sqrt(2 * np.log(2))
    h = np.sqrt(2 / np.pi) * (1 / sigma) * np.exp(-2 * (axis / sigma) ** 2)
    h /= np.max(h)
    freq_resp = np.fft.fft(non_grad_spectrum)
    epsilon = 1e-10  # Small constant value to avoid zero division
    deco_temp = np.fft.ifft(np.fft.fft(grad_spectrum.T) * h / (freq_resp + epsilon)).real
    return np.fft.ifftshift(deco_temp)


def spectrum_interpolation(spectrum: np.ndarray, output_size: int) -> np.ndarray:
    x = np.arange(spectrum.shape[0])
    x_new = np.linspace(0, spectrum.shape[0], output_size, endpoint=False)
    return np.interp(x_new, x, spectrum)
