import pandas as pd
from src import clean_csv

def test_clean_data(tmp_path):
    # Prepare test input CSV
    test_data = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", None, "Charlie"],
        "email": ["a@email.com", "b@email.com", None]
    })
    input_path = tmp_path / "test_input.csv"
    output_path = tmp_path / "test_output.csv"
    test_data.to_csv(input_path, index=False)

    # Run the cleaning function
    clean_csv.clean_data(str(input_path), str(output_path))

    # Load and check output
    result = pd.read_csv(output_path)
    assert result.shape[0] == 1
    assert "Alice" in result["name"].values