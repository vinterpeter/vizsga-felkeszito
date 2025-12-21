#!/usr/bin/env python3
"""
Generate embeddings for all flashcards, quiz questions, and markdown content.
Uses sentence-transformers with a multilingual model.

Install dependencies:
    pip install sentence-transformers

Run:
    python generate_embeddings.py
"""

import json
import os
from sentence_transformers import SentenceTransformer

# Use multilingual model that works well with Hungarian
MODEL_NAME = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'

# Paths
BASE_PATH = '/Users/peter/work/notes/Tananyag'
OUTPUT_PATH = '/Users/peter/work/példa-app/embeddings.json'

CHAPTERS = {
    "Vezetéselmélet": "02-Vezeteselmellet_altalanos_ismeretek",
    "Harcászat": "03-Harcaszat",
    "Törzsszolgálati ismeretek": "04-Torzsszolgalati_ismeretek",
    "Harci támogatás": "05-Harci_tamogatas",
    "Harci kiszolgáló támogatás": "06-Harci_kiszolgalo_tamogatas",
    "Katonai tereptan": "07-Katonai_tereptan",
    "MH haditechnikai eszközei": "08-MH_haditechnikai_eszkozei"
}

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print(f"Loading model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    all_items = []

    # Process each chapter
    for chapter_name, folder_name in CHAPTERS.items():
        chapter_path = os.path.join(BASE_PATH, folder_name)
        print(f"\nProcessing: {chapter_name}")

        # Load flashcards
        flashcards_path = os.path.join(chapter_path, 'flashcards.json')
        if os.path.exists(flashcards_path):
            data = load_json(flashcards_path)
            for card in data.get('cards', []):
                # Combine front and back for embedding
                text = f"{card['front']} {card['back']}"
                all_items.append({
                    'type': 'flashcard',
                    'chapter': chapter_name,
                    'id': card['id'],
                    'front': card['front'],
                    'back': card['back'],
                    'text': text
                })
            print(f"  - {len(data.get('cards', []))} flashcards")

        # Load quiz questions
        quiz_path = os.path.join(chapter_path, 'quiz.json')
        if os.path.exists(quiz_path):
            data = load_json(quiz_path)
            for q in data.get('questions', []):
                # Combine question, correct answer, and explanation
                correct_answer = q['answers'][q['correct']] if q['correct'] < len(q['answers']) else ''
                text = f"{q['question']} {correct_answer} {q.get('explanation', '')}"
                all_items.append({
                    'type': 'quiz',
                    'chapter': chapter_name,
                    'id': q['id'],
                    'question': q['question'],
                    'answers': q['answers'],
                    'correct': q['correct'],
                    'explanation': q.get('explanation', ''),
                    'text': text
                })
            print(f"  - {len(data.get('questions', []))} quiz questions")

    print(f"\nTotal items: {len(all_items)}")
    print("Generating embeddings...")

    # Generate embeddings in batches
    texts = [item['text'] for item in all_items]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    # Add embeddings to items and remove the full text (to save space)
    for i, item in enumerate(all_items):
        item['embedding'] = embeddings[i].tolist()
        del item['text']  # Remove text to save space

    # Save to JSON
    output_data = {
        'model': MODEL_NAME,
        'items': all_items
    }

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False)

    file_size = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
    print(f"\nSaved to: {OUTPUT_PATH}")
    print(f"File size: {file_size:.2f} MB")

if __name__ == '__main__':
    main()
