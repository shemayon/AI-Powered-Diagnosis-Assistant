from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from secret_key import openapi_key  


llm = OpenAI(temperature=0.5, openai_api_key=openapi_key)

def get_diagnosis(symptoms):
    """Generates a diagnosis based on the provided symptoms."""
    try:
        # Prompt template for diagnosis
        prompt_diagnosis = PromptTemplate(
            input_variables=['symptoms'],
            template="A patient presents the following symptoms: {symptoms}. What is a possible diagnosis?"
        )
        diagnosis_chain = LLMChain(llm=llm, prompt=prompt_diagnosis, output_key="diagnosis")

        # Generate diagnosis
        response = diagnosis_chain({"symptoms": symptoms})
        return response
    except Exception as e:
        return {"error": str(e)}

def get_treatment_plan(diagnosis):
    """Generates a treatment plan based on the diagnosis."""
    try:
        # Prompt template for treatment
        prompt_treatment = PromptTemplate(
            input_variables=['diagnosis'],
            template="Suggest a treatment plan for a patient diagnosed with {diagnosis}."
        )
        treatment_chain = LLMChain(llm=llm, prompt=prompt_treatment, output_key="treatment_plan")

        # Generate treatment plan
        response = treatment_chain({"diagnosis": diagnosis})
        return response["treatment_plan"]
    except Exception as e:
        return {"error": str(e)}
