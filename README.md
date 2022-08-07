# hasDID.io Chia NFT

Generate and publish NFT to Chia blockchain.

Uses Apophysis color scheme: 113_rw_multi_colors_6

## Generate

NICKNAME="vital"
python gen.py -i $NICKNAME;
python gen.py -r $NICKNAME;
python gen.py -gm $NICKNAME $NICKNAME chia:did:wowza https://hasDID.io/assets/meta/${NICKNAME}.flam3

## Setup

python3 -m venv nftvenv
. nftvenv/bin/activate
pip install -r requirements.txt
mkdir _dep;pushd _dep;git clone https://github.com/scottdraves/flam3.git;pushd flam3;./configure;make;popd;popd;

cp -f setup-apophysis/vidres.flam3 _dep/flam3/


### Activate environment
. nftvenv/bin/activate


