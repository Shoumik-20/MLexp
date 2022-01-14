import json
from Get_statistics import get_statistics

def main(filename):
    with open(filename) as f :
        data = json.load(f)
    input_list = data["input"]["input_list"]
    output = get_statistics(input_list)
    print("Model output", output)
    print("Expected output", data["output"])

if __name__ == "__main__":
    fn = "Testcase1.json"
    main(fn)