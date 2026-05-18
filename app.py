from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Caesar Cipher Function
def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


# Brute Force Function
def brute_force(text):
    results = []
    for shift in range(26):
        decrypted = caesar_cipher(text, shift, "decrypt")
        results.append(f"Shift {shift}: {decrypted}")
    return results


@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    brute_results = []

    if request.method == "POST":
        text = request.form["text"]
        mode = request.form["mode"]

        # ONLY take shift if needed
        if mode == "bruteforce":
            brute_results = brute_force(text)
        else:
            try:
                shift = int(request.form["shift"])
            except:
                shift = 0

            output = caesar_cipher(text, shift, mode)

    return render_template("index.html", output=output, brute_results=brute_results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)