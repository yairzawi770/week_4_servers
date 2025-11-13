import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def get_data():
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def get_name(name):
    with open("names.txt", "a") as f:
        f.write(name)
    return {"msg": "saved user"}


@app.post("/caesar/encrypt")
def encrypted_caesar(text: str, offset: int, mode: str):
    sentance = text
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    offset = offset
    cipher = ''

    for c in sentance:
        if c in alphabet:
            cipher += alphabet[(alphabet.index(c) + offset) % (len(alphabet))]
    return {"encrypted_text": "..." + cipher}


@app.post("/caesar/decrypt")
def decrypted_caesar(text: str, offset: int, mode: str):
    sentance = text
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    offset = offset
    cipher = ''

    for c in sentance:
        if c in alphabet:
            cipher += alphabet[(alphabet.index(c) - offset) % (len(alphabet))]
    return {"encrypted_text": "..." + cipher}


@app.get("/fence/encrypt")
def fence_encrypt(text: str):
    phrase = text
    odd = ''
    even = ''

    for i, ch in enumerate(phrase):
        if i % 2 == 0:
            even += ch
        else:
            odd += ch
    ciphertext = even + odd

    return {"encrypted_text": "..." + ciphertext}


@app.post("/fence/decrypt")
def fence_decrypt(text: str):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=40)
