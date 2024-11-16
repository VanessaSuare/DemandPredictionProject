"""."""
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def train_model(data_limpia):
    """."""
    X = data_limpia.drop(columns=['CANTIDAD'])
    y = data_limpia['CANTIDAD']
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
        )
    model_xgb = xgb.XGBRegressor(
        n_estimators=150,
        learning_rate=0.03,
        max_depth=5,
        min_child_weight=10,
        subsample=0.6,
        colsample_bytree=0.6,
        reg_alpha=0.5,
        reg_lambda=5,
        random_state=42
    )
    model_xgb.fit(X_train, y_train)
    y_pred_test_xgb = model_xgb.predict(X_test)
    metrics = {
        "train_rmse": np.sqrt(
            mean_squared_error(y_train, model_xgb.predict(X_train))
            ),
        "test_rmse": np.sqrt(mean_squared_error(y_test, y_pred_test_xgb)),
        "test_r2": r2_score(y_test, y_pred_test_xgb),
        "train_r2": r2_score(y_train, model_xgb.predict(X_train)),
        "test_mae": mean_absolute_error(y_test, y_pred_test_xgb)
    }
    return model_xgb, metrics


def predict(model, data):
    """."""
    return model.predict(data)
