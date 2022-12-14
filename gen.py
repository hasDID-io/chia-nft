import json
import asyncio
import os
import argparse
import sys

# https://pypi.org/project/defusedxml/
# import xml.etree.ElementTree as ET
import defusedxml.ElementTree as ET

PROJECT_NAME=""
FLAM3_DIR="_dep/flam3"
OUTPUT_DIR="_generated"
METADATA_LATEST_FILE_NAME="_latest_metadata.json"
METADATA_LATEST_FILE_PATH=OUTPUT_DIR + "/" + METADATA_LATEST_FILE_NAME

# def get_new_nft_number():
#
#     with open(METADATA_LATEST_FILE_PATH) as file1:
#         last_known_metadata = json.load(file1)
#
#     token=last_known_metadata["fa"][0]["tokens"][0]
#     last_known_token_id = token["token_id"]
#
#     new_nft_number = int(last_known_token_id) + 1
#     new_nft_number_string = str(new_nft_number).zfill(4)
#     return new_nft_number_string

def render_images(file_name):
    
    # os.system(f'env out={OUTPUT_DIR}/{PROJECT_NAME}-{nft_num_string}.png qs=40 ss=4 {FLAM3_DIR}/flam3-render < {OUTPUT_DIR}/{PROJECT_NAME}-{nft_num_string}.flam3;')
    os.system(f'env out={OUTPUT_DIR}/{file_name}.png qs=20 ss=2 {FLAM3_DIR}/flam3-render < {OUTPUT_DIR}/{file_name}.flam3')
    os.system(f'open {OUTPUT_DIR}')
    
def generate_nft(file_name):
    
    # nft_num = nft_num_string
    file_name = f"{OUTPUT_DIR}/{file_name}"
    output_flam3 = f"{file_name}.flam3"
    output_png = f"{file_name}.png"
    
    
    generate_cmd = f"env template={FLAM3_DIR}/vidres.flam3 repeat=1 {FLAM3_DIR}/flam3-genome > {output_flam3};"
    # center_cmd = f"sed -i '' 's/center=\".*\" scale=\".*\" rotate/center=\"0.0 0.0\" scale=\"50.0\" rotate/' {OUTPUT_DIR}/{PROJECT_NAME}-{nft_num}.flam3;"
    
    # STEP 1
    os.system(generate_cmd)
    
    with open(output_flam3) as file:
        tree = ET.parse(file)
        root = tree.getroot()
        # print('\n')
        # print('----1-----')
        # print(len(root))
        # print('----2-----')
        # print(root[0])
        # print('----3-----')
        # for child in root:
        #     print(child.tag)
        # print('----4-----')
        # print(root[0][0])
        # print('----5-----')
        # print(root.tag)
        # print('----6-----')
        # print(root.attrib)
        # print('----7-----')
        for flame in root:
            # print(flame.tag, flame.attrib)
            
            flame.attrib['center'] = '0.0 0.0'
            flame.attrib['scale'] = '60.0'
            
        for color in flame.findall('color'):
            flame.remove(color)
        
        
        blue_yellow_colors = ET.fromstring(
"""
    <palette count="256" format="RGB">
       FF8040FF9C6CFFAF89FFC2A6E3A690C88A7ABA7C6FAD6E64
       804040905454A16868B78282CD9C9CA1B18875C7745FD16A
       49DC6100FF4025FF5C4BFF7870FF9496FFB0A2FFB9AEFFC2
       9AAD6F8D76378040009B5815B7712BC47D35D28940EDA156
       FFB1649165A75A3FC82419E9241EF42424FF3636FF4848FF
       A8A8FFBA9FFFCD97FFE08EFFF386FFF983FFFF80FFF664F6
       EE49EEDD12DDD509D5CD00CDC300C3B900B9B000B0A800A8
       6037B23C52B7186EBD177FC51791CE2299D42EA2DB46B3E9
       5DC4F655B7E63D9ECD2686B413729F005E8A217AA34395BC
       85CCEF7FCBDB7ACAC858B59137A15B26973F168D24008000
       039B0308D20818E81828FF2835FF3543FF435EFF5E78FF78
       6CE26C4EC54E31A931229A22138C13007900377B0E6E7C1C
       A47E29FF7734FF6E27FF661BFF6114FF5D0EFF5706FF6D26
       FF9866FFAA80FFBC9BF8AE8AF1A17AE48658D66B37BF3F00
       CD612BE8A482EFB498F6C5AEFFDBCAEAB79FD59373C06F48
       9D3300A3480BAA5D17AD671DB17223BC9436C29C44C8A452
       CEAC5FD8BA76DABF7FDDC489E3CD9BE8D7AEF1E7CDF4D1CA
       FAA5C5FC92C2FF80C0FF7ABDFF74BAFF67B4FF5BADFF4EA7
       FF46A3FF2E97FF2894FF2391FF0F87F40C80E90979DE0572
       CC0066C70063C20061B8005CAE0057A400529D004F96004C
       8F00487D003F8B1B4699374DB56E5BD1A469EDDB77FFFF80
       91D28A76C78C5BBC8F24A6940097970092AD008DC40088DA
       0080FF2A8FC8549D917EAC5BA8BA24C4C400BDBD00B6B600
       A8A800A6A600A4A4009B9B00929200888800797900918536
       A9916CC19DA2D8A9D9E8B1FCDF96FBD77AFACE5EF9C643F8
       C031F7AA28DD951EC27F15A85B057C7A2C989954B3B87BCE
       D7A2EAEBBCFCB9B7D786B2B354AD8E21A76A00A45222B86D
       43CB8765DFA29DFFCE7BFABA5AF4A738EF9316EA8000E673
       0AEB7B14F1821EF68A28FB922FFF9725E1831BC46F11A65B
       00753A29935E53B0817CCEA5A6ECC9C1FFE0B3C8BEA5919B
       975B79892456800040960864AD0F88C317ACE824E8E527D2
       E329BCE02CA6DE2E90DC3082E3589AEA7FB2F1A7CAFCE9F2
    </palette>
""")
        flame.append(blue_yellow_colors)
        
        tree.write(output_flam3)
            
    
    # print('\n')
    render_cmd = f"env out={output_png} {FLAM3_DIR}/flam3-render < {output_flam3}"
    
    # STEP 3
    # os.system(center_cmd)
    os.system(render_cmd)
    
    os.system(f'open {OUTPUT_DIR}')

