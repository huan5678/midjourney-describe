import re
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    input_string = data.get('input_string', '')
    prefix = data.get('prefix', '')
    ar = data.get('ar', '')
    final_string = process_string(input_string, prefix, ar)
    return final_string

def process_string(input_string, prefix, ar):
    print('ar =', type(ar), ar , ar == None)
    input_string = re.sub(r'\d️⃣', '', input_string)
    ar_in_input = False
    ar_match = re.search(r'--ar (\d+:\d+)', input_string)
    if ar_match:
        ar_in_input = True

    if ar is None or ar == "":
        if ar_in_input:
            ar = ar_match.group(1)
        else:
            ar = ""

    input_string = input_string.replace(',', r'\,')
    input_string = re.sub(r'--ar \d+:\d+', ',', input_string)
    input_string = re.sub(r'\n+', '\n', input_string).strip()
    lines = input_string.split('\n')
    joined_lines = ','.join(lines).rstrip(',')
    joined_lines = re.sub(r',,', ',', joined_lines)

    final_string = f'{{{joined_lines}}}'
    if ar != "":
        final_string += f' --ar {ar}'
    final_string += f' --{{{prefix}}}'
    # Remove consecutive commas
    final_string = re.sub(r'( ,)+', ',', final_string)
    return final_string

if __name__ == "__main__":
    app.run(debug=True)
