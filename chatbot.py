import subprocess

def generate_response(prompt):
    try:
        # Call the Ollama CLI to generate a response
        result = subprocess.run(
            ['ollama', 'run', 'llama3:latest', prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False  # Important to set shell=False to avoid security issues
        )
        response = result.stdout.decode('utf-8').strip()
        error = result.stderr.decode('utf-8').strip()

        if error:
            print(f"Error: {error}")
        
        return response
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to the Chatbot! Type 'exit' or 'quit' to end the conversation.")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        response = generate_response(prompt)
        print(f"Bot: {response}")