def add_text(text_display_on_bottom, file_name):
    # env out={OUTPUT_DIR}/{PROJECT_NAME}-{nft_num_string}-social.png qs=20 ss=2 {FLAM3_DIR}/flam3-render < {OUTPUT_DIR}/{PROJECT_NAME}-{nft_num_string}.flam3
    os.system(f'convert {OUTPUT_DIR}/{file_name}.png -undercolor black -gravity south -fill gray -pointsize 16 -annotate +0+10 "{text_display_on_bottom}" {OUTPUT_DIR}/{file_name}.png')

def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))
        
def gen_nft_metadata(nickname, twitter_handle, chia_did, nft_image_src_url):
    '''
     * profile image?!?! - maybe enforce IPFS url OR use the generated image?
     * Dexie also parses twitter profiles for DIDs
     * How to do an array of metadata?
    '''
    import datetime
    date_now = datetime.datetime.now()
    
    nft_date_created = date_now
    nft_date_expiration = add_years(nft_date_created, 1)
    
    meta = {
      "format": "CHIP-0007",
      "name": f"{nickname}.hasDID.io",
      "description": "Creator profile generated with https://hasDID.io",
      "sensitive_content": False,
      "attributes": [
        {
          "trait_type": "generation",
          "value": 0
        },
        {
          "trait_type": "date_created",
          "value": f"{nft_date_created}"
        },
        {
          "trait_type": "date_expiration",
          "value": f"{nft_date_expiration}"
        },
        {
          "trait_type": "chia_did",
          "value": f"{chia_did}"
        },
        {
          "trait_type": "nickname",
          "value": f"{nickname}"
        },
        {
          "trait_type": "twitter_handle",
          "value": f"{twitter_handle}"
        },
        {
          "trait_type": "hasdid_profile_url",
          "value": f"https://{nickname}.hasDID.io"
        },
        {
          "trait_type": "hasdid_profile_image_src_url",
          "value": f"{nft_image_src_url}"
        },
      ],
      "collection": {
        "name": "hasDID.io",
        "id": "57F2EF18-66A8-407E-9B52-3D1649FC7135",
        "attributes": [
          {
            "type": "description",
            "value": "Creator profile generated with https://hasDID.io"
          },
          {
              "type": "icon",
              "value": "https://hasDID.io/assets/img/thumb.png"
          },
          {
              "type": "banner",
              "value": "https://hasDID.io/assets/img/banner.png"
          },
          {
            "type": "twitter",
            "value": "@hasDID_io"
          },
          {
            "type": "website",
            "value": "https://hasDID.io"
          }
        ]
      }
    }
    
    fname = f"{nickname}.json"
    with open(f"{OUTPUT_DIR}/" + fname, 'w') as outfile:
        json.dump(meta, outfile, sort_keys=False, indent=4)

def gen_nft_metadata_validate(nft_metadata_path):
    # https://www.jsonschemavalidator.net/s/0Aw7Bmlb
    print("do this")

def gen_nft_rpc_metadata():
    print("do this")


def get_args():
    
    parser = argparse.ArgumentParser(description='Generate FLAM3 artwork.')
    
    # parser.add_argument('-m', '--generate-loop', action='store_true', required=False, help='Generate art continuously + increment the numbers')
    parser.add_argument('-i', '--generate-index', metavar="NICKNAME", nargs="+", required=False, help='Index of art piece to generate')
    parser.add_argument('-r', '--render-index', metavar="NICKNAME", nargs="+", required=False, help='Index of art piece to render')
    parser.add_argument('-gm', '--generate-metadata', metavar=('NICKNAME', 'TWITTER_HANDLE', 'CHIA_DID', 'NFT_IMAGE_SRC_URL'), nargs=4, required=False, help='Generate NFT metadata.')
    
    if len(sys.argv) < 2:
        # parser.print_usage()
        parser.print_help()
        sys.exit(1)
    
    return parser.parse_args()

ARGS = get_args()

async def main():
    
    # if ARGS.generate_loop:
    #     print('todo')
    if ARGS.generate_index:
        nickname = ARGS.generate_index[0]
        generate_nft(nickname)
        add_text(f"{nickname}.hasDID.io", nickname)
    elif ARGS.render_index:
        nickname = ARGS.render_index[0]
        render_images(nickname)
        add_text(f"{nickname}.hasDID.io", nickname)
    elif ARGS.generate_metadata:
        nickname = ARGS.generate_metadata[0]
        twitter_profile = ARGS.generate_metadata[1]
        chia_did = ARGS.generate_metadata[2]
        nft_image_src_url = ARGS.generate_metadata[3]
        gen_nft_metadata(nickname, twitter_profile, chia_did, nft_image_src_url)
        
    # else:
    #     nft_num_string = get_new_nft_number()
    #     generate_nft(nft_num_string)
        # render_images(nft_num_string)


asyncio.run(main())