import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import pickle


if __name__ == "__main__":
    df = pd.read_csv("data/refined/german.csv")
    df.head()

    X = df.drop(columns=["creditability"])
    y = df["creditability"]
    y = y.replace({"Good": 1, "Bad": 0})

    # Define the mappings for ordinal variables
    ordinal_mappings = {
        "status_of_existing_checking_account": {
            "< 0 DM": 1,
            "0 <= ... < 200 DM": 2,
            ">= 200 DM / salary assignments for at least 1 year": 3,
            "no checking account": 4,
        },
        "savings_account_bonds": {
            "< 100 DM": 1,
            "100 <= ... < 500 DM": 2,
            "500 <= ... < 1000 DM": 3,
            ">= 1000 DM": 4,
            "unknown/ no savings account": 5,
        },
        "present_employment_since": {
            "unemployed": 1,
            "< 1 year": 2,
            "1 <= ... < 4 years": 3,
            "4 <= ... < 7 years": 4,
            ">= 7 years": 5,
        },
    }

    # Replace the ordinal values
    X = X.replace(ordinal_mappings)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    dv = DictVectorizer(sparse=False)
    X_train_dv = dv.fit_transform(X_train.to_dict(orient="records"))

    # Create a logistic regression model
    log_reg_model = LogisticRegression(
        max_iter=2000,
        class_weight="balanced",
        C=1.0,
    )

    # Train the model
    log_reg_model.fit(X_train_dv, y_train)

    X_test_dv = dv.transform(X_test.to_dict(orient="records"))

    # Get probability predictions
    y_pred_proba = log_reg_model.predict_proba(X_test_dv)

    # Use a higher threshold for predicting good credit (class 1)
    # Default is 0.5, let's try 0.6
    y_pred = (y_pred_proba[:, 1] >= 0.6)
    y_pred = y_pred[0].astype(int)

    with open("src/churn_app/models/log_reg_model.pkl", "wb") as file:
        pickle.dump((dv, log_reg_model), file)
