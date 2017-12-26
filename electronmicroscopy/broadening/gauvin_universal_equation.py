#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.broadening.gauvin_universal_equation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Implementation of Gauvin universal equation for probe broadening.

Gauvin, R. and Rudinsky, S. A universal equation for computing the beam broadening of incident electrons in thin films,
Ultramicroscopy, 2016, 167, 21 - 30.

# How to compute beam broadening b

- Compute 1 + H using equation (30) and table 3. For 99%, you need to use equation (31) for t/lambda >= 1
- Compute lambda using equations (13) and (27), (15), and (17).
- Compute theta\* using equations (28) and (17) and table 2.
- Compute b using equation (12) and the previous results

"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import os

# Third party modules.
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import N_A, physical_constants

# Local modules.

# Project modules.
from electronmicroscopy import get_current_module_path

# Globals and constants variables.
PERCENT_90 = "90 %"
PERCENT_95 = "95 %"
PERCENT_99 = "99 %"

figure_path = get_current_module_path(__file__, '../../figures')
if not os.path.isdir(figure_path):
    os.makedirs(figure_path)


def get_parameter_A(percent):
    """Value from table 3"""
    if percent == PERCENT_90:
        A = 1.62
    elif percent == PERCENT_95:
        A = 1.60
    elif percent == PERCENT_99:
        A = 1.52

    return A


def get_parameter_B(percent):
    """Value from table 3"""
    if percent == PERCENT_90:
        B = 0.38
    elif percent == PERCENT_95:
        B = 0.40
    elif percent == PERCENT_99:
        B = 0.48

    return B


def get_parameter_k(percent):
    """Value from table 3"""
    if percent == PERCENT_90:
        k = 2.945
    elif percent == PERCENT_95:
        k = 33.2
    elif percent == PERCENT_99:
        k = 257.3

    return k


def get_factor_R(percent):
    if percent == PERCENT_90:
        R = 0.90
    elif percent == PERCENT_95:
        R = 0.95
    elif percent == PERCENT_99:
        R = 0.99

    return R


def get_beta_value(percent):
    if percent == PERCENT_90:
        beta = 1.06
    elif percent == PERCENT_95:
        beta = 1.11
    elif percent == PERCENT_99:
        beta = 1.10

    return beta


def compute_one_plus_H(t_l, percent, n=2):
    """Equation (30)
    If percent is 99, use equation (31) for t/lambda >= 1.0.
    """
    A = get_parameter_A(percent)
    B = get_parameter_B(percent)
    k = get_parameter_k(percent)

    value = A + B * np.exp(-k * np.power(t_l, n))
    if percent == PERCENT_99 and t_l >= 1.0:
        value = 1.52 + 2.42e-3 * t_l
    return value


def compute_theta_zero(Z, E_0):
    """Equation (17)"""
    theta_rad = 0.1167 * np.power(Z, 1.0 / 3.0) / np.sqrt(E_0)
    return theta_rad


def compute_theta_star(theta_zero, percent):
    """Equation (25)"""
    R = get_factor_R(percent)

    factor = np.sqrt(R / (1 - R))

    theta_star = factor * theta_zero
    return theta_star


def compute_theta_star_with_beta(theta_zero, percent):
    """Equation (28)"""
    R = get_factor_R(percent)
    beta = get_beta_value(percent)

    factor = np.sqrt(R / (1 - R))

    theta_star = beta * factor * theta_zero
    return theta_star


def compute_delta(theta_zero):
    """Equation (15)"""
    delta = theta_zero * theta_zero / 4.0
    return delta


def compute_lambda(A, rho, sigma):
    """Equation (13)"""
    mean_free_path = A / (N_A * rho * sigma)
    return mean_free_path


def compute_sigma(Z, E_0, delta):
    """Equation (27)"""
    factor1 = (Z * Z) / (E_0 * E_0)
    factor2 = 1.0 / (delta * (1.0 + delta))
    factor3 = (E_0 + 511.0) / (E_0 + 2.0 * 511.0)
    sigma_cm2 = 6.55e-20 * factor1 * factor2 * factor3 * factor3
    return sigma_cm2


def compute_b_nm(Z, A, rho, E_0, thickness_nm, percent):
    """Equation (12)"""
    theta_zero = compute_theta_zero(Z, E_0)

    # theta_star = compute_theta_star(theta_zero, percent)
    theta_star = compute_theta_star_with_beta(theta_zero, percent)

    delta = compute_delta(theta_zero)

    sigma = compute_sigma(Z, E_0, delta)

    lambda_cm = compute_lambda(A, rho, sigma)
    lambda_nm = lambda_cm * 1.0e7

    t_l = thickness_nm / lambda_nm
    one_plus_H = compute_one_plus_H(t_l, percent)

    b_nm = np.power(t_l, one_plus_H) * lambda_nm * theta_star
    return b_nm


