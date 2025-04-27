import streamlit as st
from streamlit.components.v1 import html

# CSS and JavaScript from your original HTML
css = """
<style>
/* Paste all your CSS here */
</style>
"""

js = """
<script>
// Paste any JavaScript here
</script>
"""

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Credit Card ML Evaluation Report</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- AOS animation library -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --primary-color: #0077b6;
            --secondary-color: #00b4d8;
            --accent-color: #0096c7;
            --light-bg: #f8f9fa;
            --dark-text: #212529;
            --light-text: #6c757d;
        }
        
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f5f7fa;
            color: var(--dark-text);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .report-container {
            max-width: 1200px;
            margin: 30px auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 5px 30px rgba(0, 0, 0, 0.08);
            overflow: hidden;
        }
        
        header {
            padding: 70px 20px;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            color: white;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        header::before {
            content: "";
            position: absolute;
            top: -50px;
            right: -50px;
            width: 200px;
            height: 200px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
        }
        
        header::after {
            content: "";
            position: absolute;
            bottom: -80px;
            left: -80px;
            width: 300px;
            height: 300px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 50%;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            position: relative;
            z-index: 2;
        }
        
        .header-subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 700px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }
        
        section {
            padding: 60px 40px;
        }
        
        h2 {
            color: var(--primary-color);
            margin: 50px 0 25px;
            padding-bottom: 15px;
            border-bottom: 2px solid #e9ecef;
            position: relative;
        }
        
        h2::after {
            content: "";
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 100px;
            height: 2px;
            background: var(--secondary-color);
        }
        
        .section-intro {
            font-size: 1.1rem;
            color: var(--dark-text);
            margin-bottom: 30px;
        }
        
        .timeline {
            position: relative;
            padding-left: 30px;
            margin-left: 20px;
        }
        
        .timeline::before {
            content: "";
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            width: 3px;
            background: linear-gradient(to bottom, var(--secondary-color), var(--primary-color));
            border-radius: 3px;
        }
        
        .timeline-item {
            position: relative;
            margin-bottom: 40px;
            padding-left: 30px;
        }
        
        .timeline-item::before {
            content: "";
            position: absolute;
            left: -10px;
            top: 5px;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: white;
            border: 3px solid var(--secondary-color);
            z-index: 1;
        }
        
        .timeline-item h5 {
            color: var(--primary-color);
            margin-bottom: 10px;
            font-weight: 600;
        }
        
        .card {
            border: none;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            height: 100%;
            border-top: 3px solid var(--secondary-color);
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 180, 216, 0.15);
        }
        
        .card-header {
            background: white;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            font-weight: 600;
            color: var(--primary-color);
            padding: 15px 20px;
        }
        
        .card-body {
            padding: 20px;
        }
        
        .model-icon {
            font-size: 1.5rem;
            margin-right: 10px;
            color: var(--secondary-color);
        }
        
        .metric-item {
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
        }
        
        .metric-value {
            font-weight: 500;
            color: var(--primary-color);
        }
        
        footer {
            background: var(--primary-color);
            color: white;
            text-align: center;
            padding: 25px 10px;
            margin-top: auto;
        }
        
        .footer-content {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .footer-icon {
            margin: 0 10px;
            color: rgba(255, 255, 255, 0.7);
            transition: all 0.3s;
        }
        
        .footer-icon:hover {
            color: white;
            transform: translateY(-2px);
        }
        
        .img-container {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            border: 1px solid #e9ecef;
        }
        
        .img-container img {
            display: block;
            width: 100%;
            height: auto;
        }
        
        .feature-list {
            list-style-type: none;
            padding: 0;
        }
        
        .feature-list li {
            padding: 10px 15px;
            margin-bottom: 8px;
            background: rgba(0, 180, 216, 0.1);
            border-left: 3px solid var(--secondary-color);
            border-radius: 0 4px 4px 0;
        }
        
        @media (max-width: 768px) {
            section {
                padding: 40px 20px;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .header-subtitle {
                font-size: 1rem;
            }
        }
    </style>
</head>

<body>
<div class="report-container">

    <header>
        <h1 data-aos="fade-down"><i class="fas fa-credit-card"></i> Credit Card Evaluation Using Machine Learning</h1>
        <p class="header-subtitle" data-aos="fade-up" data-aos-delay="200">Unlocking smarter decisions through data-driven modeling --by Ariharan Sumathi Mohan</p>
    </header>

    <section>
        <h2 data-aos="fade-right">1. Introduction</h2>
        <div class="section-intro" data-aos="fade-up">
            In the ever-evolving financial services sector, the ability to accurately evaluate credit card applications has become essential 
            to maintaining healthy lending practices and minimizing financial risk.
        </div>
        <p data-aos="fade-up">
            Traditional scoring models, such as FICO or manual underwriting, often suffer from subjectivity,
            outdated variables, and inefficiencies. Consequently, financial institutions are increasingly exploring machine learning (ML) 
            to augment or even replace traditional methods.
        </p>
        <p data-aos="fade-up">
            Machine learning models offer several advantages, including the ability to process large datasets, uncover hidden patterns,
            adjust to new trends dynamically, and improve prediction accuracy through continuous learning. In this project, we aimed to leverage
            a variety of machine learning algorithms to assess credit card applicants' eligibility based on a diverse set of features extracted from the German Credit Card dataset.
        </p>
        <p data-aos="fade-up">
            The goal of this project is twofold: first, to benchmark different machine learning models for credit card evaluation tasks,
            and second, to derive actionable insights into the most influential features that affect approval outcomes.
            By doing so, we seek to not only maximize predictive performance but also enhance the interpretability and trustworthiness
            of automated credit decisions.
        </p>

        <h2 data-aos="fade-right">2. Methodology</h2>
        <div class="timeline">
            <div class="timeline-item" data-aos="fade-up">
                <h5>Data Preprocessing</h5>
                <p>The foundation of any successful machine learning project lies in careful data preparation. Our dataset consisted of 1000 instances and 24 attributes, encompassing financial metrics (e.g., credit history, credit amount), employment details, personal status, and a few anonymized numerical features (Feature1, Feature2, etc.).</p>
                <p>The target variable, labeled as 'Target', had two classes:</p>
                <ul>
                    <li>1: Credit application approved</li>
                    <li>2: Credit application rejected</li>
                </ul>
                <p>For model compatibility, particularly with algorithms like XGBoost, the target classes were re-encoded:</p>
                <ul>
                    <li>0 → Not approved (original label 2)</li>
                    <li>1 → Approved (original label 1)</li>
                </ul>
                <p>Key preprocessing steps included:</p>
                <ul>
                    <li><strong>Handling missing values:</strong> Although the dataset had minimal missing entries, any absent values were imputed using median strategies for numerical features and mode strategies for categorical features.</li>
                    <li><strong>Feature encoding:</strong> Categorical variables were label-encoded or one-hot encoded depending on the algorithm requirements.</li>
                    <li><strong>Train-test split:</strong> The data was divided into 80% for training and 20% for testing using stratified sampling to preserve class distribution.</li>
                </ul>
                <p>An initial exploratory data analysis (EDA) revealed a slight class imbalance, with approximately 70% approvals versus 30% rejections, which warranted attention during model evaluation to avoid bias toward the majority class.</p>
            </div>
            <div class="timeline-item" data-aos="fade-up" data-aos-delay="100">
                <h5>Feature Correlation Analysis</h5>
                <div class="img-container">
                    <img src="https://github.com/Ariharan-S-M/German_dataset_ml/blob/master/feature_correlation.png" alt="Correlation Heatmap" class="img-fluid">
                </div>
                <p>The correlation matrix revealed several interesting relationships between features, helping us identify potential multicollinearity issues and guide our feature selection process.</p>
            </div>
            <div class="timeline-item" data-aos="fade-up" data-aos-delay="200">
                <h5>Model Selection</h5>
                <p>A carefully chosen set of machine learning algorithms was employed:</p>
                <div class="row">
                    <div class="col-md-6">
                        <ul>
                            <li><strong>Random Forest Classifier</strong> (ensemble, bagging)</li>
                            <li><strong>XGBoost Classifier</strong> (ensemble, boosting)</li>
                            <li><strong>K-Nearest Neighbors (KNN)</strong> (distance-based)</li>
                            <li><strong>Naive Bayes</strong> (probabilistic model)</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <ul>
                            <li><strong>Support Vector Machine (SVM)</strong> (margin-based classifier)</li>
                            <li><strong>Decision Tree Classifier</strong> (tree-based model)</li>
                            <li><strong>Convolutional Neural Network (CNN)</strong> (deep learning approach)</li>
                        </ul>
                    </div>
                </div>
                <p>Each model represents a unique family of learning paradigms, enabling a broad comparison across different algorithmic strategies. The choice of CNN, although unconventional for tabular data, was intended to investigate whether feature extraction through convolutional layers could outperform manual feature engineering.</p>
                
                <h5 class="mt-4">Evaluation Metrics</h5>
                <p>Each model underwent standardized training using cross-validation techniques to ensure robust performance evaluation. The following metrics were employed:</p>
                <div class="row">
                    <div class="col-md-6">
                        <ul>
                            <li><strong>Accuracy:</strong> Overall correctness</li>
                            <li><strong>Precision:</strong> True positives among predicted positives</li>
                            <li><strong>Recall (Sensitivity):</strong> True positives among actual positives</li>
                            <li><strong>F1-Score:</strong> Harmonic mean of precision and recall</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <ul>
                            <li><strong>Matthews Correlation Coefficient (MCC):</strong> A balanced metric useful for imbalanced datasets</li>
                            <li><strong>Brier Score:</strong> Measures the accuracy of probabilistic predictions</li>
                            <li><strong>False Positive Rate (FPR):</strong> Key in financial applications where approving a risky customer is costly</li>
                            <li><strong>Response Time:</strong> Inference time for each model, crucial for real-time deployment</li>
                        </ul>
                    </div>
                </div>
                <p>These evaluation parameters were selected to ensure a balanced focus on both predictive accuracy and practical usability.</p>
            </div>
        </div>

        <h2 data-aos="fade-right">3. Model Comparison</h2>
        <p data-aos="fade-up">We evaluated seven different machine learning models using a comprehensive set of metrics. Below are the detailed results:</p>

        <div class="row g-4 mt-4">
            <!-- Random Forest -->
            <div class="col-md-6 col-lg-4" data-aos="zoom-in">
                <div class="card">
                    <div class="card-header">
                        <i class="fas fa-tree model-icon"></i> Random Forest
                    </div>
                    <div class="card-body">
                        <div class="metric-item">
                            <span>F1-Score:</span>
                            <span class="metric-value">0.837</span>
                        </div>
                        <div class="metric-item">
                            <span>Precision:</span>
                            <span class="metric-value">0.813</span>
                        </div>
                        <div class="metric-item">
                            <span>Recall:</span>
                            <span class="metric-value">0.863</span>
                        </div>
                        <div class="metric-item">
                            <span>Accuracy:</span>
                            <span class="metric-value">84.3%</span>
                        </div>
                        <div class="metric-item">
                            <span>MCC-Score:</span>
                            <span class="metric-value">0.687</span>
                        </div>
                        <div class="metric-item">
                            <span>Brier-Score:</span>
                            <span class="metric-value">0.115</span>
                        </div>
                        <div class="metric-item">
                            <span>FPR:</span>
                            <span class="metric-value">0.174</span>
                        </div>
                        <div class="metric-item">
                            <span>Response Time:</span>
                            <span class="metric-value">0.120s</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- XGBoost -->
            <div class="col-md-6 col-lg-4" data-aos="zoom-in" data-aos-delay="100">
                <div class="card">
                    <div class="card-header">
                        <i class="fas fa-rocket model-icon"></i> XGBoost
                    </div>
                    <div class="card-body">
                        <div class="metric-item">
                            <span>F1-Score:</span>
                            <span class="metric-value">0.874</span>
                        </div>
                        <div class="metric-item">
                            <span>Precision:</span>
                            <span class="metric-value">0.849</span>
                        </div>
                        <div class="metric-item">
                            <span>Recall:</span>
                            <span class="metric-value">0.901</span>
                        </div>
                        <div class="metric-item">
                            <span>Accuracy:</span>
                            <span class="metric-value">87.9%</span>
                        </div>
                        <div class="metric-item">
                            <span>MCC-Score:</span>
                            <span class="metric-value">0.758</span>
                        </div>
                        <div class="metric-item">
                            <span>Brier-Score:</span>
                            <span class="metric-value">0.103</span>
                        </div>
                        <div class="metric-item">
                            <span>FPR:</span>
                            <span class="metric-value">0.141</span>
                        </div>
                        <div class="metric-item">
                            <span>Response Time:</span>
                            <span class="metric-value">0.092s</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- KNN -->
            <div class="col-md-6 col-lg-4" data-aos="zoom-in" data-aos-delay="200">
                <div class="card">
                    <div class="card-header">
                        <i class="fas fa-project-diagram model-icon"></i> KNN
                    </div>
                    <div class="card-body">
                        <div class="metric-item">
                            <span>F1-Score:</span>
                            <span class="metric-value">0.780</span>
                        </div>
                        <div class="metric-item">
                            <span>Precision:</span>
                            <span class="metric-value">0.774</span>
                        </div>
                        <div class="metric-item">
                            <span>Recall:</span>
                            <span class="metric-value">0.786</span>
                        </div>
                        <div class="metric-item">
                            <span>Accuracy:</span>
                            <span class="metric-value">79.3%</span>
                        </div>
                        <div class="metric-item">
                            <span>MCC-Score:</span>
                            <span class="metric-value">0.584</span>
                        </div>
                        <div class="metric-item">
                            <span>Brier-Score:</span>
                            <span class="metric-value">0.145</span>
                        </div>
                        <div class="metric-item">
                            <span>FPR:</span>
                            <span class="metric-value">0.201</span>
                        </div>
                        <div class="metric-item">
                            <span>Response Time:</span>
                            <span class="metric-value">0.272s</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Naive Bayes -->
            <div class="col-md-6 col-lg-4" data-aos="zoom-in" data-aos-delay="300">
                <div class="card">
                    <div class="card-header">
                        <i class="fas fa-chart-bar model-icon"></i> Naive Bayes
                    </div>
                    <div class="card-body">
                        <div class="metric-item">
                            <span>F1-Score:</span>
                            <span class="metric-value">0.757</span>
                        </div>
                        <div class="metric-item">
                            <span>Precision:</span>
                            <span class="metric-value">0.679</span>
                        </div>
                        <div class="metric-item">
                            <span>Recall:</span>
                            <span class="metric-value">0.855</span>
                        </div>
                        <div class="metric-item">
                            <span>Accuracy:</span>
                            <span class="metric-value">74.3%</span>
                        </div>
                        <div class="metric-item">
                            <span>MCC-Score:</span>
                            <span class="metric-value">0.506</span>
                        </div>
                        <div class="metric-item">
                            <span>Brier-Score:</span>
                            <span class="metric-value">0.206</span>
                        </div>
                        <div class="metric-item">
                            <span>FPR:</span>
                            <span class="metric-value">0.356</span>
                        </div>
                        <div class="metric-item">
                            <span>Response Time:</span>
                            <span class="metric-value">0.001s</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SVM -->
            <div class="col-md-6 col-lg-4" data-aos="zoom-in" data-aos-delay="400">
                <div class="card">
                    <div class="card-header">
                        <i class="fas fa-bolt model-icon"></i> SVM
                    </div>
                    <div class="card-body">
                        <div class="metric-item">
                            <span>F1-Score:</span>
                            <span class="metric-value">0.818</span>
                        </div>
                        <div class="metric-item">
                            <span>Precision:</span>
                            <span class="metric-value">0.812</span>
                        </div>
                        <div class="metric-item">
                            <span>Recall:</span>
                            <span class="metric-value">0.824</span>
                        </div>
                        <div class="metric-item">
                            <span>Accuracy:</span>
                            <span class="metric-value">82.9%</span>
                        </div>
                        <div class="metric-item">
                            <span>MCC-Score:</span>
                            <span class="metric-value">0.656</span>
                        </div>
                        <div class="metric-item">
                            <span>Brier-Score:</span>
                            <span class="metric-value">0.127</span>
                        </div>
                        <div class="metric-item">
                            <span>FPR:</span>
                            <span class="metric-value">0.168</span>
                        </div>
                        <div class="metric-item">
                            <span>Response Time:</span>
                            <span class="metric-value">0.120s</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Decision Tree -->
            <div class="col-md-6 col-lg-4" data-aos="zoom-in" data-aos-delay="500">
                <div class="card">
                    <div class="card-header">
                        <i class="fas fa-network-wired model-icon"></i> Decision Tree
                    </div>
                    <div class="card-body">
                        <div class="metric-item">
                            <span>F1-Score:</span>
                            <span class="metric-value">0.746</span>
                        </div>
                        <div class="metric-item">
                            <span>Precision:</span>
                            <span class="metric-value">0.710</span>
                        </div>
                        <div class="metric-item">
                            <span>Recall:</span>
                            <span class="metric-value">0.786</span>
                        </div>
                        <div class="metric-item">
                            <span>Accuracy:</span>
                            <span class="metric-value">75.0%</span>
                        </div>
                        <div class="metric-item">
                            <span>MCC-Score:</span>
                            <span class="metric-value">0.504</span>
                        </div>
                        <div class="metric-item">
                            <span>Brier-Score:</span>
                            <span class="metric-value">0.250</span>
                        </div>
                        <div class="metric-item">
                            <span>FPR:</span>
                            <span class="metric-value">0.282</span>
                        </div>
                        <div class="metric-item">
                            <span>Response Time:</span>
                            <span class="metric-value">0.004s</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CNN -->
            <div class="col-md-6 col-lg-4" data-aos="zoom-in" data-aos-delay="600">
                <div class="card">
                    <div class="card-header">
                        <i class="fas fa-brain model-icon"></i> CNN
                    </div>
                    <div class="card-body">
                        <div class="metric-item">
                            <span>F1-Score:</span>
                            <span class="metric-value">0.820</span>
                        </div>
                        <div class="metric-item">
                            <span>Precision:</span>
                            <span class="metric-value">0.807</span>
                        </div>
                        <div class="metric-item">
                            <span>Recall:</span>
                            <span class="metric-value">0.832</span>
                        </div>
                        <div class="metric-item">
                            <span>Accuracy:</span>
                            <span class="metric-value">82.9%</span>
                        </div>
                        <div class="metric-item">
                            <span>MCC-Score:</span>
                            <span class="metric-value">0.657</span>
                        </div>
                        <div class="metric-item">
                            <span>Brier-Score:</span>
                            <span class="metric-value">0.127</span>
                        </div>
                        <div class="metric-item">
                            <span>FPR:</span>
                            <span class="metric-value">0.174</span>
                        </div>
                        <div class="metric-item">
                            <span>Response Time:</span>
                            <span class="metric-value">0.419s</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <h2 data-aos="fade-right">4. Key Features</h2>
        <p data-aos="fade-up">Feature importance analysis revealed the following attributes as most significant in determining credit card approval decisions:</p>
        
        <div class="timeline-item" data-aos="fade-up" data-aos-delay="100">
            <h5>Feature Importance Analysis</h5>
            <div class="img-container">
                <img src="feature_importance.png" alt="Feature importance" class="img-fluid">
            </div>
        </div>
        
        <div class="row mt-4">
            <div class="col-md-6" data-aos="fade-up">
                <h5>Top Predictive Features</h5>
                <ul class="feature-list">
                    <li><strong>Status:</strong> Current account status</li>
                    <li><strong>Purpose:</strong> Intended use of credit</li>
                    <li><strong>Other_debtors:</strong> Other debt obligations</li>
                    <li><strong>Duration:</strong> Loan duration in months</li>
                    <li><strong>Credit_history:</strong> Past credit performance</li>
                </ul>
            </div>
            <div class="col-md-6" data-aos="fade-up" data-aos-delay="100">
                <h5>Feature Implications</h5>
                <p>These features align with traditional credit scoring factors while also revealing some less obvious but statistically significant predictors. The prominence of 'Status' and 'Credit_history' confirms the importance of existing financial behavior in predicting future creditworthiness.</p>
            </div>
        </div>

        <h2 data-aos="fade-right">5. Discussion</h2>
        <div data-aos="fade-up">
            <h5>Model Performance Analysis</h5>
            <p>The hybrid approach of using traditional machine learning and deep learning ensures robustness across:</p>
            <ul>
                <li><strong>Small sample sizes:</strong> Tree-based models performed particularly well</li>
                <li><strong>Complex feature interactions:</strong> XGBoost and CNN excelled here</li>
                <li><strong>Noisy data tolerance:</strong> Random Forest showed strong resilience</li>
            </ul>
            
            <h5 class="mt-4">Key Findings</h5>
            <p>XGBoost's regularization techniques (L1 and L2) prevent overfitting, making it highly suitable for financial data that often contains noise. While CNNs showed strong results, their operational cost in production environments was higher, making traditional ML models more preferable unless computational resources are abundant.</p>
            
            <h5 class="mt-4">Actionable Insights</h5>
            <div class="row">
                <div class="col-md-6">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h6><i class="fas fa-cogs text-primary"></i> Model Deployment</h6>
                            <p>Deploy XGBoost with real-time inferencing capabilities given its balance of accuracy and efficiency.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h6><i class="fas fa-sliders-h text-primary"></i> Feature Engineering</h6>
                            <p>Focus efforts on the most important attributes, removing redundant ones to simplify the model.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h6><i class="fas fa-chart-line text-primary"></i> Monitoring</h6>
                            <p>Set up automated model monitoring pipelines to detect and address performance degradation.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h6><i class="fas fa-comment-alt text-primary"></i> Explainability</h6>
                            <p>Integrate SHAP values or LIME for better customer communication and regulatory compliance.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <h2 data-aos="fade-right">6. Conclusion & Recommendations</h2>
        <div data-aos="fade-up">
            <p>Machine learning has demonstrated its capability to revolutionize credit card evaluation processes. This study found that XGBoost outperformed all other models, achieving an impressive accuracy of 87.9%, while Random Forest and CNN models also exhibited strong predictive abilities.</p>
            
            <div class="card bg-light mt-4">
                <div class="card-body">
                    <h5><i class="fas fa-lightbulb text-warning"></i> Key Recommendations</h5>
                    <ol>
                        <li><strong>Production Implementation:</strong> Deploy XGBoost as the primary scoring model with fallback to Random Forest for edge cases.</li>
                        <li><strong>Feature Optimization:</strong> Streamline data collection to focus on the top 5 predictive features.</li>
                        <li><strong>Continuous Monitoring:</strong> Implement automated drift detection for both data and model performance.</li>
                        <li><strong>Customer Experience:</strong> Simplify application forms to include only essential questions based on key features.</li>
                        <li><strong>Regulatory Compliance:</strong> Develop model explainability reports using SHAP values for audit purposes.</li>
                    </ol>
                </div>
            </div>
            
            <p class="mt-4">Future work should focus on enhancing interpretability, automating feature selection, handling data drift, and optimizing models for low-latency deployments. The use of intelligent, data-driven decision-making processes in credit evaluation not only improves approval accuracy but also drives better customer experiences and financial outcomes.</p>
        </div>
    </section>

    <footer data-aos="fade-up">
        <div class="footer-content">
            <span>© 2025 Credit Evaluation Report</span>
            <div class="ms-4">
                <a href="#" class="footer-icon"><i class="fab fa-github"></i></a>
                <a href="#" class="footer-icon"><i class="fab fa-linkedin"></i></a>
                <a href="#" class="footer-icon"><i class="fas fa-envelope"></i></a>
            </div>
        </div>
    </footer>
</div>

<!-- Scripts -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script>
    AOS.init({
        duration: 1000,
        once: true,
        easing: 'ease-in-out'
    });
</script>

</body>
</html>
"""

# Streamlit app
def main():
    st.set_page_config(layout="wide")
    
    # Inject CSS
    st.markdown(css, unsafe_allow_html=True)
    
    # Display HTML
    html(html_content, width=None, height=2000, scrolling=True)
    
    # Add interactive Streamlit elements
    with st.sidebar:
        st.header("Model Controls")
        selected_model = st.selectbox("Select Model", ["XGBoost", "Random Forest", "CNN"])
        
        if st.button("Run Analysis"):
            st.success(f"Running {selected_model} analysis...")

if __name__ == "__main__":
    main()
