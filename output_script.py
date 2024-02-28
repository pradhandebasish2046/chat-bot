```python
import pandas as pd

total_nan_values = df['age'].isnull().sum()
print(total_nan_values)
```