# SQL Query: Monthly Revenue Trend with Indexing

## Objective
Track revenue trends month by month from a transactions table, while preparing the query for performance optimization using indexing.

## Schema

'''
CREATE TABLE transactions (
    txn_id INT,
    customer_id INT,
    txn_date DATE,
    revenue DECIMAL(10,2)
);
'''

## Sample Data

'''
INSERT INTO transactions VALUES
(1, 101, '2025-01-10', 100.00),
(2, 101, '2025-01-15', 200.00),
(3, 102, '2025-02-05', NULL),
(4, 103, '2025-02-20', 300.00),
(5, 104, '2025-03-01', 150.00);
'''

## SQL Code

'''
WITH cleaned AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', txn_date) AS txn_month,
        COALESCE(revenue, 0) AS revenue
    FROM transactions
)
SELECT
    txn_month,
    SUM(revenue) AS total_revenue
FROM cleaned
GROUP BY txn_month
ORDER BY txn_month;
'''

## Explanation

- CTE 'cleaned': Prepares the dataset by truncating transaction dates to monthly buckets and replacing 'NULL' revenues with '0' using 'COALESCE'.
- Main SELECT:
  - Groups data by 'txn_month'.
  - Aggregates total revenue per month using 'SUM(revenue)'.
  - Orders results chronologically.

## Sample Output

| txn_month | total_revenue |
|-----------|----------------|
| 2025-01-01 | 300.00        |
| 2025-02-01 | 300.00        |
| 2025-03-01 | 150.00        |

## Highlights

-  CTE ('cleaned')
-  NULL Handling with 'COALESCE(revenue, 0)'
-  Temporal grouping using 'DATE_TRUNC('month', txn_date)'
-  Prepared for performance optimization

## Suggested Index

'''
CREATE INDEX idx_txn_date ON transactions(txn_date);
'''
This improves performance of queries involving filtering or grouping by 'txn_date'.

## Use Case

Common in business intelligence dashboards, finance analytics, or SaaS reporting, where monthly revenue trends must be visualized and analyzed.

---

##  Performance Considerations

###  Small to Medium Datasets
- Executes efficiently with basic resources

### Larger Datasets
- Monthly grouping and 'COALESCE()' are fine, but indexing 'txn_date' is key

### Index Recommendations
'''sql
CREATE INDEX idx_txn_date ON transactions(txn_date);
'''
- Speeds up date-based filtering and grouping operations

### EXPLAIN Observations
- Look for 'GroupAggregate' on 'txn_month'
- Ensure 'Seq Scan' becomes 'Index Scan' when filtering is introduced
