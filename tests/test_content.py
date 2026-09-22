from scripts.validate import run_all, validate_evidence, validate_language_pairs, validate_proposal_graph, validate_review_matrix

def test_repository_is_valid() -> None:
    assert run_all() == []

def test_evidence_graph_is_consistent() -> None:
    assert validate_evidence() == []

def test_bilingual_structure_is_consistent() -> None:
    assert validate_language_pairs() == []


def test_proposal_graph_is_consistent() -> None:
    assert validate_proposal_graph() == []

def test_review_matrix_is_complete() -> None:
    assert validate_review_matrix() == []
