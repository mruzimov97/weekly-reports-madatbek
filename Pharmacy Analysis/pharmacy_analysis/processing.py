import pandas as pd


def process_claims(claims_df: pd.DataFrame, reverts_df: pd.DataFrame) -> pd.DataFrame:
    if claims_df.empty:
        return pd.DataFrame()

    claims_df["price"] = pd.to_numeric(claims_df["price"], errors="coerce").fillna(0.0)
    claims_df["quantity"] = pd.to_numeric(claims_df["quantity"], errors="coerce").fillna(0).astype(int)
    claims_df["unit_price"] = claims_df["price"] / claims_df["quantity"]

    if not reverts_df.empty:
        reverts_df = reverts_df.groupby("claim_id").size().reset_index(name="reverted")
        claims_df = claims_df.merge(reverts_df, left_on="id", right_on="claim_id", how="left").fillna(0)
        claims_df["reverted"] = claims_df["reverted"].astype(int)
    else:
        claims_df["reverted"] = 0

    return claims_df.groupby(["npi", "ndc"]).agg(
        fills=("id", "count"),
        reverted=("reverted", "sum"),
        avg_price=("unit_price", "mean"),
        total_price=("price", "sum")
    ).reset_index()
