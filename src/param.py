"""
Data Pipeline Configuration Script.
"""
from pathlib import Path

class Params:
    random_state=42,
    assets_path = Path('./som_assets')
    original = assets_path / 'som_original' / 'data.xlsx'
    data = assets_path / 'som_data'
    features = assets_path / 'som_features'
    models = assets_path / 'som_models'
    metrics = assets_path / 'som_metrics'