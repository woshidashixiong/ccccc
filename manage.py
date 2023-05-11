用conda install 还是pip install好？

依赖数据库
conda install：依赖于 anaconda 数据库https://www.anaconda.com/和 bioconda 数据库https://bioconda.github.io/
pip install：依赖于 PyPI 数据库 https://pypi.org/
    
安装范围
conda install 的安装范围不仅仅局限于 python package，还能安装通用 linux 软件，gcc 库等。
但 conda install 所能安装的 python package 数量要远远少于 pip install。
pip install：绝大多数的 python package 都可以通过 pip install packagename 命令直接安装。

安装方式优先级
conda install package 和 pip install package 这两种方式优先使用哪一种都没关系，
但需要考虑避免重复安装，优先使用哪种就要一直保持，
不能这次安装 package A 用 conda install 方式，下次安装 package B 用 pip install，如果经常这样安装 package 在以后调用的时候很可能报错。

个人推荐优先使用pip install,亲测稳定不易出错，特别是多个包有依赖安装的时候,并且包多还全，实在pip搞不定在用conda试试，最好一直保持用pip
