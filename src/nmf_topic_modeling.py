import numpy as np
from sklearn.decomposition import NMF

def nmf_topic_modeling(data, n_topics=10):
    """Perform NMF on gene expression data for topic modeling."""
    model = NMF(n_components=n_topics, init='random', random_state=0)
    W = model.fit_transform(data.X)  # Cell x Topic matrix
    H = model.components_            # Topic x Gene matrix
    return W, H
