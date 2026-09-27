from strands.models.ollama import OllamaModel


def get_qwen_4b():
    return OllamaModel(
        host="http://localhost:11434",
        model_id="qwen3:4b",
    )