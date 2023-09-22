from dataclasses import dataclass


@dataclass(frozen=True)
class AcqPars:
    data: str
    time: str
    scan_time: str
    img_time: str
    exp_type: str
    img_type: str
    orient: str
    points: int
    alpha_no: int
    beta_no: int
    gamma_no: int
    first_alpha: float
    max_gamma: float
    gradient: float
    sweep: float
    center_field: float
    mod_amp: float
    mod_freq: float
    power: float
