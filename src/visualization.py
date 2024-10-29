import scanpy as sc
import matplotlib.pyplot as plt

def plot_umap(data, color='disease_state'):
    """Visualize data in UMAP space colored by specified metadata."""
    sc.pp.neighbors(data)
    sc.tl.umap(data)
    sc.pl.umap(data, color=color)
    plt.show()

def plot_topic_gene_loadings(H, gene_names, n_genes=10):
    """Plot top gene loadings for each topic."""
    for i, topic in enumerate(H):
        top_genes = np.argsort(topic)[-n_genes:]
        top_gene_names = [gene_names[j] for j in top_genes]
        plt.barh(top_gene_names, topic[top_genes])
        plt.xlabel("Gene Loading")
        plt.title(f"Topic {i+1}")
        plt.show()
