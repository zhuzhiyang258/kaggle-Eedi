from vllm import LLM, SamplingParams
from sentence_transformers import SentenceTransformer
class LLM_vllm_Service:
    def __init__(self, model_path, tensor_parallel_size=1):
        self.llm = LLM(model_path, tensor_parallel_size=tensor_parallel_size)
        self.sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
    def generate(self, prompts, sampling_params):
        outputs = self.llm.generate(prompts, sampling_params)
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            return generated_text

    
class sbert_Service:
    def __init__(self, model_path):
        self.sbert_model = SentenceTransformer(model_path)
    def encode(self, texts):
        embeddings = self.sbert_model.encode(texts)
        return embeddings

if __name__ == '__main__':
    model_path = 'models/raw_model/llama2-13b-math'
    tensor_parallel_size = 2
    llm_service = LLM_vllm_Service(model_path)
    question = ["22的二次方是多少！"]
    answer = llm_service.generate(question, llm_service.sampling_params)
    print(answer)


# if __name__ == '__main__':
#     model_path = 'models/raw_model/bge-large'
#     sbert_service = sbert_Service(model_path)
#     texts = ["22的二次方是多少！"]
#     embeddings = sbert_service.encode(texts)
#     print(embeddings.shape)