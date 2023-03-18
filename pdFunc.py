print()
print()
print("Resultat")

import pandas as pd
import numpy as np
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s) 


print()
print()
print("Resultat")
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
print(df)

print()
print()
print("Resultat")
import pandas as pd 
import numpy as np 
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
print(df['A'])

print()
print()
print("Resultat")
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD')) 
print(df.mean()) 
print(df.std())
