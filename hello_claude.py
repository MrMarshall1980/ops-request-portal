from dotenv import load_dotenv
import anthropic

load_dotenv()  # copies the key from .env into this program's environment

client = anthropic.Anthropic()  # finds ANTHROPIC_API_KEY by itself; the key never appears in code

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "In two sentences, what is Splunk ITSI?"}],
)

# The reply can hold several blocks; print only the text ones
for block in response.content:
    if block.type == "text":
        print(block.text)

# Every call reports its size in tokens, which is what you pay for
print(f"\nTokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out")