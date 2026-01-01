from icp.inference_control_plane import InferenceControlPlane
from icp.types import Signal, Noise

# --- ICP Initialization ---
icp = InferenceControlPlane(config_path="config/charter.json")

# --- Test Prompts ---
prompts = [
    "The future of AI control and inference stabilization is critical.",
    "Large language models can drift if left unchecked during inference.",
    "Entropy control prevents hallucinations and improves coherence."
]

# --- Helper: Sampling-Only Simulation ---
def sampling_only_inference(prompt: str) -> str:
    # Simplified simulation: returns prompt with mutation to mimic open-loop drift
    return prompt + " (sampled)"

# --- Main Execution Loop ---
for idx, prompt in enumerate(prompts, start=1):
    print(f"\n--- Prompt {idx} ---")
    print(f"Input: {prompt}")

    # 1. ICP Inference
    icp_output = icp.run(prompt)
    if icp_output:
        print(f"\nICP Output:\n{icp_output}")
    else:
        print("\nICP Output: Dampened due to low SNR or instability.")

    # Telemetry Placeholder (In live integration, fetch this from ObserverCore)
    print("Telemetry: [SNR: 1.0 | Error: 0.0 | Signal Power: 128]")

    # 2. Sampling-Only Inference
    sampled_output = sampling_only_inference(prompt)
    print(f"\nSampling-only Output:\n{sampled_output}")

print("\n✅ ICP pipeline demonstration complete.")
print("Use 'benchmarks/benchmark.py' to generate CSV and graphs for deeper comparison.")