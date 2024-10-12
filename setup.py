
### 2. `setup.py`Este arquivo é necessário para empacotar e distribuir o seu pacote. Ele contém as informações do pacote e as dependências.

from setuptools import setup, find_packages

setup(
    name='meu_pacote',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Biblioteca para manipulação de imagens
    ],
    description='Um pacote simples de processamento de imagens',
    author='Seu Nome',
    author_email='seu.email@exemplo.com',
    url='https://github.com/seuusuario/meu_pacote',
)
