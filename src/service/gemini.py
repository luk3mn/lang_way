import google.generativeai as genai
from src.data.param import A1,A2,B1,B2,C1,C2

class Gemini:
    __GOOGLE_API_KEY: str
    __response: genai.GenerativeModel
    __context: str
    __generation_config: object = {
        "candidate_count": 1,
        "temperature": 0.7
    }
    __safety_settings: object = {
        "HARASSMENT": "BLOCK_NONE",
        "HATE": "BLOCK_NONE",
        "SEXUAL": "BLOCK_NONE",
        "DANGEROUS": "BLOCK_NONE" 
    }

    def __init__(self, GOOGLE_API_KEI: str) -> None:
        self.__GOOGLE_API_KEY = GOOGLE_API_KEI

    def __model_fit(self, model_name: str) -> genai.GenerativeModel:
        genai.configure(api_key=self.__GOOGLE_API_KEY)

        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=self.__generation_config,
            safety_settings=self.__safety_settings
        )

        return model

    
    def generate(self, input: str, language: str, model_name: str = "gemini-1.0-pro"):
        
        params = [A1,A2,B1,B2,C1,C2]

        self.__context = """
            vou fornecer um texto em {} que redigi. Por favor, analise-o minuciosamente, aplicando o Quadro Europeu Comum de Referência para Línguas (CEFR) para 
            determinar meu atual nível de proficiência no idioma. Solicito que leve em conta aspectos como gramática, vocabulário e expressões utilizadas no texto.

            Após a análise, destaque as áreas que exigem correção e forneça orientações específicas sobre o que devo estudar para progredir para o próximo nível, 
            com base na avaliação atual.

            Para facilitar a compreensão, sugiro a organização das informações em tópicos. Além disso, gostaria de receber uma estimativa do total de palavras que 
            conheço com base no texto fornecido.

            Por fim, seria muito útil receber um plano de estudo detalhado, incluindo uma rotina recomendada, para alcançar o próximo nível de proficiência no idioma.
            
            Utilize o Quadro Europeu Comum de Referência para Línguas como forma de medir a proedificência: {}

            O texto escrito por mim será esse: "{}"
        """.format(language, params, input)

        model = self.__model_fit(model_name)
        self.__response = model.generate_content(contents=self.__context)
        
        return self.__response.text
