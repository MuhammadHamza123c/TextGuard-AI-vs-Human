![TextGuard](https://github.com/MuhammadHamza123c/TextGuard-AI-vs-Human/blob/main/demo_image.png) TextGuard – AI vs Human Text Detector

**TextGuard** is an AI-powered detector that distinguishes between human-written and AI-generated text. It is trained on the **AI vs Human dataset** from Kaggle with **500K+ samples**.  

Live demo: [TextGuard on Hugging Face](https://humza7656-textguard.hf.space)

---

## 🚀 Features

- Detects AI-generated vs human-written text with **high accuracy**.
- Pretrained models included: \`ai_human_vec.joblib\`, \`model_lg.joblib\`.
- Easy inference via \`main.py\`.
- Provides detailed classification metrics and ROC visualization.

---

## 🎯 Purpose

The purpose of **TextGuard** is to provide a reliable AI vs Human text detection tool that helps users, educators, and developers quickly identify AI-generated content. It aims to support content verification, plagiarism detection, and maintain trust in written material.



## 📊 Model Performance

### Accuracy on **Unseen Data**:

```
Accuracy: 0.9917
```

**Classification Report:**
```
| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.99      | 0.99   | 0.99     | 36,098  |
| 1     | 0.99      | 0.99   | 0.99     | 36,478  |
```
**Macro / Weighted Avg:** 0.99  

### Accuracy on **Seen Data**:

```
Accuracy: 0.9926
```

**Classification Report:**
```
| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.99      | 0.99   | 0.99     | 145,340 |
| 1     | 0.99      | 0.99   | 0.99     | 144,960 |

```

**Macro / Weighted Avg:** 0.99  

### ROC Curve

![ROC Curve](https://github.com/MuhammadHamza123c/TextGuard-AI-vs-Human/blob/main/roc.png)


## 🛠️ Installation

```
git clone https://github.com/MuhammadHamza123c/TextGuard-AI-vs-Human.git
cd TextGuard-AI-vs-Human
pip install -r requirements.txt

```

## **⚡ Usage**

```
streamlit run main.py

```
## 🗂️**Repository Structure**

```
.
├── .gitignore
├── AI_vs_human.ipynb      # Jupyter Notebook for training & analysis
├── ai_human_vec.joblib    # Pretrained vectorizer
├── demo_image.png         # Project banner image
├── LICENSE
├── main.py                # Main script for prediction
├── model_lg.joblib        # Pretrained AI model
├── requirements.txt       # Dependencies
└── roc.png                # ROC curve image

```

## **LICENSE**

This project is licensed under the MIT License.

## Made with ❤️ by Hamza.

