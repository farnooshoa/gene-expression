import scanpy as sc

def load_data(file_path):
    """Load single-cell RNA-seq or ATAC-seq data."""
    data = sc.read_h5ad(file_path)
    return data

def preprocess_data(data):
    """Filter, normalize, and scale data."""
    sc.pp.filter_cells(data, min_genes=200)
    sc.pp.filter_genes(data, min_cells=3)
    sc.pp.normalize_total(data, target_sum=1e4)
    sc.pp.log1p(data)
    sc.pp.highly_variable_genes(data, min_mean=0.0125, max_mean=3, min_disp=0.5)
    data = data[:, data.var.highly_variable]
    sc.pp.scale(data, max_value=10)
    return data
