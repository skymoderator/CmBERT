# CmBERT

## Introduction
CmBERT stands for Commit BERT, which is a pre-trained language model for commit messages. It is trained on CodeSearchNet dataset and a self-crawled dataset from top 100 popular GitHub repositories.

Models are trained on two stages. First stage involves training on CodeSearchNet dataset. Second stage involves training on self-crawled dataset. 

## Usage
Examples scripts are provided in [Notebook](plot/probe.ipynb)
```shell
added = "def add(a, b): return a + b"
deleted = "def sub(a, b): return a - b"
run_model(added, deleted)
>>> change sub to add
```

## Pre-trained Model
Six different programming languages are supported, namely: Python, Java, JavaScript, Go, PHP, Ruby. The pre-trained models for both stages can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1RCmKPYywGI3hoJlGxxX7q4vTOxCiGfaZ?usp=sharing).

### First Stage
| Language | Weight (Best Perplexity) | Weight (Best BLEU score) |
| --- | --- | --- |
| Python | [Link](https://drive.google.com/file/d/1Jb9j_WD7b8NkvbgoDLD3ZJwFc_PVbV70/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1XPjSIspZjI_C2tpCQsQFE1SyFC7x-2jj/view?usp=drive_link) |
| Java | [Link](https://drive.google.com/file/d/1Xi5WgqFdDl4bXa5r6Y3FMcspyIvC2NDi/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1DZWg1PH8R25527cJBdc3CfptwXbSwny1/view?usp=drive_link) |
| JavaScript | [Link](https://drive.google.com/file/d/1Bc0rYXXKABxuGeYHLPTEE8ox0cwZJEft/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1piMbFLS4FIvOQVqmPr4ONGJKG0KOzdKv/view?usp=drive_link) |
| Go | [Link](https://drive.google.com/file/d/1dJVyPOG3XAAsg0nx28Ou7_gUsg3BOOy9/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1ZUmrN0tMY1VTdlFUkyIvXGM2NPSLULA5/view?usp=drive_link) |
| PHP | [Link](https://drive.google.com/file/d/1NsikXprwS4oN3QNSWYhGHHOso5Jej8GB/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1tcy0Zpyu3-Dwg8yeBHA8HeSAr-IpCTH3/view?usp=drive_link) |
| Ruby | [Link](https://drive.google.com/file/d/1URoTrIlguyzU314yxHJTI3iT-Wd4gqt-/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1aGMdQqXrdBaWRgNsD7MOug_hhL3gjZ59/view?usp=drive_link) |

### Second Stage
| Language | Weight (Best Perplexity) | Weight (Best BLEU score) |
| --- | --- | --- |
| Python | [Link](https://drive.google.com/file/d/1NCSpWgG3idUk1TEkrTD0N8lZ2-QORQHa/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1kJlPkTdIjBJI1VfIzSMr030JMHgjzrBK/view?usp=drive_link) |
| Java | [Link](https://drive.google.com/file/d/1Xi5WgqFdDl4bXa5r6Y3FMcspyIvC2NDi/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1DZWg1PH8R25527cJBdc3CfptwXbSwny1/view?usp=drive_link) |
| JavaScript | [Link](https://drive.google.com/file/d/1JqOcyeKwoFDlW2UNhha-dmBQVNZ34Hk0/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1G84OzzZyT1VsD01dNsVHDuM2hHe5D7MQ/view?usp=drive_link) |
| Go | [Link](https://drive.google.com/file/d/1jDRKBUrH_3ZKNZ6snVIFJyhoNWcqncyJ/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1628pGGl7RsBjiMaEcQStGM_tAaTjsRmA/view?usp=drive_link)
| PHP | [Link](https://drive.google.com/file/d/1CJeOHOAO5_7Ax24CezIElpVOyyacT306/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1k9kAWDNjr4FyfmbYqnuPkerKqpG3lLeZ/view?usp=drive_link) |
| Ruby | [Link](https://drive.google.com/file/d/1abWTwNRZ70jjnAV_noRnRA71zaLa6muj/view?usp=drive_link) | [Link](https://drive.google.com/file/d/1DxLpZFC3C8Gz41vHLkUpCO5A0Ti176Af/view?usp=drive_link)

## Side Note
CmBERT is built for pure academic purpose, thus performance is not guaranteed. You are welcome to built upon it and improve it. 