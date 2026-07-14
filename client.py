class OpenRouterMultiProviderTestClient:
    def run_tests(self, test_prompt: str, target_models: list[str]) -> dict:
        return {"results_map": {m: f"Simulated reply to {test_prompt}" for m in target_models}}