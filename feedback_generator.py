from langchain.chains import SimpleChain
from langchain.llms import OpenAI

def generate_feedback(profile_data):
    """
    Uses the OpenAI model to generate feedback for the given LinkedIn profile data.
    Returns a dictionary with feedback for each section.
    """
    llm = OpenAI(api_key='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')  
    chain = SimpleChain(llm)  # Create a simple chain for processing requests
    
    feedback = {}
    # Loop through each section of the profile and generate feedback
    for section, content in profile_data.items():
        feedback[section] = chain.run(f"Provide constructive feedback and improvements for the following section: {content}")
    
    return feedback  # Return the feedback for each section

def generate_improved_content(profile_data):
    """
    Uses the OpenAI model to generate improved and reworded text for each LinkedIn profile section.
    Returns a dictionary with the improved content for each section.
    """
    llm = OpenAI(api_key='your-openai-api-key')  # Initialize the LLM (e.g., GPT)
    chain = SimpleChain(llm)  # Create a simple chain for processing requests
    
    improved_content = {}
    # Loop through each section of the profile and generate improved content
    for section, content in profile_data.items():
        improved_content[section] = chain.run(f"Rewrite and enhance the following section: {content}")
    
    return improved_content  # Return the improved content for each section
