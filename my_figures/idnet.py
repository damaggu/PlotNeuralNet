
import sys

from pycore.blocks import block_2ConvPool, block_Res

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    # to_input('./primate.jpg'),
    to_Pool(name="pool_b1", offset="(0,0,0)", to="(pool1-east)", width=1, height=32, depth=32, opacity=0.5),
    # *block_Res(name='b4', num=3, botton='pool_b1', top='pool_b4', s_filer=64, n_filer=512, offset="(1,0,0)",
    #                  size=(16, 16, 5.5), opacity=0.5),
    # to_Conv_mine("pool1", offset="(0,0,0)", to="(pool1-east)", width=70, caption="BACKBONE (Resnet)"),
    to_SoftMax_mine("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    # to_connection("pool_b4", "soft1"),
    to_end()
    ]

def main():
    to_generate(arch, './idnet.tex')

if __name__ == '__main__':
    main()
