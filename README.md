# California Housing Price Prediction

This project builds a **Machine Learning API** using **Flask** to predict housing prices in California based on user input. The model is trained using the **California Housing Dataset** from Scikit-learn. The front-end form allows users to input housing features and get real-time price predictions.

---

## 🚀 Features

- 📊 **Exploratory Data Analysis (EDA)** to understand the dataset.
- 🔥 **Feature Engineering** including scaling, encoding, and selection.
- 🤖 **Multiple Regression Models** trained and compared (Linear Regression, Decision Tree, Random Forest, XGBoost).
- 🎯 **Hyperparameter Tuning** with GridSearchCV for optimal performance.
- 🌐 **Flask-based API** to serve predictions.
- 🖥️ **Interactive Web Form** to input values and get predictions.
- 📦 **Docker Support** for containerized deployment.

---

## 📂 Project Structure

```
📁 California-Housing-Prediction
│── 📁 templates             # HTML files for the web interface
│   ├── index.html           # User input form
│── 📁 static                # (Optional) CSS, JS, or image files
│── 📁 models                # Stores trained model files
│── 📄 app.py                # Flask application
│── 📄 model_train.py        # Script to train and save the model
│── 📄 requirements.txt      # Required dependencies
│── 📄 Dockerfile            # Containerization setup (optional)
│── 📄 README.md             # Documentation
```

---

## 📥 Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/California-Housing-Prediction.git
cd California-Housing-Prediction
```

### 2️⃣ Create a Virtual Environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Model Training

Run the `model_train.py` script to train the model and save it as a `.pkl` file.

```sh
python model_train.py
```

---

## 🚀 Run the Flask Application

```sh
python app.py
```

- Open **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser.
- Enter values in the form and click **Predict** to get the estimated price.

---

## 🎯 API Endpoints

### **1️⃣ Home Page**

- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Renders the input form (index.html)

### **2️⃣ Prediction API**

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Input:** JSON with housing features
- **Output:** JSON with predicted price

#### Example Request (POST):

```json
{
  "features": [4.5, 20.0, 6.0, 1.2, 300.0, 150.0, 37.8, -122.4]
}
```

#### Example Response:

```json
{
  "predicted_price": 250000.0
}
```

---

## 🐳 Docker (Optional)

### **Build and Run in Docker**

```sh
docker build -t housing-prediction .
docker run -p 5000:5000 housing-prediction
```

---

## 🛠 Technologies Used

- Python 🐍
- Flask 🌐
- Scikit-learn 📊
- XGBoost ⚡
- Pandas & NumPy 🏋️
- HTML, CSS, JavaScript 🎨
- Docker 🐳 (Optional)

---

## 📌 Future Enhancements

✅ Deploy on AWS/Heroku 🚀
✅ Add authentication for API requests 🔐
✅ Improve UI with Bootstrap/Tailwind CSS 🎨
✅ Store historical predictions in a database 📊

---

## 🤝 Contributing

Feel free to fork and submit a pull request with improvements! 🚀

---

## 📜 License

This project is **MIT licensed**. Feel free to use and modify! ✨
