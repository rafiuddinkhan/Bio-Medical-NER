import datetime
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from dotenv import load_dotenv


load_dotenv('.env')

class BioMedicalParser:
    def __init__(self):
        self.load_model()
        self.parser()
    
    def load_model(self):
        current_date = datetime.datetime.now().date()
        target_date = datetime.date(2024, 6, 12)
        if current_date > target_date:
            self.llm_model = "gpt-3.5-turbo"
        else:
            self.llm_model = "gpt-3.5-turbo-0301"
        self.chat = ChatOpenAI(temperature=0.0, model=self.llm_model)

    def parser(self):
        symptoms_schema = ResponseSchema(name="symptoms",
                             description="extract symptoms from text")
        duration_schema = ResponseSchema(name="duration",
                                            description="extract duration from text")
        disease_schema = ResponseSchema(name="disease",
                                            description="extract disease form text")
        medication_schema = ResponseSchema(name="medication",
                                            description="Extract medication from text")

        medical_test_schema = ResponseSchema(name="medical_test",
                                            description="Extract medical test from text")

        response_schemas = [symptoms_schema,
                            duration_schema,
                            disease_schema,
                            medication_schema,
                            medical_test_schema
                            ]
        self.output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

        self.format_instructions = self.output_parser.get_format_instructions()

        bio_medical_ner_template = """\
        Ignore all the previous instruction. Now For the following text, extract the following information:

        symptoms: extract the symptoms from the text
        output them as Python list, if not available return []

        duration: extract the duration from the text
        output them as Python list, if not available return []

        disease: extract diseases from the text
        output them as Python list, if not available return []

        medication: extract medication from the text
        output them as Python list and if not available return []

        medical_test_schema: extract medical test from the text
        output them as Python list and if not available return []

        Format the output as JSON with the following keys:
        symptoms
        duration
        disease
        medication
        medical_test

        text: {text}
        {format_instructions}
        """
        self.prompt = ChatPromptTemplate.from_template(template=bio_medical_ner_template)


    def extract_biomedical_entities(self, input_text):
    
        messages = self.format_messages(input_text)
        response = self.chat(messages)
        output_dict = self.output_parser.parse(response.content)
        return output_dict

    def format_messages(self, text):

        
        messages = self.prompt.format_messages(text=text,
                                format_instructions=self.format_instructions)
        return messages

 

if __name__ == "__main__":
    bio_medical_parser = BioMedicalParser()

    input_text = " i have fever and headache for 2 days"
    result = bio_medical_parser.extract_biomedical_entities(input_text)
    print(result)
