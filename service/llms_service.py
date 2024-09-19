from vllm import LLM, SamplingParams
from sentence_transformers import SentenceTransformer
from openai import OpenAI
class OpenAIClient:
    """
    OpenAI client
    """
    def __init__(self):
        self.api_key = "123456"
        self.base_url = "http://localhost:8000/v1"
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.models = self.client.models.list()
        self.model = self.models.data[0].id

    def get_standard_response(self, system_content, user_content):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
        )
        return completion.choices[0].message.content

    
class sbert_Service:
    def __init__(self, model_path):
        self.sbert_model = SentenceTransformer(model_path)
    def encode(self, texts):
        embeddings = self.sbert_model.encode(texts)
        return embeddings

if __name__ == '__main__':
    client = OpenAIClient()
    system_content = "你是 AI 人工智能助手"
    user_content = "介绍一下四川的美食"
    standard_response = client.get_standard_response(system_content, user_content)
    # streaming_response = client.get_streaming_response(system_content, user_content)
    print(standard_response)


# if __name__ == '__main__':
#     model_path = 'models/raw_model/bge-large'
#     sbert_service = sbert_Service(model_path)
#     texts = ["22的二次方是多少！"]
#     embeddings = sbert_service.encode(texts)
#     print(embeddings.shape)