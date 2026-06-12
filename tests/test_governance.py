import sys
import os
import traceback
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from governance_engine.zkml_pipeline_verifier import ZKMLPipelineVerifier
from governance_engine.asa_drift_monitor import ASADriftMonitor
from governance_engine.gsri_scoring_engine import GSRIScoringEngine
from governance_engine.pqc_worm_logger import PQCWORMLogger
from governance_engine.omega_actual_switch import OmegaActualSwitch

def test_governance_integration():
    print("Starting Governance Engine Integration Test...")

    # 1. Initialize Components
    verifier = ZKMLPipelineVerifier(fairness_threshold=0.11)
    monitor = ASADriftMonitor()
    scoring = GSRIScoringEngine()
    logger = PQCWORMLogger(log_file="tests/test_audit.jsonl")
    switch = OmegaActualSwitch()

    # 2. MAS FEAT: Fairness Verification
    selection_data = {
        "counts": {"minority": 45, "majority": 55},
        "sizes": {"minority": 100, "majority": 100}
    }
    proof = verifier.generate_zk_fairness_proof("node_01", selection_data)
    if not proof['is_fair']:
        raise Exception("Fairness check failed")
    logger.commit_audit_log("FAIRNESS_VERIFIED", proof)
    print("✔ MAS FEAT ZK-Fairness Proof Generated")

    # 3. HKMA Ethics: Interpretability (CAE)
    cae_id = monitor.create_contextual_attribution_envelope("loan_agent", {"income": 100000})
    monitor.append_attribution_hop(cae_id, "credit_expert", "HASH_X1")
    monitor.append_attribution_hop(cae_id, "risk_expert", "HASH_Y2")
    final_audit = monitor.finalize_cae(cae_id, "APPROVED")
    if len(final_audit['attribution_lineage']) != 2:
        raise Exception(f"Expected 2 hops, got {len(final_audit['attribution_lineage'])}")
    logger.commit_audit_log("CAE_FINALIZED", {"cae_id": cae_id, "decision": "APPROVED"})
    print("✔ HKMA CAE Interpretability Layer Verified")

    # 4. Maturity Scoring
    compliance_metrics = {
        "fairness": 90,
        "interpretability": 85,
        "immutability": 95,
        "containment": 100
    }
    score = scoring.calculate_ethics_maturity_score(compliance_metrics)
    level = scoring.get_maturity_level(score)
    if level < 3:
        raise Exception(f"Maturity level too low: {level}")
    print(f"✔ Ethics Maturity Score: {score} (Level {level})")

    # 5. Omega Actual Switch
    if not switch.check_system_state():
        raise Exception("System should be operational initially")
    switch.trigger_containment("Test Breach")
    if switch.check_system_state():
        raise Exception("System should be isolated after trigger")
    print("✔ Omega Actual Containment Verified")

    print("\nGovernance Engine Integration Test: PASS")

if __name__ == "__main__":
    try:
        test_governance_integration()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
