# I want to store passenger data of the Titanic. For a number of passengers, 
# I know the name (characters), age (integers) and sex (male/female) data.
import pandas as pa
def pandas_df():
    df = pa.DataFrame(
        {
            "Name" : ["Braund, Mr. Owen Harries",
                       "Allen, Mr, William Henry",
                       "Bonnel, Miss. Elazabath"],
            "Age" : [45,50,30],
            "Sex" : ["Male", "Male", "Female"]
        }
    )
    print(df)
pandas_df()

