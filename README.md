
# MetallicaGPT

Train and create new lyrics like a Metallica songs.
This code is based on nanoGPT, read the original README from https://github.com/karpathy/nanoGPT for more details.
Special thanks for Karpathy for the bests lessons that I ever seen about Backpropagation and Transformers.

## install

Dependencies:

- [pytorch](https://pytorch.org) <3
- [numpy](https://numpy.org/install/) <3
- `pip install tiktoken` for OpenAI's fast BPE code <3
- `pip install wandb` for optional logging <3
- `pip install tqdm`


## training

Download the dataset on https://huggingface.co/huggingartists/metallica and puts on `./data/metallica`.
Run
```
$ python /data/metallica/prepare.py
```
for prepare the dataset to training. 

In `./config/train_metallica.py` you can edit the training setup. 

Now, just run:
```
$ python train.py config/train_metallica.py
```

## inference

You can edit the start string, generate more than one sample by inference and apply the max number of tokens that it will generate. 
```
$ python sample.py --out_dir=out-metallica --start="Am I alive?" --num_samples=1 --max_new_tokens=100 --seed=1997
```


