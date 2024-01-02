import json
import transformers
from tqdm import tqdm
import re


class Example(object):
    """A single training/test example."""

    def __init__(
        self,
        idx,
        source,
        target,
    ):
        self.idx = idx
        self.source = source
        self.target = target


def read_code_search_net(filename):
    """Read examples from filename."""
    examples = []
    with open(filename, encoding="utf-8") as f:
        examples = [
            Example(
                idx=j["idx"] if "idx" in j else index,
                source=" ".join(
                    " ".join(j["code_tokens"]).replace("\n", "").strip().split()
                ),
                target=" ".join(
                    " ".join(j["docstring_tokens"]).replace("\n", "").strip().split()
                ),
            )
            for index, line in tqdm(enumerate(f))
            if (j := json.loads(line.strip()))
        ]
    return examples


def read_top100(tokenizer, filename):
    """Read examples from filename."""
    examples = []

    def process_fn(json, split):
        return re.sub("[Ġ]{2,}", "", "".join(json[split])).replace("Ġ", " ")

    with open(filename, encoding="utf-8") as f:
        examples = [
            Example(
                idx=j["idx"] if "idx" in j else index,
                source=process_fn(json=j, split="added")
                + tokenizer.sep_token
                + process_fn(json=j, split="deleted"),
                target=process_fn(json=j, split="msg"),
            )
            for index, line in tqdm(enumerate(f))
            if (j := json.loads(line.strip()))
        ]
    return examples


def convert_examples_to_features(examples, tokenizer, args, stage=None):
    max_source_length = min(args.max_source_length, tokenizer.model_max_length)
    max_target_length = min(args.max_target_length, tokenizer.model_max_length)
    # hack to avoid tokenizer warning
    old_level = transformers.logging.get_verbosity()
    transformers.logging.set_verbosity_error()
    source_batch_encodings = tokenizer(
        text=[e.source for e in examples],
        max_length=max_source_length,
        padding="max_length",
        truncation="longest_first",
        return_tensors="pt",
    )
    target_batch_encodings = tokenizer(
        text=[e.target for e in examples] if stage != "test" else "None",
        max_length=max_target_length,
        padding="max_length",
        truncation="longest_first",
        return_tensors="pt",
    )
    transformers.logging.set_verbosity(old_level)
    return (
        source_batch_encodings["input_ids"],
        source_batch_encodings["attention_mask"],
        target_batch_encodings["input_ids"],
        target_batch_encodings["attention_mask"],
    )
