data2["Customer Review"] = data2["Customer Review"].apply(lambda x:" ".join(token for token in x))