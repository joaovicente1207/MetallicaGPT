# train a miniature metallica model
# good for debugging and playing on macbooks and such

out_dir = 'out-metallica'
eval_interval = 50 # keep frequent because we'll overfit
eval_iters = 25
log_interval = 5 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'metallica'
wandb_run_name = 'mini-gpt'

dataset = 'metallica'
batch_size = 24
block_size = 32

# tiny GPT model :)
n_layer = 4
n_head = 4
n_embd = 64
dropout = 0.0

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 1000
lr_decay_iters = 1000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 20 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model
