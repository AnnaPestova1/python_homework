import pandas as pd
import math

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    def print_with_headers(self):
        print(len(self))
        if len(self) <= 10:
            print(self)
        else:
            max_for_range = math.ceil((len(self)/10))
            for x in range(max_for_range+1):
                first = x*10-10
                if x <= max_for_range:
                    last = x*10
                else:
                    last=len(self)

                print(self.iloc[first:last])


            


    
dfp = DFPlus.from_csv("../csv/products.csv")
DFPlus.print_with_headers(dfp)