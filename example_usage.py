from client import OpenRouterMultiProviderTestClient
client = OpenRouterMultiProviderTestClient()
print(client.run_tests("What is gravity?", ["openai/gpt-4o", "anthropic/claude-3-haiku"]))