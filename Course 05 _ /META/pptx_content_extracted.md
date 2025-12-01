# PPTX Content Extraction Summary

## Extracted Files

### 01.pptx

- **Number of Slides:** 24

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Automated Workflows in the Cloud

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:
Define cloud automation and its key components.
Design workflows using serverless architectures (e.g., AWS Step Functions, Azure Logic Apps).
Implement CI/CD pipelines for ML models...

#### Slide 4

**Title:** Introduction to Automation in the Cloud

**Content:**
- Introduction to Automation in the Cloud...
- What are Automated Workflows?
Automated workflows are sequences of tasks and processes that are triggered and executed automatically using predefined rules or events in cloud environments.
They elimin...

#### Slide 5

**Title:** Common Examples:

**Content:**
- Common Examples:...
- Note: Tools like AWS CloudFormation, Terraform, Ansible, 
and CI/CD pipelines (Jenkins, GitHub Actions) play key roles in automating cloud environments....

*... and 19 more slides*

---

### 02.pptx

- **Number of Slides:** 26

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Cloud Collaboration Tools

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:
Understand what cloud collaboration tools are and why they are important.
Identify popular cloud collaboration platforms and their core features.
Compare different tools based on fu...

#### Slide 4

**Title:** Introduction to Cloud Collaboration

**Content:**
- Introduction to Cloud Collaboration...
- What is Cloud Collaboration?
Cloud Collaboration refers to the practice of using cloud computing technologies that allow multiple people to:
Work together on documents, files, or projects
Access and e...

#### Slide 5

**Title:** Why Use Cloud Collaboration Tools?

**Content:**
- Why Use Cloud Collaboration Tools?...
- 1. Supports Remote and Hybrid Work Models
With more people working from home or from different locations, cloud tools ensure everyone stays connected and productive.
2. Facilitates Teamwork Across Geo...

*... and 21 more slides*

---

### 03.pptx

- **Number of Slides:** 23

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Unit 5: Cloud Infrastructure & Production Deployment

**Content:**
- Cloud Storage Fundamentals & Running Your First Cloud Analysis...
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:

Define cloud storage and its core components.
Compare different cloud storage types (object, block, file).
Explain key cloud storage features (durability, availability, scalability...

#### Slide 4

**Title:** Introduction to Cloud Storage

**Content:**
- Introduction to Cloud Storage...
- What is Cloud Storage?
Cloud storage is a service model in which data is maintained, managed, backed up remotely, and made available to users over a network (typically the internet).
Explanation in s...

#### Slide 5

**Title:** How Does Cloud Storage Work?

**Content:**
- How Does Cloud Storage Work?...
- Data is Sent to Data Centers Using the InternetWhen you upload a file (like a photo or document), it travels through the internet to a remote server (computer) located in a data center  a secure faci...

*... and 18 more slides*

---

### 04.pptx

- **Number of Slides:** 14

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** cuDF: Understsanding performance

**Content:**
- Correct the code...
- By: Dr. Afshan Hashmi...

#### Slide 3

**Title:** Course Objectives:
Learners will be able to identify the performance issue
Learners will be able to Fix the issue in the code

#### Slide 4

**Title:** Avoiding Unnecessary to_pandas() Calls

Question: The following code converts a cuDF DataFrame to Pandas unnecessarily, causing performance issues. Correct the code to improve performance.

**Content:**
- import cudf

df = cudf.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]})

# Inefficient approach
df_pandas = df.to_pandas()
df_pandas['c'] = df_pandas['a'] + df_pandas['b']
df = cudf.DataFrame.from_pa...
- Hint: Perform operations directly on the cuDF DataFrame....

#### Slide 5

**Title:** 1. Avoiding Unnecessary to_pandas() Calls- Corrected code

**Content:**
- By performing the addition directly on the cuDF DataFrame, we avoid converting it to Pandas, thus improving performance....
- import cudf

df = cudf.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]})

# Correct approach: Perform operations directly on the cuDF DataFrame
df['c'] = df['a'] + df['b']

print(df)...

*... and 9 more slides*

---

### 05.pptx

- **Number of Slides:** 24

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** cuML for GPU-accelerated machine learning

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:

Understand GPU-Accelerated Machine Learning – Learn how to leverage RAPIDS cuML for high-performance machine learning on large datasets, comparing it with traditional CPU-based app...

#### Slide 4

**Title:** Introduction to cuML(RAPIDS Machine Learning Library)

**Content:**
- Introduction to cuML(RAPIDS Machine Learning Library)...
- What is cuML?
cuML is an open-source GPU-accelerated machine learning library developed by NVIDIA as part of the RAPIDS AI framework. It provides highly optimized implementations of common machine lea...
- cuML
Rapids Machine Learning Library...

