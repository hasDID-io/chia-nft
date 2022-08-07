# hasDID.io Chia NFT

Generate and publish NFT to Chia blockchain.

Uses Apophysis color scheme: 113_rw_multi_colors_6

## Generate

python gen.py -r 0000

NFTNUM=0000;NFTNAME=hasDID;env out=_generated/${NFTNAME}-${NFTNUM}.png _dep/flam3/flam3-render < _generated/${NFTNAME}-${NFTNUM}.flam3

for num in {01..24}
do
   NFTNUM=$(printf "%04d" $num);
   python gen.py -r $NFTNUM;
   sleep 1;
done


## Setup

python3 -m venv nftvenv
. nftvenv/bin/activate
pip install -r requirements.txt
mkdir _dep;pushd _dep;git clone https://github.com/scottdraves/flam3.git;pushd flam3;./configure;make;popd;popd;

cp -f setup-apophysis/vidres.flam3 _dep/flam3/


### Activate environment
. nftvenv/bin/activate


