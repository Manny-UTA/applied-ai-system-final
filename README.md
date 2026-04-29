# 🎵 SmartTune AI: Explainable Music Recommender

## 📌 Summary

This project extends my **Music Recommender Simulation (Project 3)** into a full applied AI system.

The system recommends songs based on user preferences such as genre, mood, and energy level. It uses a scoring algorithm to rank songs and generates explanations for why each recommendation was selected.

This project demonstrates how AI systems can transform input data into ranked predictions while maintaining transparency and reliability.

---

## 🧠 AI Features

This system includes the following AI-inspired components:

- **Scoring Engine**: Evaluates how well each song matches user preferences
- **Explanation Generator**: Provides human-readable reasoning for each recommendation
- **Agentic Workflow**: Displays step-by-step reasoning (scoring → ranking → output)
- **Reliability System (Evaluation Script)**: Tests system performance across multiple user profiles

This satisfies the requirement for an integrated AI feature by demonstrating **automated decision-making, reasoning, and validation within a single pipeline**.

---

## 🏗️ System Architecture


User Input → Preference Parser → Scoring Engine → Ranking → Explanation Generator → Output → Evaluation


- **Input**: User preferences (genre, mood, energy)
- **Processing**: Scoring + ranking logic
- **Output**: Top recommendations with explanations
- **Evaluation**: Automated test system verifies correctness

---

## ⚙️ Setup Instructions

1. Clone the repository:

git clone https://github.com/Manny-UTA/applied-ai-system-final.git

cd applied-ai-system-final


2. Install dependencies:

pip install -r requirements.txt


3. Run the system:

python src/main.py


4. Run evaluation tests:

python evaluation.py


---

## 💻 Sample Output

Example input:
- genre = pop  
- mood = happy  
- energy = 0.7  

Output:
- Top 5 recommended songs  
- Scores and detailed explanations  

Evaluation Results:

PASS
PASS
PASS


---

## 🧪 Testing & Reliability

The system includes an automated evaluation script that tests multiple user profiles.

Results:
- 3/3 test cases passed  
- System consistently returned valid recommendations  
- Demonstrates reliability across different input scenarios  

Additionally, outputs were manually reviewed to confirm that recommendations align with user preferences.

---

## ⚖️ Design Decisions

- Used rule-based scoring instead of machine learning for interpretability
- Prioritized explainability to make decisions transparent
- Structured the system modularly for testing and scalability

---

## ⚠️ Limitations

- Limited dataset size may affect diversity of recommendations  
- No real-time learning or adaptive personalization  
- Relies on predefined scoring rules instead of trained models  

---

## 🧠 Reflection

This project reinforced that AI systems are not just about models, but about building **structured pipelines that process input, generate decisions, and validate outputs**.

I also learned the importance of combining automated testing with human judgment to ensure reliability.

---

## 🎥 Demo Video

[PASTE YOUR LOOM LINK HERE]

---

## 📁 Base Project

This project is based on my Project 3 Music Recommender Simulation, which originally implemented scoring and ranking logic without evaluation or system-level reasoning. This version expands it into a full applied AI system with testing, reasoning, and evaluation components.