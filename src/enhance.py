import pandas as pd
import numpy as np
from modAL.models import ActiveLearner
from modAL.uncertainty import uncertainty_sampling
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import time
from sklearn.metrics import accuracy_score
from tqdm import tqdm
import random
import generator


def enhance_al(dataset_path='C:\\Users\\Utsav Mehta\\Desktop\\for_rqs\\data\\2021.02.17.csv',env='stock',numb_iters=None,model='rf',do_preprocess=True,train_sample_size=100):
    data=pd.read_csv(dataset_path)
    if env=='stock':
        from sklearn.ensemble import RandomForestClassifier
        data=data.dropna()
        X=data.drop(['label'],axis=1).values
        y= data['label'].values

        random_choices_train=random.sample(range(0,X.shape[0]),train_sample_size)
        X_train=X[random_choices_train]
        y_train=y[random_choices_train]
        X=np.delete(X,random_choices_train,0)
        y=np.delete(y,random_choices_train,0)
        X_pool,X_test,y_pool,y_test=train_test_split(X,y)

        if do_preprocess:
            sc=StandardScaler()
            X=sc.fit_transform(X)

            enc=LabelEncoder()
            y=enc.fit_transform(y)

        else:
            pass

        learner = ActiveLearner(
            estimator=RandomForestClassifier(),
            query_strategy=uncertainty_sampling,
            X_training=X_train, y_training=y_train
        )

        scores=[]
        if numb_iters is None:
            numb_iters=X_pool.shape[0]

        start_time_data_prep = time.time()
        for i in tqdm(range(numb_iters)):
            query_idx, query_sample = learner.query(X_pool)
            noise_added_data=generator.add_noise_modified(query_sample)
            learner.teach(X_pool[query_idx], y_pool[query_idx])
            learner.teach(noise_added_data, y_pool[query_idx])
            X_pool=np.delete(X_pool,query_idx,0)
            y_pool=np.delete(y_pool,query_idx,0)
            y_pred=learner.predict(X_test)
            score=accuracy_score(y_test,y_pred)
            scores.append(score)
        total_time=time.time()-start_time_data_prep

        return scores, total_time

    elif env=='intel':
        from sklearnex.ensemble import RandomForestClassifier
        data=data.dropna()
        X=data.drop(['label'],axis=1).values
        y= data['label'].values

        random_choices_train=random.sample(range(0,X.shape[0]),train_sample_size)
        X_train=X[random_choices_train]
        y_train=y[random_choices_train]
        X=np.delete(X,random_choices_train,0)
        y=np.delete(y,random_choices_train,0)
        X_pool,X_test,y_pool,y_test=train_test_split(X,y)

        if do_preprocess:
            sc=StandardScaler()
            X=sc.fit_transform(X)

            enc=LabelEncoder()
            y=enc.fit_transform(y)

        else:
            pass

        learner = ActiveLearner(
            estimator=RandomForestClassifier(),
            query_strategy=uncertainty_sampling,
            X_training=X_train,
            y_training=y_train
        )

        scores=[]
        if numb_iters is None:
            numb_iters=X_pool.shape[0]
        start_time_data_prep = time.time()
        for i in tqdm(range(numb_iters)):
            query_idx, query_sample = learner.query(X_pool)
            noise_added_data=generator.add_noise_modified(query_sample)
            learner.teach(X_pool[query_idx], y_pool[query_idx])
            learner.teach(noise_added_data, y_pool[query_idx])
            X_pool=np.delete(X_pool,query_idx,0)
            y_pool=np.delete(y_pool,query_idx,0)
            y_pred=learner.predict(X_test)
            score=accuracy_score(y_test,y_pred)
            scores.append(score)
        total_time=time.time()-start_time_data_prep

        return scores, total_time