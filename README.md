# SynapseChat  

SynapseChat is an AI chat application based on **PySide6**, integrating **OpenAI, Google Gemini, and Hugging Face Hub AI models**. It provides real-time interactions and streaming responses, making it suitable for researchers and developers working on AI applications.  

---

## Key Features  

- **AI Conversations**: Supports **ChatGPT-4o, Gemini-Pro, and various models from Hugging Face Hub**.  
- **Real-Time Streaming Responses**: ChatGPT-4o provides responses via streaming for an enhanced interactive experience.  
- **Model Search**: Built-in Hugging Face model search feature to quickly find AI models and open their web pages.  
- **Settings Management**: API key management for OpenAI, Google Gemini, and Hugging Face, making setup easy.  
- **Custom Hugging Face Model Library**: Users can input their own **Hugging Face model repository** and directly select it for chatting.  

---

## Installation & Usage  

### 1. Install Dependencies  

Ensure you have **Python 3.8+**, then run the following command to install the required dependencies:  

```sh
pip install -r requirements.txt
```  

**Main Dependencies**:  
- `PySide6`  
- `requests`  
- `python-dotenv`  
- `langchain`  
- `langchain-google-genai`  
- `huggingface_hub`  

---

### 2. Set Up API Keys & Hugging Face Model  

Create a `.env` file in the project root directory and enter your API keys and custom Hugging Face model repository:  

```
OPENAI_API_KEY=your_OpenAI_API_Key
GOOGLE_API_KEY=your_Gemini_API_Key
HF_TOKEN=your_Hugging_Face_Token
HF_MODEL_REPO=your_Hugging_Face_Model
```  

Alternatively, you can enter your **API keys** and **Hugging Face model repository** directly in the **Settings page** and save them.  

---

### 3. Run the Application  

```sh
python main.py
```  

---

## Interface Overview  

### **1. Home Screen**  
- The left sidebar provides **Home, Model Search, Chat, and Settings** pages.  
- The right side displays the corresponding content.  

### **2. Model Search**  
- Allows searching for **AI models on Hugging Face Hub**.  
- Clicking on a search result opens the model's Hugging Face page.  

### **3. Chat Room**  
- **Model Selection**: Switch between **ChatGPT-4o, Gemini, Zephyr-7B, Falcon-7B, Deepseek-Chat**, and other models.  
- **Real-Time Streaming**: Supports **ChatGPT-4o's** streaming responses.  
- **Clear Chat**: Enter `clear` to delete all messages.  
- **User-Customized Hugging Face Model Library**: Users can add and select their own Hugging Face models.  

### **4. Settings Page**  
- Input **API keys** for OpenAI, Google Gemini, and Hugging Face.  
- Configure the **Hugging Face Model Repository** to use custom models.  
- Click **Save API Keys** to store the settings.  

---

## Version History  

### **v1.1.0 (2025-02-04)**  
- Added **custom Hugging Face model library** support.  
- Improved UI design for a better user experience.  

### **v1.0.0 (2025-02-04)**  
- Initial release with core features.  
- Supports **ChatGPT-4o, Gemini-Pro, and Hugging Face Hub models**.  
- Provides **real-time streaming responses** and **model search**.  

---

## Developer  

**Tudo Tech** (c) 2025. All rights reserved.  

---

## Contribution  

We welcome issues and pull requests!  

1. Fork the repository  
2. Create a new branch (`git checkout -b new-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to your branch (`git push origin new-feature`)  
5. Submit a **Pull Request**  

---

## License  

This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---
