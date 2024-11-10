from setuptools import setup, find_packages
setup(
      name="Jogo da velha",
      version="0.1",
      description="Jogo de tabuleiro",
      install_requires=["numpy","random"],
      packages=find_packages(),
)