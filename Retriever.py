#File purpose: get a query and return the app file

import json
import numpy as np
import Embedder
import Parser

def load_json(file_path):
    vectors = []
    filenames = []
    chunks = []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        vectors.append(np.array(item["vector"]))
        filenames.append(item["filename"])
        chunks.append(item["chunk"])

    return vectors, filenames, chunks

def FindBest(vectors, filenames, chunks, query):
    length = len(filenames)
    queryVec = Embedder.embed(query)
    bestScore = Embedder.similarity(queryVec, vectors[0])
    bestIndex = 0
    for i in range(1, length):
        score = Embedder.similarity(queryVec, vectors[i])
        if score > bestScore:
            bestScore = score
            bestIndex = i
    return bestIndex

def extractText(vectors, filenames, chunks, index):
    FullText = Parser.DocToText(filenames[index])
    words = FullText.split()
    chunk_words = words[250*chunks[index]:250*(chunks[index]+1)]
    chunk_text = " ".join(chunk_words)
    return chunk_text

def search(query, DB= "ktqdmCptcsXM.json"):
    v,f,c = load_json(DB)
    q = query
    bi = FindBest(v,f,c,q)
    return f[bi], extractText(v,f,c,bi)