#### Slide 5

**Title:** cuML overview

**Content:**
- cuML overview...
- cuML is a machine learning library developed by NVIDIA as part of the RAPIDS ecosystem.
Its main goal is to accelerate traditional machine learning algorithms using GPU computing.
cuML offers GPU-acce...

*... and 19 more slides*

---

### 06.pptx

- **Number of Slides:** 17

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** cuML: open-source GPU-accelerated machine learning library

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:

Understand GPU-Accelerated Machine Learning – Learn how to leverage RAPIDS cuML for high-performance machine learning on large datasets, comparing it with traditional CPU-based app...

#### Slide 4

**Title:** Introduction to cuML(RAPIDS Machine Learning Library)

**Content:**
- Introduction to cuML(RAPIDS Machine Learning Library)...
- What is cuML?
cuML is an open-source GPU-accelerated machine learning library developed by NVIDIA as part of the RAPIDS AI framework. It provides highly optimized implementations of common machine lea...
- cuML
Rapids Machine Learning Library...

#### Slide 5

**Title:** cuML-Supported Algorithms

**Content:**
- cuML provides GPU-accelerated implementations of various machine learning algorithms, including:

Linear Models: Linear Regression, Ridge Regression, Lasso Regression

Clustering: K-Means, DBSCAN

Dim...

*... and 12 more slides*

---

### 07.pptx

- **Number of Slides:** 17

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Data visualization

**Content:**
- With Seaborn and Matplotlib...
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:
Learn the fundamentals of data visualization using Matplotlib and Seaborn.
Create static, animated, and interactive plots for data analysis.
Utilize Seaborn for statistical and enha...

#### Slide 4

**Title:** Matplotlib and Seaborn for Data Visualization

**Content:**
- Matplotlib and Seaborn for Data Visualization...
- Data visualization is crucial in scalable data science for understanding trends, distributions, and relationships. 

Matplotliband Seaborn are two powerful Python libraries that provide extensive func...

#### Slide 5

**Title:** Matplotlib

**Content:**
- Matplotlib...
- Introduction to Matplotlib: Matplotlib is a fundamental library for creating static, animated, and interactive visualizations. It provides fine-grained control over plots, making it highly customizabl...

*... and 12 more slides*

---

### 08.pptx

- **Number of Slides:** 58

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Deploying GPU-accelerated data pipelines

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:

Understand the architecture and benefits of GPU-accelerated computing
Design efficient data pipelines for GPU processing
Implement GPU-accelerated data transformations
Optimize pip...

#### Slide 4

**Title:** Fundamentals of GPU Computing

#### Slide 5

**Title:** Introduction to GPU Architecture

**Content:**
- Introduction to GPU Architecture...
- What is a GPU?

GPU stands for Graphics Processing Unit.
Originally designed for rendering images and video.
Now widely used for parallel computation in scientific computing, deep learning, etc.

Orig...

*... and 53 more slides*

---

### 09.pptx

- **Number of Slides:** 29

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Distributed ML with Spark MLlib

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:

Understand the fundamentals of distributed computing
Gain hands-on experience with Spark MLlib, 
Explore and implement supervised and unsupervised machine learning algorithms 
Lear...

#### Slide 4

**Title:** Introduction to Distributed Machine Learning

