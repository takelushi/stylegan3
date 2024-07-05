# work

## 2024/07/04

お試し

```sh
rye sync
.\.venv\Scripts\activate
$Env:CUDA_HOME="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.5"

# トレーニング済モデルで画像生成
python gen_images.py --outdir=out --trunc=1 --seeds=2 --network=https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-afhqv2-512x512.pkl

# トレーニング済モデルで動画を生成
python gen_video.py --output=lerp.mp4 --trunc=1 --seeds=0-31 --grid=4x2 --network=https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-afhqv2-512x512.pkl

# ビジュアライザーの起動
python visualizer.py
```

## 2024/07/05

学習に挑戦する

```sh
# ポケモンの画像を data/pokemon に配置
# https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types

# prepare_pokemon.py を実装し、実行
python prepare_pokemon.py

# データセット作成
python dataset_tool.py --source=data/pokemon_no_alpha --dest=data/pokemon_no_alpha/data.zip

# 学習s
python train.py --outdir=~/training-runs --cfg=stylegan3-t --data=data/pokemon_no_alpha/data.zip --gpus=1 --batch=32 --gamma=8.2 --mirror=1
python train.py --outdir=~/training-runs --cfg=stylegan3-t --data=data/pokemon_no_alpha/data.zip --gpus=1 --batch=32 --gamma=8.2

```
