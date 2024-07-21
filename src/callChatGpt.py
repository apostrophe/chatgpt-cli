import argparse
from openai import OpenAI
import shutil

def draw_horizontal_line():
    # Get the terminal size
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    
    # Create the horizontal line
    line = '-' * width
    
    print(line)


def main():
    parser = argparse.ArgumentParser(description="Get chat completion from OpenAI")
    parser.add_argument("content", type=str, help="The content to send to the model")
    args = parser.parse_args()

    client = OpenAI()
    
    additionalRequest = ", please format the response in plain text"

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": args.content+additionalRequest}],
        stream=True,
    )

    #print("---------------------------------------------------------")
    draw_horizontal_line()
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    
    # make sure there's an extra line in the terminal        
    print()
    #print("---------------------------------------------------------")
    draw_horizontal_line()
    
if __name__ == "__main__":
    main()
