> **⚠️ Active Development Notice**  
> This project is currently in active development and may contain breaking changes.  
> Updates and modifications are being made frequently, which may impact stability or functionality.  
> This notice will be removed once the project reaches a stable release.

# Azure AI Foundry Damage Detection Agent

An AI-powered **few-shot image comparison agent** built with **Azure AI Foundry** and **Semantic Kernel**.  
The agent compares two images of a vehicle (before and after) to detect visible damage such as dents, scratches, and cracks.  
It uses **few-shot examples** to improve consistency in reasoning and JSON output when identifying and localizing visible damage.

---

## Overview  

This project demonstrates how to use **Azure AI Agents** in **Azure AI Foundry** to perform visual reasoning tasks such as image comparison and structured extraction.  

The solution leverages **few-shot learning** with **Semantic Kernel** to provide the model with pre-labeled examples of vehicle images.  
These examples help the model learn how to identify visual differences and structure its JSON responses accurately for new image pairs.

The agent:
- Accepts two input images (`before` and `after`)  
- Detects visible vehicle damage (dents, scratches, cracks, deformations, etc.)  
- Outputs bounding boxes and confidence scores in **pixel coordinates**  
- Leverages **few-shot examples** to improve detection accuracy and JSON consistency  
- Returns structured JSON output that can be easily processed or visualized  

---

![design](/media/detection1.png)

---

## 🛠️ **Core Steps for Solution Implementation**

Follow these key steps to successfully deploy and configure the solution:

### 1️⃣ [**Deploy the Solution**](docs/deployment.md)
-  Instructions for deploying solution, including prerequisites, configuration steps.  

### 2️⃣ [**Hands-On Notebook: Damage Detection with Semantic Kernel**](docs/notebooks.md)
- Follow the guided notebook to create and test a few-shot Azure AI Agent that detects and describes vehicle damage using GPT-4o.



---

## ♻️ **Clean-Up**

After completing the workshop and testing, ensure you delete any unused Azure resources or remove the entire Resource Group to avoid additional charges.

---

## 📜 License  
This project is licensed under the [MIT License](LICENSE.md), granting permission for commercial and non-commercial use with proper attribution.

---

## Disclaimer  
This code and demo application are intended for educational and demonstration purposes. It is provided "as-is" without any warranties, and users assume all responsibility for its use.