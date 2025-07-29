from setuptools import setup, find_packages

setup(
    name="ai_desire_bot",
    version="0.1.0",
    author="林柏毅",
    description="一個支援角色扮演與語音功能的色情 AI 聊天機器人",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "transformers>=4.36.2",
        "torch>=2.1.0",
        "llama-cpp-python>=0.2.24",
        "safetensors>=0.3.1",
        "pyyaml>=6.0",
        "flask>=2.3.3",
        "edge-tts>=6.1.10",
        "soundfile>=0.12.1",
        "numpy>=1.25.2",
        "scipy>=1.11.3",
        "tqdm>=4.66.1",
        "colorama>=0.4.6",
    ],
    python_requires=">=3.10",
)
