<<<<<<< HEAD
# 📮 PhilatelyAI — The Offline Stamp Appraiser & Marketplace Draft Generator
*A Hacktoberfest 2026 Submission for the "Side Hustle" & "Best Use of Gemma" categories.*

## The Hustle: The High-Value Privacy Problem
High-end stamp collectors, dealers, and auction houses (like the Philatelic Collectors of Ahmedabad) sit on thousands of unlisted, uncataloged assets. Digitizing these collections to sell on platforms like eBay or Delcampe is incredibly tedious. 

However, **collectors refuse to upload high-resolution scans of valuable, unlisted assets to untrusted cloud APIs** due to privacy and security concerns. 

**PhilatelyAI solves this.** It is a 100% offline, privacy-first desktop application that uses open-weight vision models to instantly appraise stamps, extract multilingual text/postmarks, and generate SEO-optimized marketplace listing drafts without ever connecting to the internet. The user keeps complete control of their data.

## Best Use of Gemma: Why Open Innovation Matters
General-purpose APIs are too expensive for bulk inventory processing and violate the strict data privacy requirements of niche collectors. 

This project uses Google's natively multimodal **Gemma 4 (gemma4:e4b)** running entirely locally via Ollama on an AMD RX 580 GPU. 
*   **Zero Inference Cost:** 100% profit margin per software license sold to dealers.
*   **Complete Offline Privacy:** Keeps unlisted assets off external servers.
*   **Niche Accuracy:** Gemma 4 effortlessly reads microscopic multilingual inscriptions (like Hindi and English on Indian stamps) and detects postmark degradation.

## Features
*   **Local Vision-Language Inference:** Powered by `gemma4:e4b`.
*   **Marketplace Listing Generator:** Instantly drafts SEO-optimized titles and descriptions for Delcampe or eBay.
*   **Structured Data Export:** Generates standardized JSON metadata (Denomination, Condition, Year, Theme) for bulk inventory management.
*   **Claymorphism UI:** A clean, modern drag-and-drop interface built with FastAPI and HTML/CSS.

## Installation & Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
=======
# 📮 PhilatelyAI — The Offline Stamp Appraiser & Marketplace Draft Generator
*A Hacktoberfest 2026 Submission for the "Side Hustle" & "Best Use of Gemma" categories.*

## The Hustle: The High-Value Privacy Problem
High-end stamp collectors, dealers, and auction houses (like the Philatelic Collectors of Ahmedabad) sit on thousands of unlisted, uncataloged assets. Digitizing these collections to sell on platforms like eBay or Delcampe is incredibly tedious. 

However, **collectors refuse to upload high-resolution scans of valuable, unlisted assets to untrusted cloud APIs** due to privacy and security concerns. 

**PhilatelyAI solves this.** It is a 100% offline, privacy-first desktop application that uses open-weight vision models to instantly appraise stamps, extract multilingual text/postmarks, and generate SEO-optimized marketplace listing drafts without ever connecting to the internet. The user keeps complete control of their data.

## Best Use of Gemma: Why Open Innovation Matters
General-purpose APIs are too expensive for bulk inventory processing and violate the strict data privacy requirements of niche collectors. 

This project uses Google's natively multimodal **Gemma 4 (gemma4:e4b)** running entirely locally via Ollama on an AMD RX 580 GPU. 
*   **Zero Inference Cost:** 100% profit margin per software license sold to dealers.
*   **Complete Offline Privacy:** Keeps unlisted assets off external servers.
*   **Niche Accuracy:** Gemma 4 effortlessly reads microscopic multilingual inscriptions (like Hindi and English on Indian stamps) and detects postmark degradation.

## Features
*   **Local Vision-Language Inference:** Powered by `gemma4:e4b`.
*   **Marketplace Listing Generator:** Instantly drafts SEO-optimized titles and descriptions for Delcampe or eBay.
*   **Structured Data Export:** Generates standardized JSON metadata (Denomination, Condition, Year, Theme) for bulk inventory management.
*   **Claymorphism UI:** A clean, modern drag-and-drop interface built with FastAPI and HTML/CSS.

## Installation & Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
>>>>>>> 8accd92f03b4e365a4f61d2906f867d0afae1640
