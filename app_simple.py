import hashlib

def generate_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()

def verify_hash(text, hash):
    new_hash = generate_hash(text)
    return new_hash == hash

input_text = "API_SIMULADOR_HIBRIDA"
generated_hash = generate_hash(input_text)

print(f'Text inputed: {input_text}')
print(f'Generated hash: {generated_hash}')

incorrect_input_text = "Input text incorrect."
verify_result = verify_hash(incorrect_input_text, generated_hash)

if verify_result:
    print("The hash matches the text.")
else:
    print("The hash does not match the text.")
