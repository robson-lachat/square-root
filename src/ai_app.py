import os
import sys
from google import genai
from google.genai.errors import APIError

def generate_ai_analysis():
    # Verify if the API key is configured in the environment
    if "GEMINI_API_KEY" not in os.environ or not os.environ["GEMINI_API_KEY"]:
        print("Error: GEMINI_API_KEY not configured in environment.", file=sys.stderr)
        sys.exit(1)

    # Initialize the official GenAI client
    client = genai.Client()
    
    # Simple prompt to test non-deterministic output variations
    prompt = "Explain in one short sentence what a regression test is."
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        print(response.text.strip())
        
    except APIError as e:
        # Captures specific Google API errors (like 503 Service Unavailable, 429 Rate Limit, etc.)
        print(f"\n❌ [Google API Error] Connection failed (Status Code: {e.code}).", file=sys.stderr)
        print(f"Details: {e.message}", file=sys.stderr)
        print("Recommendation: Google servers might be busy. Please wait a moment and try again.", file=sys.stderr)
        sys.exit(1)
        
    except Exception as e:
        # Captures any other unexpected errors (like network drop)
        print(f"\n❌ [Unexpected Error] An error occurred while contacting the AI model: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_ai_analysis()