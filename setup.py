# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup


with open("esm/version.py") as infile:
    exec(infile.read())

with open("README.md") as f:
    readme = f.read()

extras = {
    "esmfold": [ # OpenFold does not automatically pip install requirements, so we add them here.
        "biopython",
        "deepspeed==0.5.9",
        "dm-tree",
        "pytorch-lightning",
        "omegaconf",
        "ml-collections",
        "einops",
        "scipy",
    ]
}

setup(
    name="fair-esm",
    version=version,
    description="Evolutionary Scale Modeling (esm): Pretrained language models for proteins. From Facebook AI Research.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Facebook AI Research",
    url="https://github.com/facebookresearch/esm",
    license="MIT",
    packages=["esm", "esm/model", "esm/inverse_folding", "esm/esmfold/v1"],
    #JO: added for hydrogen addition
    package_data={
        "esm": [
            "esmfold/v1/*.lib",  # 确保 amino12.lib 被包含
            "esmfold/v1/*.pkl",  # 以防其他非 Python 文件丢失
            "esmfold/v1/*.dat",
            "esmfold/v1/*.ff14SB",
            "esmfold/v1/ens_models/*.pt",
        ]
    },
    extras_require=extras,
    data_files=[("source_docs/esm", ["LICENSE", "README.md", "CODE_OF_CONDUCT.rst"])],
    zip_safe=True,
)
