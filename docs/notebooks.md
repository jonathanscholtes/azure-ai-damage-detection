## 📘 Notebooks — Detecting Vehicle Damage with Semantic Kernel

This section provides a set of Jupyter notebooks demonstrating how to build and run a **few-shot Azure AI Agent** using **Semantic Kernel** to detect vehicle damage from before-and-after images.

---

## 📥 Download Notebooks

Once your environment is ready, download the notebooks directly from GitHub:

Once your environment is up and running, you can download the notebooks directly from the GitHub repository using the following commands:

```bash
curl -L https://github.com/jonathanscholtes/azure-ai-damage-detection/archive/refs/heads/main.zip -o detection.zip
unzip detection.zip
mv azure-ai-damage-detection-main/src/Notebooks ./Notebooks
rm -rf azure-ai-damage-detection-main detection.zip
```

This approach downloads only the relevant [src/Notebooks](../src/Notebooks) directory, keeping your workspace clean and lightweight.

---


### ⚙️ Configure Your Environment

To connect your notebooks to your Azure AI resources, create a .env file with your specific service credentials.

#### Steps:

1. Copy `sample.env` to a new file named `.env`
2. Replace the placeholder values with your Azure resource info:

```
# Azure AI Project
PROJECT_ENDPOINT=''
AZURE_OPENAI_ENDPOINT='Endpoint from deployed Azure AI Service or Azure OpenAI Service'
AZURE_OPENAI_API_KEY='Key from deployed Azure AI Service or Azure OpenAI Service'
AZURE_OPENAI_CHAT_MODEL='gpt-4o'
AZURE_OPENAI_API_VERSION='2025-01-01-preview'

```
<br/>

3. Create an Environment for Notebooks:

Navigate to the Notebook directory src/Notebooks and follow these steps:

- Create a Python Virtual Environment

```bash
python -m venv venv
```

- Activate the Virtual Environment and Install Dependencies:

```bash
venv\Scripts\activate # On macOS/Linux, use `source venv/bin/activate`
python -m pip install -r requirements.txt
```


## 🖼️ Image Preprocessing

This project includes example data for few-shot prompts and damage detection.  
However, all images must be scaled to a consistent resolution (`1536x1024`) for accurate results.

Run the preprocessor script from `src/Notebooks` to generate the scaled images in `data/transformed`:


```
python preprocess_images.py
```
This will resize and normalize all images from data/raw into a standardized format used by the notebooks.

--- 

## 📓 Available Notebook

| Notebook | Description |
|-----------|--------------|
| **01_semantic_kernel_damage_detection.ipynb** | A complete walkthrough demonstrating how to build a few-shot Semantic Kernel agent in Azure AI Foundry for vehicle damage detection using GPT-4o. The notebook covers image preprocessing, example loading, agent creation, and structured JSON output generation for before-and-after image comparisons. |


