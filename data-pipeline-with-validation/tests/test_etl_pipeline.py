import pandas as pd
from scripts import etl_pipeline

def test_ingest():
    df = etl_pipeline.ingest_data("../data/raw_data.csv")
    assert not df.empty, "Ingested DataFrame should not be empty"

def test_clean():
    df = pd.DataFrame({
        "id": [1, 1],
        "email": ["a@email.com", "a@email.com"]
    })
    df_cleaned = etl_pipeline.clean_data(df)
    assert len(df_cleaned) == 1, "Duplicate rows should be removed"

def test_validation_pass():
    df = pd.DataFrame({
        "id": [1, 2],
        "email": ["a@email.com", "b@email.com"]
    })
    result = etl_pipeline.validate_data(df)
    assert all(result.values()), "All validation checks should pass"

def test_validation_fail():
    df = pd.DataFrame({
        "id": [1, 1],
        "email": ["a@email.com", None]
    })
    result = etl_pipeline.validate_data(df)
    assert not all(result.values()), "Validation should fail for duplicate and null email"