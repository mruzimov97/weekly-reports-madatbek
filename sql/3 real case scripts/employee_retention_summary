# SQL Query: Departmental Employee Retention Summary

## Objective
Provide a summarized view of employee attrition by department, including active employees, terminated employees, and a simple retention percentage.

## SQL Code

'''
WITH status_counts AS (
    SELECT
        department,
        COUNT(*) FILTER (WHERE termination_date IS NOT NULL) AS terminated,
        COUNT(*) FILTER (WHERE termination_date IS NULL) AS active
    FROM employees
    GROUP BY department
),
retention AS (
    SELECT
        department,
        active,
        terminated,
        ROUND(100.0 * active / NULLIF((active + terminated), 0), 2) AS retention_percent
    FROM status_counts
)
SELECT * FROM retention
ORDER BY retention_percent DESC;
'''

## Explanation

- CTE 'status_counts': Counts the number of active and terminated employees in each department using SQL's 'FILTER' clause.
- CTE 'retention':Calculates the retention percentage using the formula: retention = active / (active + terminated)
- Uses 'NULLIF(..., 0)' to avoid division-by-zero errors.
- Uses 'ROUND(..., 2)' to present a clean percentage value.

## Sample Output

| department  | active | terminated | retention_percent |
|-------------|--------|------------|-------------------|
| HR          | 1      | 0          | 100.00            |
| Sales       | 1      | 1          | 50.00             |
| Engineering | 1      | 1          | 50.00             |

## Highlights

-  Clean two-step CTE structure
-  Conditional counting with 'FILTER'
-  Safe and readable retention calculation
-  Output ordered by retention performance

## Use Case

Useful for HR dashboards or internal analytics to monitor departmental retention and compare performance across business units.


---

##  Performance Considerations

### Small Datasets (< 10K employees)
- Executes quickly with no indexes needed
- 'FILTER' and 'GROUP BY' are highly efficient

### Larger Datasets (> 100K employees)
Potential bottlenecks:
- Full table scan on 'employees'
- Repeated aggregation and sorting
- 'ORDER BY retention_percent DESC' adds computation on large results

###  Index Recommendations

'''
-- Helps FILTER and WHERE clauses on termination analysis
CREATE INDEX idx_employees_termination ON employees(termination_date);

-- speeds up grouping by department
CREATE INDEX idx_employees_department ON employees(department);
'''

### EXPLAIN Observations
- Seq Scan on employees without indexes
- GroupAggregate over departments
- CPU & memory increase with number of rows and departments

### Optimization Tips
- Materialize 'status_counts' as a temp table for reuse
- Consider partitioning or clustering if data is huge
- Avoid repeated scans if query is used often — cache results periodically

---

