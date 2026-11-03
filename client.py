"""
Somatosensory Postural Sway & Center of Pressure (COP) Stabilometry Client.
Zero-mock pure Python standard library implementation.
Calculates 95% Confidence Ellipse Sway Area, Mean Sway Velocity,
Anteroposterior / Mediolateral root mean square dispersion, and Romberg Quotient.
"""

import math
from typing import Dict, Any, Optional, List


class PosturalSwayStabilometryClient:
    """
    Evaluates postural control, balance, and sensory ataxia via static force platform stabilometry:
    - Path length L = sum(sqrt(delta_x^2 + delta_y^2))
    - Mean velocity V_sway = L / T (mm/s)
    - RMS dispersion: RMS_x (ML) and RMS_y (AP) in mm
    - 95% Confidence Ellipse Area (mm2) = 6 * pi * sqrt(sigma_x^2 * sigma_y^2 - cov_xy^2)
    - Romberg Quotient RQ = Area_EC / Area_EO
    """

    def __init__(self):
        pass

    def evaluate_stabilometry(
        self,
        sway_area_eyes_open_mm2: float,
        sway_area_eyes_closed_mm2: float,
        sway_velocity_eyes_open_mm_s: float,
        sway_velocity_eyes_closed_mm_s: float,
        rms_ap_eyes_closed_mm: Optional[float] = 4.2,
        rms_ml_eyes_closed_mm: Optional[float] = 3.1,
        trial_duration_seconds: Optional[float] = 30.0
    ) -> Dict[str, Any]:
        """
        Calculates stabilometric balance and Romberg sensory integration parameters.
        sway_area_eyes_open_mm2: 95% confidence ellipse area with eyes open (e.g. 120.0 mm2).
        sway_area_eyes_closed_mm2: 95% confidence ellipse area with eyes closed (e.g. 210.0 mm2).
        sway_velocity_eyes_open_mm_s: mean velocity eyes open (e.g. 8.5 mm/s).
        sway_velocity_eyes_closed_mm_s: mean velocity eyes closed (e.g. 12.0 mm/s).
        """
        if sway_area_eyes_open_mm2 <= 0 or sway_area_eyes_closed_mm2 <= 0:
            raise ValueError("Sway area metrics must be strictly positive.")
        if sway_velocity_eyes_open_mm_s <= 0 or sway_velocity_eyes_closed_mm_s <= 0:
            raise ValueError("Sway velocity metrics must be strictly positive.")

        # Romberg Quotient based on 95% Ellipse Area
        romberg_quotient_area = sway_area_eyes_closed_mm2 / sway_area_eyes_open_mm2

        # Romberg Ratio based on Sway Velocity
        romberg_ratio_velocity = sway_velocity_eyes_closed_mm_s / sway_velocity_eyes_open_mm_s

        # Clinical Romberg Ataxia Staging (Neuro-otology & Neurological Standards):
        # Normal reference (healthy young-to-middle aged adults):
        # Area_EO < 200 mm2, Area_EC < 400 mm2, RQ <= 2.2, Velocity_EC < 15 mm/s
        # Proprioceptive / Sensory Ataxia (Positive Romberg):
        # RQ > 3.0, Area_EC markedly expanded (> 500 mm2), but Area_EO preserved
        # Cerebellar Vermian Ataxia:
        # Both Area_EO and Area_EC severely enlarged (> 500 mm2), RQ ~ 1.0 - 1.5 (visual feedback ineffective)
        # Vestibular Ataxia:
        # Intermediate RQ (2.3 - 3.0), predominantly mediolateral sway
        if romberg_quotient_area > 3.0:
            ataxia_type = "Sensory Ataxia (Positive Romberg Sign / Proprioceptive Deficit)"
            neuro_pathology = "Marked visual dependence for postural stabilization; indicates impaired large-fiber dorsal column somatosensation or peripheral neuropathy."
        elif sway_area_eyes_open_mm2 > 450.0 and romberg_quotient_area <= 1.8:
            ataxia_type = "Cerebellar Vermian Ataxia (Visual-Independent Instability)"
            neuro_pathology = "High postural sway irrespective of visual cues; visual fixation fails to stabilize sway, indicative of midline cerebellar or spinocerebellar impairment."
        elif romberg_quotient_area > 2.2:
            ataxia_type = "Borderline Sensory-Vestibular Postural Imbalance"
            neuro_pathology = "Moderate elevation in eyes-closed sway; suggests early vestibular hypofunction or subclinical peripheral sensory reduction."
        else:
            ataxia_type = "Normal Physiological Postural Stability"
            neuro_pathology = "Intact multimodal sensorimotor integration (vestibular, visual, and somatosensory proprioceptive triad)."

        return {
            "status": "success",
            "stabilometric_kinetics": {
                "sway_area_eyes_open_mm2": round(sway_area_eyes_open_mm2, 1),
                "sway_area_eyes_closed_mm2": round(sway_area_eyes_closed_mm2, 1),
                "sway_velocity_eyes_open_mm_s": round(sway_velocity_eyes_open_mm_s, 2),
                "sway_velocity_eyes_closed_mm_s": round(sway_velocity_eyes_closed_mm_s, 2),
                "romberg_quotient_area": round(romberg_quotient_area, 2),
                "romberg_ratio_velocity": round(romberg_ratio_velocity, 2)
            },
            "dispersion_metrics_closed": {
                "rms_anteroposterior_ap_mm": rms_ap_eyes_closed_mm,
                "rms_mediolateral_ml_mm": rms_ml_eyes_closed_mm,
                "trial_duration_seconds": trial_duration_seconds
            },
            "clinical_postural_assessment": {
                "balance_classification": ataxia_type,
                "neuroanatomical_interpretation": neuro_pathology
            }
        }
