import os, sys
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from custom_exceptions.exceptions import TripPlannerExceptions

class ModelLoader:
    """
    class for loading the llm models
    """
    def __init__(self):
        load_dotenv()
        print("Loading config...")
        self.config = load_config()
        self.model_provider: Literal["openai", "groq"] = "groq"

    def load__llm(self):
        """
        load and return the llm
        """
        try:
            print("Loading llm.....")
            if self.model_provider == "groq":
                print("Loading LLM from groq...")
                groq_api_key = os.getenv("GROQ_API_KEY")
                model_name = self.config['llm']['groq']['model_name']
                llm = ChatGroq(model = model_name, groq_api_key = groq_api_key)

            elif self.model_provider == "openai":
                print("Loading LLM from openai...")
                openai_api_key = os.getenv("OPENAI_API_KEY")
                model_name = self.config['llm']['openai']['model_name']
                llm = ChatOpenAI(model = model_name, openai_api_key = openai_api_key)
            return llm
        
        except Exception as e:
            raise TripPlannerExceptions(e, sys)
        
if __name__ == "__main__":
    loader = ModelLoader()
    loader.load__llm()
