# Mental-Health-Assistance-Project
**Project Overview:**

A mental-health counseling assistant fine-tuned from the Llama-2-7B model using a curated dataset of psychologist-verified Q&A pairs to deliver supportive, safe, and context-aware responses.

**Key Features**

- Fine-tuned Llama-2-7B using QLoRA and 4-bit quantization for efficient training
- Structured prompt format aligned with Llama’s conversational style
- Interactive chatbot interface built with ipywidgets
- Produces context-relevant mental-health guidance

**Technologies Used:**

- Llama-2-7B (Meta)
- QLoRA, BitsAndBytes (4-bit quantization)
- Hugging Face Transformers & Datasets
- Python, Jupyter Notebook
- Ipywidgets

**Model Overview:**

The model was trained on Amod/mental_health_counseling_conversations (3,512 Q&A pairs from counselchat.com), using Llama-specific formatted prompts for 3 epochs. The goal was to generate concise, supportive mental-health responses and redirect users to appropriate resources when needed.

**Challenges Encountered:**

- Occasionally short, repetitive, or vague responses
- Occasional hallucinations in advice
- Limited dataset size restricting diversity of counseling scenarios
- Basic UI constraints in ipywidgets

**Future Improvements:**

- Expand dataset with more diverse counseling cases
- Enhance prompt engineering and safety alignment
- Integrate a richer, more intuitive UI (web app / chatbot interface)
- Upgrade to higher-capacity models for better depth and nuance