def compute_goldstein_b_nm(Z, A, rho, E_0, thickness_nm, percent):
    """Equation (2)"""
    factor = np.sqrt(rho/A)
    thickness_cm = thickness_nm * 1.0e-7
    b_cm = 625.0 * Z / E_0 * factor * np.power(thickness_cm, 3.0/2.0)

    b_nm = b_cm * 1.0e7
    return b_nm


def compute_reimer_b_nm(Z, A, rho, E_0, thickness_nm, percent):
    """Equation (13) in Niels paper"""
    theta_zero = compute_theta_zero(Z, E_0)

    delta = compute_delta(theta_zero)

    sigma = compute_sigma(Z, E_0, delta)

    lambda_cm = compute_lambda(A, rho, sigma)
    lambda_nm = lambda_cm * 1.0e7

    a_H_m, unit, uncertainty = physical_constants["Bohr radius"]
    # print(unit)
    a_H_nm = a_H_m * 1.0e9
    factor1 = lambda_nm * lambda_nm / (2.0 * np.pi * a_H_nm)
    rho_1_nm3 = rho / 1.0e21
    factor2 = np.sqrt(N_A*rho_1_nm3 / (3.0 * np.pi * A))
    factor3 = Z * (1.0 + E_0 / 511.0)

    b_nm = factor1 * factor2 * factor3 * np.power(thickness_nm, 1.5)
    return b_nm


def compute_reimer2_b_nm(Z, A, rho, E_0, thickness_nm, percent):
    """Equation (13) in Niels paper"""
    E_0_eV = E_0 * 1.0e3
    factor1 = np.sqrt(rho / A)
    factor2 = Z / E_0_eV
    factor3 = (1.0 + E_0_eV / 511.0e3)/(1.0 + E_0_eV / (2.0 * 511.0e3))

    thickness_cm = thickness_nm * 1.0e-7
    b_cm = 1.05e5 * factor1 * factor2 * factor3 * np.power(thickness_cm, 3.0/2.0)
    b_nm = b_cm * 1.0e7
    return b_nm


def compute_t_l(Z, A, rho, E_0, thickness_nm):
    """Equation (12)"""
    theta_zero = compute_theta_zero(Z, E_0)

    delta = compute_delta(theta_zero)

    sigma = compute_sigma(Z, E_0, delta)

    lambda_cm = compute_lambda(A, rho, sigma)
    lambda_nm = lambda_cm * 1.0e7

    t_l = thickness_nm / lambda_nm
    return t_l


def create_figure_5():
    t_ls = np.logspace(np.log10(0.001), np.log10(10))

    one_plus_Hs_90 = [compute_one_plus_H(t_l, PERCENT_90) for t_l in t_ls]

    one_plus_Hs_95 = [compute_one_plus_H(t_l, PERCENT_95) for t_l in t_ls]

    one_plus_Hs_99 = [compute_one_plus_H(t_l, PERCENT_99) for t_l in t_ls]

    plt.figure()
    plt.semilogx(t_ls, one_plus_Hs_90, label="Mean 90%")
    plt.semilogx(t_ls, one_plus_Hs_95, label="Mean 95%")
    plt.semilogx(t_ls, one_plus_Hs_99, label="Mean 99%")

    plt.legend()
    plt.xlabel(r"$\frac{t}{\lambda}$")
    plt.ylabel(r"$1 + H$")

    plt.close()


def create_figure_6():
    t_ls = np.logspace(np.log10(0.001), np.log10(10))

    b_lts_90 = [np.power(t_l, compute_one_plus_H(t_l, PERCENT_90)) for t_l in t_ls]

    b_lts_95 = [np.power(t_l, compute_one_plus_H(t_l, PERCENT_95)) for t_l in t_ls]

    b_lts_99 = [np.power(t_l, compute_one_plus_H(t_l, PERCENT_99)) for t_l in t_ls]

    plt.figure()
    plt.loglog(t_ls, b_lts_90, label="Mean 90%")
    plt.loglog(t_ls, b_lts_95, label="Mean 95%")
    plt.loglog(t_ls, b_lts_99, label="Mean 99%")
    plt.xlabel(r"$\frac{t}{\lambda}$")
    plt.ylabel(r"$\frac{b}{\lambda \theta^{*}}$")

    plt.legend()

    plt.close()


def get_gauvin2016_fig5_al_data():
    data_file_path = get_current_module_path(__file__, '../../test_data/gauvin2016/gauvin2016_fig5.png_al_eq.dat')

    x_data = []
    y_data = []

    with open(data_file_path, 'r') as data_file:
        lines = data_file.readlines()

        for line in lines:
            items = line.split()

            if len(items) == 2:
                x_data.append(float(items[0]))
                y_data.append(float(items[1]))

    return x_data, y_data


