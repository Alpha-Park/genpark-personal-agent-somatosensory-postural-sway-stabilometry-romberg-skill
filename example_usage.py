"""
Example usage of Somatosensory Postural Sway & Center of Pressure (COP) Stabilometry.
Demonstrates physiological stability vs sensory ataxia (positive Romberg) vs cerebellar vermian ataxia.
"""

from client import PosturalSwayStabilometryClient

def main():
    client = PosturalSwayStabilometryClient()

    print("=== Case 1: Healthy Adult Postural Stability ===")
    normal_case = client.evaluate_stabilometry(
        sway_area_eyes_open_mm2=110.0,
        sway_area_eyes_closed_mm2=195.0,
        sway_velocity_eyes_open_mm_s=8.0,
        sway_velocity_eyes_closed_mm_s=11.2
    )
    print("Stabilometry:")
    print(f"  Area EO:          {normal_case['stabilometric_kinetics']['sway_area_eyes_open_mm2']} mm2")
    print(f"  Area EC:          {normal_case['stabilometric_kinetics']['sway_area_eyes_closed_mm2']} mm2")
    print(f"  Romberg Quotient: {normal_case['stabilometric_kinetics']['romberg_quotient_area']}")
    print(f"  Classification:   {normal_case['clinical_postural_assessment']['balance_classification']}")

    print("\n=== Case 2: Sensory Ataxia (Positive Romberg / Large-Fiber Neuropathy) ===")
    sensory_case = client.evaluate_stabilometry(
        sway_area_eyes_open_mm2=160.0,
        sway_area_eyes_closed_mm2=640.0,
        sway_velocity_eyes_open_mm_s=10.5,
        sway_velocity_eyes_closed_mm_s=24.0
    )
    print("Stabilometry:")
    print(f"  Area EO:          {sensory_case['stabilometric_kinetics']['sway_area_eyes_open_mm2']} mm2")
    print(f"  Area EC:          {sensory_case['stabilometric_kinetics']['sway_area_eyes_closed_mm2']} mm2")
    print(f"  Romberg Quotient: {sensory_case['stabilometric_kinetics']['romberg_quotient_area']} (Marked eye closure destabilization)")
    print(f"  Classification:   {sensory_case['clinical_postural_assessment']['balance_classification']}")
    print(f"  Neuro-Pathology:  {sensory_case['clinical_postural_assessment']['neuroanatomical_interpretation']}")

if __name__ == "__main__":
    main()
