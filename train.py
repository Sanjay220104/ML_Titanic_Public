from numpy._core import numeric
import joblib
import pandas as pd
import seaborn as sns
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.linear_model import LogisticRegression

df = sns.load_dataset("titanic")

df = df[["pclass", "sex", "age", "fare", "survived"]]

x = df.drop("survived", axis=1)
y = df["survived"]

numeric_feature = ["age", "fare"]
categorical_features = ["sex", "pclass"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
categorical_pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("scaler", OrdinalEncoder())
    ])
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_feature),
    ("cat", categorical_pipeline, categorical_features)
])

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression())
])

os.makedirs("model", exist_ok=True)

joblib.dump(pipeline, "model/pipeline.pkl")

print("pipeline saved successfully")
