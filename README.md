# hasDID.io Chia NFT

Generate and publish NFT to Chia blockchain.

Uses Apophysis color scheme: 113_rw_multi_colors_6

## Generate

python gen.py -i scotopic;
python gen.py -r scotopic;
python gen.py -gm scotopic scotopic chia:did:wowza https://hasDID.io/assets/meta/scotopic.flam3

## Setup

python3 -m venv nftvenv
. nftvenv/bin/activate
pip install -r requirements.txt
mkdir _dep;pushd _dep;git clone https://github.com/scottdraves/flam3.git;pushd flam3;./configure;make;popd;popd;

cp -f setup-apophysis/vidres.flam3 _dep/flam3/


### Activate environment
. nftvenv/bin/activate


