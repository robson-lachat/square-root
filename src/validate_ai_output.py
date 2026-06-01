import sys
import os
import re
from difflib import unified_diff, SequenceMatcher
from google import genai
from google.genai.errors import APIError

def extract_numbers(text):
    """Helper function to extract the actual calculated result after the colon ':'."""
    if ":" in text:
        # Extract the part after the last colon to focus on the numeric result
        text_after_colon = text.split(":")[-1]
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", text_after_colon)
        return [float(n) for n in numbers] if numbers else []
    
    # If no colon is found, attempt to extract any numbers from the entire text as a fallback
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    return [float(n) for n in numbers] if numbers else []

def get_ai_recommendation(old_text, new_text):
    """Asks Gemini to audit the changes. Returns None if API fails."""
    if "GEMINI_API_KEY" not in os.environ or not os.environ["GEMINI_API_KEY"]:
        return None
    
    try:
        client = genai.Client()
        prompt = f"""
        You are a QA Automation Expert auditing an engineering regression test.
        Compare the following two outputs from a software application:
        
        [Baseline Reference]: "{old_text}"
        [Current New Output]: "{new_text}"
        
        Provide a strict technical evaluation in English including:
        1. Semantic Acceptance Score: (0% to 100%).
        2. Final Verdict: (APPROVED or REJECTED).
        3. A one-sentence technical justification explaining why.
        """
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        # Silently fail here to trigger the fallback logic gracefully
        return None

def validate_ai_triple_check(current_file, reference_file):
    print("\n[Robson's Advanced AI Validator] Starting TRIPLE-CHECK Integration...")

    if not os.path.exists(current_file) or not os.path.exists(reference_file):
        print(f"❌ Error: Missing files. Ensure both current output and reference baseline exist.")
        sys.exit(1)

    with open(reference_file, 'r', encoding='utf-8') as f_ref, open(current_file, 'r', encoding='utf-8') as f_cur:
        ref_text = f_ref.read().strip()
        current_text = f_cur.read().strip()

    # PHASE 1: Deterministic Check (100% Match)
    if ref_text == current_text:
        print("✅ LAYER 1 (Deterministic Check): 100% Exact match. No drift detected.")
        sys.exit(0)

    print("⚠️  Notice: Output Variation Detected. Activating Multi-Layer Validation.")

    # PHASE 2: Algorithmic Fuzzy Matching
    similarity_ratio = SequenceMatcher(None, ref_text, current_text).ratio()
    print(f"\n📊 LAYER 2 (Fuzzy Character Similarity Rate): {similarity_ratio:.2%}")

    # Print Text Diff
    print("\n------------------ DETECTED TEXT DIFFERENCES (DIFF) ------------------")
    ref_lines = ref_text.splitlines()
    cur_lines = current_text.splitlines()
    diff = list(unified_diff(ref_lines, cur_lines, fromfile='Baseline (Old)', tofile='Current (New)', lineterm=''))
    if diff:
        for line in diff:
            print(line)
    print("----------------------------------------------------------------------")

    # PHASE 3: AI Semantic Audit with Local Fallback
    print("\n🤖 LAYER 3 (Semantic Audit & Verification Layer):")
    ai_report = get_ai_recommendation(ref_text, current_text)
    
    if ai_report:
        print(ai_report)
    else:
        print("⚠️  [API Quota/Network Alert] Google API is unavailable (Rate Limit / 429 / 503).")
        print("🔄 Activating Local Deterministic Fallback Engine (Regex Math Auditing)...")
        
        # Local fallback parsing logic
        ref_nums = extract_numbers(ref_text)
        cur_nums = extract_numbers(current_text)
        
        if ref_nums and cur_nums:
            # Check if the primary numbers are close mathematically (e.g., 1.41 vs 1.414214)
            diff_pct = abs(ref_nums[0] - cur_nums[0])
            if diff_pct < 0.05:  # Tolerance limit for float precision drift
                print(f"✅ Fallback Verdict: APPROVED (Local Engine)")
                print(f"   Justification: Mathematical values ({ref_nums[0]} vs {cur_nums[0]}) are within acceptable precision bounds.")
            else:
                print(f"❌ Fallback Verdict: REJECTED (Local Engine)")
                print(f"   Justification: Numeric divergence too high ({ref_nums[0]} vs {cur_nums[0]}).")
        else:
            print("❌ Fallback Verdict: REJECTED")
            print("   Justification: Unable to parse numeric values locally to validate the drift.")
            
    print("----------------------------------------------------------------------")

    # PHASE 4: Human-in-the-Loop Decision
    print("\n💡 LAYER 4 (HUMAN-IN-THE-LOOP FINAL DECISION REQUIRED):")
    print("Review the algorithmic Fuzzy Match and the Verification Report above.")
    print("")
    print("👉 IF YOU APPROVE THE CHANGE: Run 'make outref-math' (or 'make outref-ai') to update the baseline.")
    print("👉 IF YOU REJECT THE CHANGE : Discard it and investigate the model/data drift.")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_ai_output.py <current_file> <reference_file>")
        sys.exit(1)
    validate_ai_triple_check(sys.argv[1], sys.argv[2])