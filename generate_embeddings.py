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
import re
from sentence_transformers import SentenceTransformer

# Use multilingual model that works well with Hungarian
MODEL_NAME = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'

# Paths
BASE_PATH = '/Users/peter/work/notes/Tananyag'
MEDIA_PATH = '/Users/peter/work/példa-app/media'
OUTPUT_PATH = '/Users/peter/work/példa-app/embeddings.json'

CHAPTERS = {
    "Vezetéselmélet": {"folder": "02-Vezeteselmellet_altalanos_ismeretek", "id": "02"},
    "Harcászat": {"folder": "03-Harcaszat", "id": "03"},
    "Törzsszolgálati ismeretek": {"folder": "04-Torzsszolgalati_ismeretek", "id": "04"},
    "Harci támogatás": {"folder": "05-Harci_tamogatas", "id": "05"},
    "Harci kiszolgáló támogatás": {"folder": "06-Harci_kiszolgalo_tamogatas", "id": "06"},
    "Katonai tereptan": {"folder": "07-Katonai_tereptan", "id": "07"},
    "MH haditechnikai eszközei": {"folder": "08-MH_haditechnikai_eszkozei", "id": "08"}
}

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_markdown(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def split_markdown_into_sections(content, chapter_name):
    """Split markdown into sections based on headers."""
    sections = []

    # Split by ## headers (level 2)
    parts = re.split(r'\n(?=## )', content)

    section_id = 0
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Extract title from first line if it's a header
        lines = part.split('\n')
        title = ""
        text = part

        if lines[0].startswith('## '):
            title = lines[0].replace('## ', '').strip()
            # Remove markdown formatting from title
            title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title)
            title = re.sub(r'\*([^*]+)\*', r'\1', title)
        elif lines[0].startswith('# '):
            title = lines[0].replace('# ', '').strip()
            title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title)

        # Clean up markdown for embedding (remove images, links formatting, etc.)
        clean_text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # Remove images
        clean_text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean_text)  # Keep link text
        clean_text = re.sub(r'```[\s\S]*?```', '', clean_text)  # Remove code blocks
        clean_text = re.sub(r'`[^`]+`', '', clean_text)  # Remove inline code
        clean_text = re.sub(r'\n{3,}', '\n\n', clean_text)  # Normalize newlines
        clean_text = clean_text.strip()

        # Skip very short sections
        if len(clean_text) < 100:
            continue

        # If section is too long, split further by ### headers
        if len(clean_text) > 2000:
            subsections = re.split(r'\n(?=### )', part)
            for subsection in subsections:
                subsection = subsection.strip()
                if len(subsection) < 100:
                    continue

                sub_lines = subsection.split('\n')
                sub_title = title
                if sub_lines[0].startswith('### '):
                    sub_title = sub_lines[0].replace('### ', '').strip()
                    sub_title = re.sub(r'\*\*([^*]+)\*\*', r'\1', sub_title)

                # Clean subsection
                clean_sub = re.sub(r'!\[.*?\]\(.*?\)', '', subsection)
                clean_sub = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean_sub)
                clean_sub = re.sub(r'```[\s\S]*?```', '', clean_sub)
                clean_sub = re.sub(r'`[^`]+`', '', clean_sub)
                clean_sub = clean_sub.strip()

                if len(clean_sub) >= 100:
                    section_id += 1
                    sections.append({
                        'id': section_id,
                        'title': sub_title or f"Szakasz {section_id}",
                        'content': clean_sub[:1500],  # Limit content length
                        'text': clean_sub[:1500]
                    })
        else:
            section_id += 1
            sections.append({
                'id': section_id,
                'title': title or f"Szakasz {section_id}",
                'content': clean_text[:1500],
                'text': clean_text[:1500]
            })

    return sections

def main():
    print(f"Loading model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    all_items = []

    # Process each chapter
    for chapter_name, chapter_info in CHAPTERS.items():
        folder_name = chapter_info['folder']
        chapter_id = chapter_info['id']
        chapter_path = os.path.join(BASE_PATH, folder_name)
        print(f"\nProcessing: {chapter_name}")

        # Load flashcards
        flashcards_path = os.path.join(chapter_path, 'flashcards.json')
        if os.path.exists(flashcards_path):
            data = load_json(flashcards_path)
            for card in data.get('cards', []):
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

        # Load teljes.md from media folder
        teljes_path = os.path.join(MEDIA_PATH, chapter_id, 'teljes.md')
        if os.path.exists(teljes_path):
            content = load_markdown(teljes_path)
            sections = split_markdown_into_sections(content, chapter_name)
            for section in sections:
                all_items.append({
                    'type': 'markdown',
                    'chapter': chapter_name,
                    'id': section['id'],
                    'title': section['title'],
                    'content': section['content'],
                    'text': section['text']
                })
            print(f"  - {len(sections)} markdown sections")

    print(f"\nTotal items: {len(all_items)}")
    print("Generating embeddings...")

    # Generate embeddings in batches
    texts = [item['text'] for item in all_items]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    # Add embeddings to items and remove the full text (to save space)
    for i, item in enumerate(all_items):
        item['embedding'] = embeddings[i].tolist()
        del item['text']

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
