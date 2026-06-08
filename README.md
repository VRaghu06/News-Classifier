# News Classifier

## Overview

This project retrieves news articles at real time using the Real-Time News Data API, and can either output just the titles based on the search query provided, or could also categorize the articles from a wide array of topics, such as business, politics, sports, entertainment etc. 

The application itself is built using FastAPI, and exposes REST endpoints that accept a search query and an optional limit query, and can either return the categorized news titles as well as the category they belong to, or just the news titles, depending on what the user chooses.   

---

## Features

- Real-time news retrieval
- Transformer based text classification
- FastAPI structure
- Multiple RestAPI endpoints
- Interactive API documentation
- Users choice on what output they want
- JSON responses

---

## How it works

1. User chooses between the categorized news endpoint or title retrieval endpoint
2. User submits a search query and an optional limit query to either endpoint
3. Article titles are returned as JSON if the title retrieval endpoint is chosen
4. If the classified news endpoint is chosen, the article's title and snippet is passed to a transformer model
5. The transformer model uses zero-shot classification to categorize the articles
6. The article data + category are returned as JSON data

---

## Example Request

GET/news/Lebron James?limit=3 - for the title retrieval endpoint with three article titles returned
GET/classified-news/Lady Gaga - for the classified news endpoint, with the default option of 5 articles being returned

---

## Example Response

Title Retrieval Example:

```json
{
  "title 1": "LeBron James’ message to Nelly Korda after U.S. Women’s Open win",
  "title 2": "Warriors' Best-Case Scenario This Offseason Might Not Be What You Think",
  "title 3": "Michael Wilbon: Jalen Brunson, LeBron James not in same group as Kobe Bryant"
}
```

Classified news Example:

```json
[
  {
    "text": "Lady Gaga Makeup Brand Faces Backlash Over Dark Skin Inclusivity A viral review from beauty creator Golloria George is putting Haus Labs' bronzer shades and inclusivity claims under renewed scrutiny.",
    "category": "business",
    "confidence": 0.795277833938599
  },
  {
    "text": "Lady Gaga ignites 2026 comeback tour and new music era Lady Gaga is gearing up a massive 2026 return with fresh tour plans, studio teasers, and a renewed pop vision fans in the US have waited years ...",
    "category": "entertainment",
    "confidence": 0.707522869110107
  },
  {
    "text": "‘We’re not Lady Gaga and Elton John’: unmasking Angine de Poitrine, the year’s buzziest, dottiest band 'We're not Lady Gaga and Elton John': unmasking Angine de Poitrine, the year's buzziest, dottiest band ... Recently, Angine de Poitrine had to get ...",
    "category": "entertainment",
    "confidence": 0.535648941993713
  },
  {
    "text": "Lady Gaga Reinvents Herself, Yet Again, With ‘Mayhem Requiem’ Performance: Review Lady Gaga brought her 'Mayhem' era to a close with a reinvention of the album and show.",
    "category": "entertainment",
    "confidence": 0.653221368789673
  },
  {
    "text": "Lady Gaga Releases New Live Album Mayhem Requiem Lady Gaga has released a new live project, Mayhem Requiem, via Apple Music. The album, which was recorded during a no-phones-allowed show at ...",
    "category": "entertainment",
    "confidence": 0.508282065391541
  }
]
```

Refer to the screenshots in the screenshots folder to see the interactive docs version

---

## Installation

```bash
git clone <repository-url >
cd News-Topic-Classifier

pip install -r requirements.txt
```

---

## Running the application

```bash
fastapi dev classifier.py
```

Visit:

```text
http://localhost:8000/docs
```


