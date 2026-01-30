👔 Formal Attire Assessment Model
📌 Overview

The Formal Attire Assessment Model is designed to automatically evaluate the user’s clothing during a mock interview session. Since a candidate’s attire plays a crucial role in forming a strong first impression, especially in professional environments, this model aims to determine whether the user’s outfit is appropriate for a formal interview setting.

The model classifies attire into two main categories:

Formal

Not Formal

The analysis is applied to extracted video frames after the interview session, and the results are integrated into the overall system feedback to help users improve their professional appearance and interview readiness.

🎯 Objectives

This model helps to:

Encourage candidates to wear professional and suitable interview attire.

Provide objective, automated feedback regarding appearance.

Ensure that non-verbal communication cues, such as clothing style, align with professional interview expectations.

Improve the overall interview performance evaluation system.

🛠 Tools & Technologies

YOLO (You Only Look Once):
Used for real-time object detection to identify clothing items in video frames.

OpenCV:
Utilized to extract 10 random frames from the interview video for efficient and representative analysis.

Python:
Used for post-processing, classification logic, and system integration.

📂 Dataset & Model Architecture
Dataset

Fashionpedia Dataset
A large-scale, richly annotated fashion dataset containing a wide variety of clothing categories.

Provides:

Detailed garment annotations

High-quality labeled images

Multiple clothing styles and contexts

Model Architecture

A YOLO-based pre-trained object detection model is used to detect clothing items in each video frame.

The detected garments are passed through a post-processing classification logic that determines whether each item belongs to the formal attire category.

⚙️ Attire Classification Logic

Each detected clothing item is categorized as Formal or Not Formal based on predefined professional dress standards:

Examples of Formal Attire

Shirt

Jacket / Blazer

Suit

Formal Pants

Tie

Examples of Not Formal Attire

T-shirts

Hoodies

Shorts

Casual wear

Sportswear

A final decision is obtained using majority voting across the analyzed frames.

📊 Model Performance
Metric	Value
Accuracy	90%

Conclusion:
The achieved accuracy demonstrates that the model is highly effective in identifying formal attire, making it suitable for real-world interview assessment scenarios.
