import pytest
import os
from unittest.mock import MagicMock, patch
from services.ml_service import MLService

@pytest.fixture
def temp_models_dir(tmp_path):
    return str(tmp_path / "models")

def test_ml_service_initialization(temp_models_dir):
    service = MLService(model_path=temp_models_dir)
    service.initialize()
    
    assert service.model is not None
    assert service.scaler is not None
    assert os.path.exists(service.model_file)
    assert os.path.exists(service.scaler_file)

def test_extract_single_bid_features(temp_models_dir):
    service = MLService(model_path=temp_models_dir)
    
    bid = {
        'id': 1,
        'company_name': 'Test Company',
        'bid_amount': 50000,
        'proposal_text': 'Objective: Build a new bridge.',
        'nlp_score': 0.8,
        'created_at': '2026-06-29 10:00:00',
        'tender_deadline': '2026-07-29 10:00:00'
    }
    
    features = service._extract_single_bid_features(bid, tender_budget=100000)
    
    assert len(features) == 8
    assert features[0] == 50000.0
    assert features[1] == 0.5
    assert features[2] == len('Objective: Build a new bridge.')
    assert features[3] == len('Test Company')
    assert features[4] == 10
    assert features[5] == 0

@patch('services.database_service.DatabaseService')
def test_train_model_with_insufficient_data(mock_db_class, temp_models_dir):
    mock_db = MagicMock()
    mock_db.get_connection.return_value.cursor.return_value.fetchall.return_value = []
    mock_db_class.return_value = mock_db
    
    service = MLService(model_path=temp_models_dir)
    result = service.train_model(retrain=True)
    
    assert result['success'] is True
    assert result['n_samples'] == 100
    assert result['model_saved'] is True
