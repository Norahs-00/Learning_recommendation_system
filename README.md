# 📚 Learning Recommendation System

## 🔍 Project Overview
The **Learning Recommendation System** is an Artificial Intelligence–based application designed to help learners select relevant online courses from large learning platforms such as Coursera.  
Due to the rapid growth of online education, learners often face **information overload** and difficulty choosing suitable courses.  
This project applies **Machine Learning techniques** to provide **personalized and intelligent course recommendations**.

---

## 🎯 Objectives
- Reduce information overload for online learners  
- Recommend relevant and high-quality courses  
- Apply supervised and unsupervised learning techniques  
- Develop a hybrid AI-based recommendation system  
- Demonstrate real-world application of Artificial Intelligence in education  

---

## 🧠 AI & Machine Learning Concepts Used

### Artificial Intelligence (AI)
Enables the system to make intelligent decisions based on course data.

### Machine Learning (ML)
Learns patterns from historical course data to predict course relevance.

### Supervised Learning
Used to predict whether a course should be recommended:
- **Logistic Regression** – Simple and interpretable baseline model  
- **Decision Tree** – Captures complex decision rules  
- **Random Forest** – Improves accuracy by combining multiple trees  

### Unsupervised Learning
- **K-Means Clustering** – Groups similar courses based on features.

### Hybrid Recommendation System
Combines supervised predictions and clustering results to improve:
- Accuracy  
- Stability  
- Recommendation diversity  

---

## 🗂 Dataset
- **Source:** Coursera Course Dataset (2024)  
- **Features Used:**
  - Course title  
  - Ratings  
  - Enrollment numbers  
  - Reviews  
  - Course category  
  - Organization / Institution  

---

## ⚙️ System Workflow
1. Load Coursera dataset  
2. Preprocess data:
   - Remove duplicate records  
   - Handle missing values  
   - Encode categorical features  
   - Normalize numerical features  
3. Split dataset into 80% training and 20% testing  
4. Train supervised machine learning models  
5. Apply K-Means clustering  
6. Combine results using a hybrid recommendation approach  
7. Generate Top-N course recommendations  

---

## 🧪 Achieved Results
- **Logistic Regression:** Provides baseline performance  
- **Decision Tree:** Learns complex data patterns  
- **Random Forest:** Achieves the highest accuracy  
- **Hybrid Model:** Produces stable and reliable recommendations  

---

## 🌍 Real-World Impact
- Reduces difficulty in course selection  
- Saves learner time  
- Improves learning satisfaction and engagement  
- Works without detailed learner history  
- Scales for large online learning platforms  

---

## 🖥 Application Implementation
The project includes a **Python-based graphical user interface (GUI)** that allows users to:
- Enter skills they want to learn  
- View top-rated and relevant course recommendations  

---

## 🛠 Tools & Technologies Used
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Tkinter  
- **Development Environment:** VS Code, Jupyter Notebook  
- **Version Control:** Git & GitHub  

---

## 📌 Future Enhancements
- Include learner behavior and feedback data  
- Apply Natural Language Processing (NLP) on course reviews  
- Develop a web-based recommendation system  
- Implement Explainable AI (XAI) techniques  

