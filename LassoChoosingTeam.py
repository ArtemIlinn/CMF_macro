"""
Takin’ on a challenge is a lot like riding a horse.
If you’re comfortable while you’re doin’ it, you’re probably doin’ it wrong.
                                                      -- Ted Lasso

That's this Lasso, right? Right?



!!!The code runs Lasso Linear Model to determine the most useful features for forecasting!!!

"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Lasso


def body(df, X, y, X_train, X_test, y_train, y_test):
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', Lasso())
    ])

    search = GridSearchCV(pipeline,
                          {'model__alpha': np.arange(0.1, 10, 0.1)},
                          cv=5, scoring="neg_mean_squared_error", verbose=3
                          )

    search.fit(X_train, y_train)
    # search.best_params_

    coefficients = search.best_estimator_.named_steps['model'].coef_
    importance = np.abs(coefficients)

    try:
        important_features = np.array(df.drop(columns=['APSP crude oil($/bbl)', 'Date']).columns)[importance > 0]
    except:
        important_features = np.array(df.drop(columns=['APSP crude oil($/bbl)']).columns)[importance > 0]

    return importance, important_features


def lasso_get_features(df, X, y, X_train, X_test, y_train, y_test):
    try:
        return body(df, X, y, X_train, X_test, y_train, y_test)
    except:
        X, y = df.drop(columns=['APSP crude oil($/bbl)']), df['APSP crude oil($/bbl)']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        return body(df, X, y, X_train, X_test, y_train, y_test)
