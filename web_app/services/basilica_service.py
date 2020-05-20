#web_app/services/basilica_service.py

from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

connection = Connection(BASILICA_API_KEY)
print(type(connection))

if __name__ ==  "__main__":

    embeddings = connection.embed_sentences("HELLO_WORLD")
    print(embeddings)

    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]

    embeddings = list(connection.embed_sentences(sentences))
    for embed in embeddings:
        print("______________")
        print(embed)


