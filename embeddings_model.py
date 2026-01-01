import open_clip
import pandas as pd
import torch
from IPython.display import display
from PIL import Image
from tqdm import tqdm

from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
model.eval()

tokenizer = open_clip.get_tokenizer('ViT-B-32')


def get_embedding(row):
    emoji_name, suffix = row["name"], row.suffix
    if suffix == 'gif':
        return torch.zeros([1, 512])

    image_path = SCRIPT_DIR / 'embeddings' / 'emojis' / f'{emoji_name}.{suffix}'
    image = preprocess(Image.open(image_path)).unsqueeze(0)
    text = tokenizer([emoji_name])

    with torch.no_grad(), torch.autocast("cuda"):
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        emoji_embedding = 0.5*image_features + 0.5*text_features
        emoji_embedding /= emoji_embedding.norm(dim=-1, keepdim=True)

        emoji_embedding.cpu()

    return emoji_embedding


def get_embeddings():
    df = pd.read_csv(SCRIPT_DIR / 'embeddings' / 'emojis' / 'emojis.csv')

    embeddings = []
    for idx, row in tqdm(list(df.iterrows())):
        embedding = get_embedding(row)
        embeddings.append(embedding)

    embeddings = torch.cat(embeddings)
    return embeddings


def get_text_embedding(emoji_name):
    text = tokenizer([emoji_name])

    with torch.no_grad(), torch.autocast("cuda"):
        text_embedding = model.encode_text(text)
        text_embedding /= text_embedding.norm(dim=-1, keepdim=True)
        text_embedding.cpu()

    return text_embedding


def get_scores(query_embedding, embeddings):
    scores = embeddings @ query_embedding.T
    return scores.flatten()


def get_sorted_idxs(scores):
    sorted_idxs = torch.argsort(scores.flatten(), descending=True)
    sorted_idxs = sorted_idxs.cpu().numpy()
    return sorted_idxs


def get_emojis(query):
    embeddings = get_embeddings()
    query_embedding = get_text_embedding(query)
    scores = get_scores(query_embedding, embeddings)
    sorted_idxs = get_sorted_idxs(scores)

    df = pd.read_csv(SCRIPT_DIR / 'embeddings' / 'emojis' / 'emojis.csv')

    emoji_names = df["name"].iloc[sorted_idxs].head().tolist()

    return emoji_names


if __name__ == '__main__':
    emojis = get_emojis('cat')
    for emoji in emojis:
        print(emoji)

