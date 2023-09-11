import estimator
import pandas as pd
import generator
import numpy as np

def augment(df_path:None,samples_to_generate):
    if df_path== None:
        df_path='C:\\Users\\Utsav Mehta\\Desktop\\for_rqs\\data\\2021.02.17.csv'
    df=pd.read_csv(df_path)
    type_of_cols=estimator.get_estimate(df)
    print(type_of_cols)
    generated_values=[]
    for i in range(len(type_of_cols)):
        curr=df.iloc[:,i]
        types=type_of_cols[i]
        if types=='categorical':
            print('here')
            unique_values, counts = np.unique(curr.values, return_counts=True)
            total_elements = len(curr.values)
            probabilities = np.zeros(len(unique_values), dtype=float)
            for i, count in enumerate(counts):
                probabilities[i] = count / total_elements
            generated=generator.add_categorical_column_modified(curr,samples_to_generate,"abc",[curr.iloc[0],curr.iloc[1]],unique_values,probabilities)
            generated_values.append(generated)

        if types=='binomial':
            unique_values, counts = np.unique(curr.values, return_counts=True)
            total_elements = len(curr.values)
            probabilities = np.zeros(len(unique_values), dtype=float)
            for i, count in enumerate(counts):
                probabilities[i] = count / total_elements
            generated=generator.add_numeric_column_modified(curr,samples_to_generate,label="abc",dist="binomial",vals=[int(curr.iloc[0]),int(curr.iloc[1]),probabilities[0],probabilities[1]])
            generated_values.append(generated)

        if types=='uniform':
            generated=generator.add_numeric_column_modified(curr,samples_to_generate,label="abc",dist="uniform",vals=[int(curr.iloc[0]),int(curr.iloc[1])])
            generated_values.append(generated)

        if types=='random':
            generated=generator.add_numeric_column_modified(curr,samples_to_generate,label="abc",dist="random",vals=[int(curr.iloc[0]),int(curr.iloc[1])])
            generated_values.append(generated)
    generated_values=np.array(generated_values)
    generated_values=generated_values.T
    return generated_values