def create_figure_9_al():
    # Al parameters
    A_al = 26.98
    rho_al = 2.69
    Z_al = 13

    thickness_nm = 80.0
    energies_keV = np.linspace(1.0, 100.0, 1000)
    bs_nm = [compute_b_nm(Z_al, A_al, rho_al, E_0, thickness_nm, PERCENT_90) for E_0 in energies_keV]

    plt.figure()

    x_data, y_data = get_gauvin2016_fig5_al_data()
    plt.semilogy(x_data, y_data, 'o', label='Gauvin (2016)')

    plt.semilogy(energies_keV, bs_nm, label='This script')

    plt.xlabel(r"$E_{0}$ (keV)")
    plt.ylabel("b (nm)")
    plt.legend()

    figure_file_path = os.path.join(figure_path, "figure_9_al.png")
    plt.savefig(figure_file_path)

    bs_nm = [compute_b_nm(Z_al, A_al, rho_al, E_0, thickness_nm, PERCENT_90) for E_0 in x_data]
    xi_square = np.sum(np.power(np.array(bs_nm) - np.array(y_data), 2))
    print("Xi2 = {}".format(xi_square))

    plt.close()


def create_dejonge_2017_figure_5():
    # Al parameters
    A_al = 26.98
    rho_al = 2.4
    Z_al = 13

    E_0 = 200.0
    thicknesses_nm = np.linspace(1.0, 600.0, 1000)
    thicknesses_um = thicknesses_nm*1.0e-3
    bs_nm = [compute_b_nm(Z_al, A_al, rho_al, E_0, thickness_nm, PERCENT_90) for thickness_nm in thicknesses_nm]
    t_ls = [compute_t_l(Z_al, A_al, rho_al, E_0, thickness_nm) for thickness_nm in thicknesses_nm]
    bgs_nm = [compute_goldstein_b_nm(Z_al, A_al, rho_al, E_0, thickness_nm, PERCENT_90) for thickness_nm in thicknesses_nm]
    brs_nm = [compute_reimer2_b_nm(Z_al, A_al, rho_al, E_0, thickness_nm, PERCENT_90) for thickness_nm in thicknesses_nm]

    plt.figure()
    plt.plot(thicknesses_um, bs_nm)

    plt.xlabel(r"z ($\mu$m)")
    plt.ylabel("b (nm)")

    plt.xlim((0.0, 0.6))
    plt.ylim(ymin=0.0)
    figure_file_path = os.path.join(figure_path, "dejonge_2017_figure_5.png")
    plt.savefig(figure_file_path)

    plt.xlim((0.0, 0.6))
    plt.ylim((0.0, 6))
    figure_file_path = os.path.join(figure_path, "dejonge_2017_figure_5_ymax6.png")
    plt.savefig(figure_file_path)

    plt.close()

    plt.figure()
    plt.plot(t_ls, bs_nm, label="Gauvin")
    plt.plot(t_ls, bgs_nm, label="Goldstein")
    plt.plot(t_ls, brs_nm, label="Reimer")

    plt.xlabel(r"t/$\lambda$")
    plt.ylabel("b (nm)")
    plt.legend()

    plt.ylim(ymin=0.0)
    figure_file_path = os.path.join(figure_path, "dejonge_2017_figure_5b.png")
    plt.savefig(figure_file_path)

    plt.ylim((0.0, 6))
    figure_file_path = os.path.join(figure_path, "dejonge_2017_figure_5b_ymax6.png")
    plt.savefig(figure_file_path)

    # plt.close()


def compute_sigma_beta(Z, lambda_cm, E_0_keV, beta_rad):
    theta0 = compute_theta_zero(Z, E_0_keV)

    factor1 = np.power(Z, 4.0/3.0) * lambda_cm * lambda_cm * np.power(1.0 + E_0_keV/511.0, 2) / np.pi
    factor2 = 1.0 / (1.0 + np.power(beta_rad / theta0, 2))

    sigma_cm = factor1 * factor2
    return sigma_cm


def wavelength_relativistic_electron_nm(energy_keV):
    energy_eV = energy_keV * 1.0e3
    h = 6.626e-34
    restEnergy_eV = 511.0e3
    resMass_kg = 9.109e-31
    charge_C = 1.602e-19
    nominator = h / np.sqrt(charge_C)

    denominator = np.sqrt(2.0 * resMass_kg * energy_eV * (1.0 + energy_eV / (2.0 * restEnergy_eV)))

    wavelength_m = nominator / denominator
    wavelength_nm = wavelength_m * 1.0e9

    return wavelength_nm


def niels_model():
    A_al = 26.98
    rho_al = 2.7
    Z_al = 13

    E_0 = 200.0
    beta_rad = 11.0e-3

    for beta_rad in [11.0e-3, 68.e-3]:
        lambda_nm = wavelength_relativistic_electron_nm(E_0)
        lambda_cm = lambda_nm*1.0e-7

        sigma_beta_cm = compute_sigma_beta(Z_al, lambda_cm, E_0, beta_rad)
        mean_free_path_cm = A_al / (sigma_beta_cm * rho_al * N_A)

        mean_free_path_um = mean_free_path_cm * 1.0e4
        print("mean_free_path_um for {} mrad: {}".format(beta_rad, mean_free_path_um))


if __name__ == '__main__':  # pragma: no cover
    # create_figure_5()
    # create_figure_6()
    # create_figure_9_al()
    # create_dejonge_2017_figure_5()

    niels_model()
    plt.show()

