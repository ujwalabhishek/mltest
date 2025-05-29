#this is the code to the machine learning model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
def train_model(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)
    
    # Preprocess the data
    X = data.drop('target', axis=1)  # Features
    y = data['target']  # Target variable
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
    
    return model
def save_model(model, model_path):
    import joblib
    # Save the trained model to a file
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
def load_model(model_path):
    import joblib
    # Load the model from a file
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")
    return model

def predict(model, input_data):
    # Make predictions using the loaded model
    predictions = model.predict(input_data)
    return predictions          


if __name__ == "__main__":
    # Example usage
    data_path = 'data.csv'  # Path to your dataset
    model_path = 'model.joblib'  # Path to save the trained model
    
    # Train the model
    model = train_model(data_path)
    
    # Save the trained model
    save_model(model, model_path)
    
    # Load the model
    loaded_model = load_model(model_path)
    
    # Example input data for prediction (replace with actual data)
    example_input = pd.DataFrame([[1, 2, 3, 4]], columns=['feature1', 'feature2', 'feature3', 'feature4'])
    
    # Make predictions
    predictions = predict(loaded_model, example_input)
    print(f"Predictions: {predictions}")