from scripts.validate import run_all, validate_evidence, validate_language_pairs

def test_repository_is_valid() -> None:
    assert run_all() == []

def test_evidence_graph_is_consistent() -> None:
    assert validate_evidence() == []

def test_bilingual_structure_is_consistent() -> None:
    assert validate_language_pairs() == []