**Content:**
- Introduction to Distributed Machine Learning...
- What is Distributed Machine Learning?
Distributed Machine Learning (Distributed ML) is a technique where the training and processing of machine learning models are spread across multiple computers (al...

#### Slide 5

**Title:** Why Use Distributed ML?

**Content:**
- Why Use Distributed ML?...
- In today's world, machine learning models often deal with:
Massive datasets (like millions of images or billions of rows of user data).
Complex models (like deep neural networks with millions of param...

*... and 24 more slides*

---

### 10.pptx

- **Number of Slides:** 31

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** cuDF: GPU-accelerated Data Manipulation

**Content:**
- Overview and Comparison with Pandas...
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:
This course aims to equip learners with GPU-accelerated data analysis skills using cuDF, Pandas. Students will learn how to efficiently manipulate, clean, and analyze large datasets...

#### Slide 4

**Title:** Introduction to cuDF

**Content:**
- What is cuDF?
cuDF is a GPU DataFrame library for loading, joining, aggregating, filtering, and otherwise manipulating data.
GPU-accelerated library for data manipulation.
Part of the RAPIDS ecosystem...

#### Slide 5

**Title:** Key Features of cuDF

**Content:**
- GPU-accelerated DataFrame operations.
Similar API to Pandas for ease of use.
Seamless integration with other RAPIDS libraries (cuML, cuGraph).
Support for CSV, Parquet, and ORC file formats....

*... and 26 more slides*

---

### 11.pptx

- **Number of Slides:** 18

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Unit 5: Cloud Infrastructure & Production Deployment

**Content:**
- Introduction to Cloud Computing...
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:

Define cloud computing and its key characteristics.
Compare different cloud service models (IaaS, PaaS, SaaS).
Explain the benefits and challenges of cloud computing.
Identify majo...

#### Slide 4

**Title:** Introduction to Cloud Computing 

**Content:**
- Introduction to Cloud Computing...
- Cloud computing is the delivery of computing services—such as servers, storage, databases, networking, software, analytics, and intelligence—over the Internet ("the cloud") to offer faster innovation,...

#### Slide 5

**Title:** 

**Content:**
- Cloud Service Models:...

*... and 13 more slides*

---

### 12.pptx

- **Number of Slides:** 32

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Model Training on Large Datasets

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:
Understand the challenges of training models on large datasets
Apply best practices for handling large data efficiently
Choose the right tools and infrastructure (e.g., distributed ...

#### Slide 4

**Title:** Introduction to Large-Scale Model Training

**Content:**
- Introduction to Large-Scale Model Training...
- Why Large-Scale Training Matters
Modern datasets exceed single-machine memory (e.g., TB-scale images, logs)
Need for faster iteration in production ML systems
Regulatory/compliance requirements for mo...
- Key Challenges...

#### Slide 5

**Title:** Strategies for Efficient Training

**Content:**
- 1.Data Sampling and Mini-Batching
These are techniques used to efficiently train machine learning models, especially when dealing with large datasets that can't fit into memory all at once.
A. Train o...

*... and 27 more slides*

---

### 13.pptx

- **Number of Slides:** 14

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** cuDF: Understsanding performance and visualization

**Content:**
- Analyzing Performance by profiling utilities...
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:
To introduce the fundamentals of cudf.pandas and its role in accelerating data processing using GPUs.
To equip learners with profiling techniques for optimizing performance and iden...

#### Slide 4

**Title:** Numba: Just-In-Time (JIT) Compilation for Speeding Up Python Code

**Content:**
- Numba: Just-In-Time (JIT) Compilation for Speeding Up Python Code...
- Numba is a Python library that accelerates code execution using JIT compilation.

Converts Python code into machine code at runtime for improved performance.

It is particularly useful for speeding up...

#### Slide 5

**Title:** Why Use Numba?

**Content:**
- Benefits:
Speed: Dramatically improves performance of numerical computations.
Simplicity: Requires only a decorator to optimize functions.
Flexibility: Works with existing Python code and libraries.
U...

*... and 9 more slides*

---

### 14.pptx

- **Number of Slides:** 28

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** Scaling Scikit-learn with Joblib and Dask

**Content:**
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:

Understand the limitations of scikit-learn when working with large datasets or complex pipelines.
Learn how to implement parallel computing in scikit-learn using Joblib for efficie...

#### Slide 4

**Title:** Introduction

**Content:**
- Introduction...
- Scikit-learn is one of the most widely used machine learning libraries in Python, offering simple and efficient tools for data mining and analysis. However, when working with large datasets or computa...

#### Slide 5

**Title:** Why Scaling is Needed in Scikit-learn

**Content:**
- Why Scaling is Needed in Scikit-learn...
- Limited Scope for Big Data: Scikit-learn is optimized for small to medium datasets; it can struggle with memory and computation when working with large-scale data.
Lack of Built-in Parallelism: Most m...

*... and 23 more slides*

---

### 15.pptx

- **Number of Slides:** 21

#### Slide 1

**Title:** أكـــــاديميــــة طــــويـــق

**Content:**
- Scalable Data Science...

#### Slide 2

**Title:** cuDF: Understsanding performance and visualization

**Content:**
- Analyzing Performance by profiling utilities...
- By: Dr. Afshan Hashmi...

#### Slide 3

**Content:**
- Course Objectives:
To introduce the fundamentals of cudf.pandas and its role in accelerating data processing using GPUs.
To equip learners with profiling techniques for optimizing performance and iden...

#### Slide 4

**Title:** Understanding the Basics

**Content:**
- When dealing with large datasets, processing speed is crucial. That's where GPUs (Graphics Processing Units) come in, as they're designed for parallel processing, which significantly accelerates data ...

#### Slide 5

**Title:** Understanding Performance in cudf.pandas

**Content:**
- cudf.pandas provides profiling utilities to help you analyze the performance of your code when working with GPU-accelerated data frames. 

These tools help determine which parts of your code ran on th...

*... and 16 more slides*

---

