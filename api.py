import paralleldots
paralleldots.set_api_key('cFq6WhLHBPX2ltxngt8G53vfnAYw1aCjSpbnJ5rDNZs')

def ner(text):
    ner=paralleldots.ner(text)
    return ner

