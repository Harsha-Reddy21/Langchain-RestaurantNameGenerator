from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv()
import os

os.environ['OPEN_AI_KEY']=os.getenv('OPENAI_APIKEY')

llm=OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):

    prompt_template_name=PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest a fancy name for this'
    )

    name_chain=LLMChain(llm=llm,promt=prompt_template_name,output_key='restaurant_name')

    
    prompt_template_items=PromptTemplate(
        input_variables=['restaurant_name'],
        template='Suggest some menu items for {restaurant_name}. Return it as a comma separed string'

    )

    food_items_chain=LLMChain(llm=llm, promt=prompt_template_items,output_key='menu_items')

    chain=SequentialChain(
        chains=[name_chain,food_items_chain],
        input_varibles=['cuisine'],
        output_varibles=['restaurant_name','menu_items']
    )

    response=chain({'cuisine':cuisine})

    return response

