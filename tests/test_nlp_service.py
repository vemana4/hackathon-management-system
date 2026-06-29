import pytest
from services.nlp_service import NLPService

def test_nlp_service_initialization():
    service = NLPService()
    # Should initialize, even if spaCy is missing, it will have fallback
    assert service is not None

def test_analyze_proposal_empty():
    service = NLPService()
    result = service.analyze_proposal("")
    assert result['quality_score'] == 0.0
    assert result['word_count'] == 0

def test_analyze_proposal_valid():
    service = NLPService()
    text = (
        "Objective: We propose to design and implement a comprehensive procurement management system. "
        "Our team has extensive experience in delivery of enterprise software contracts, assuring compliance "
        "with all technical specifications, milestone plans, and project management regulations. "
        "We look forward to collaborating on this critical infrastructure project."
    )
    result = service.analyze_proposal(text)
    
    assert result['quality_score'] > 0.0
    assert result['word_count'] > 0
    assert result['readability_score'] >= 0.0
    assert result['technical_terms_count'] > 0
    assert result['completeness_score'] > 0.0
    assert result['professional_score'] > 0.5  # Phrases like 'we propose' boost professionalism

def test_syllable_count():
    service = NLPService()
    assert service._count_syllables("test") == 1
    assert service._count_syllables("banana") == 3
    assert service._count_syllables("implementation") == 5
