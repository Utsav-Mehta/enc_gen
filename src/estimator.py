import pandas as pd
from scipy.special import rel_entr
import numpy as np 
import scipy.stats as stats
from generator import *

def get_estimate(df):
    type_of_cols=[]

    for i in range(df.shape[1]):
        temp=df.iloc[:,i].values

        unique_values=np.unique(temp)
        if isinstance(unique_values[0], str):
            unique_values=np.unique(temp)
            if len(unique_values) == 2:
                type_of_cols.append('binomial')
            else:
                type_of_cols.append('categorical')

        else:
            final_arr=[]
            for value in temp:
                final_arr.append(value)
            final_arr=np.array(final_arr)

            try:
                minimum=np.min(final_arr)
                maximum=np.max(final_arr)
                mean_values=np.mean(final_arr)
                std_dev=np.std(final_arr)
            except:
                minimum=final_arr[0]
                maximum=final_arr[-1]
                mean_values=final_arr[0]
                std_dev=1000

            # Generate a NumPy array of random numbers from the truncated normal distribution
            num_samples = temp.shape[0]  # Number of samples 
            truncated_samples = np.random.normal(mean_values, std_dev, num_samples)

            uniform_samples = np.random.uniform(minimum, maximum, num_samples)

            uniform_kl=sum(rel_entr(final_arr,uniform_samples))
            normal_kl=sum(rel_entr(final_arr,truncated_samples))

            if uniform_kl and normal_kl == 'inf':
                type_of_cols.append('random')

            if normal_kl < uniform_kl:
                type_of_cols.append('normal')
            
            else:
                type_of_cols.append('uniform')
        
    return type_of_cols