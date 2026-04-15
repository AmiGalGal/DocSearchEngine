DocSearchEngine
light weight local documents search engine, Index the documents once and you find them forever
run completely on the local machine without any API calls or usage of any LLM

Convert the documents in your directory into high-dimensional vectors (384 to be exact) and store those vectors
when you have a query you simply describe in a general sense what in the file you wanted and it compares it to the rest of the files in chunks of 250 words, it produces a sorted list of the fits
and presents the files ranked by similarity.

support docx, pdf, txt and md
finds the K best results
simple GUI built in tkinter
