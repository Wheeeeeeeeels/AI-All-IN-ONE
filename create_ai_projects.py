import os
import shutil
from pathlib import Path

def create_directory_structure(base_path, structure_dict):
    for key, value in structure_dict.items():
        current_path = os.path.join(base_path, key)
        if isinstance(value, dict):
            os.makedirs(current_path, exist_ok=True)
            create_directory_structure(current_path, value)
        else:
            Path(current_path).touch()

def create_readme(path, content):
    with open(os.path.join(path, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(content)

def create_requirements(path, requirements):
    with open(os.path.join(path, 'requirements.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(requirements))

def create_init_files(directory):
    for root, dirs, files in os.walk(directory):
        if '__pycache__' not in root:
            init_file = os.path.join(root, '__init__.py')
            if not os.path.exists(init_file):
                Path(init_file).touch()

def create_all_projects():
    # 所有项目的结构定义
    projects = {
        'ml-framework': {
            'src': {
                'algorithms': {
                    'supervised': {
                        'linear_models': {},
                        'tree_models': {},
                        'svm': {}
                    },
                    'unsupervised': {
                        'clustering': {},
                        'dimensionality_reduction': {}
                    },
                    'ensemble': {}
                },
                'core': {
                    'data': {},
                    'metrics': {},
                    'preprocessing': {}
                },
                'utils': {}
            },
            'tests': {},
            'examples': {},
            'docs': {}
        },
        'dl-framework': {
            'src': {
                'nn': {
                    'layers': {},
                    'models': {},
                    'functional': {}
                },
                'optim': {},
                'data': {},
                'loss': {},
                'utils': {}
            },
            'tests': {},
            'examples': {
                'mnist': {},
                'cifar': {},
                'custom': {}
            },
            'docs': {}
        },
        'llm-framework': {
            'src': {
                'models': {
                    'architecture': {},
                    'embedding': {},
                    'variants': {}
                },
                'training': {},
                'tokenizer': {},
                'inference': {},
                'memory': {},
                'utils': {}
            },
            'tests': {},
            'examples': {
                'pretraining': {},
                'finetuning': {},
                'inference': {}
            },
            'docs': {}
        },
        'nlp-algorithms': {
            'src': {
                'text_processing': {'tokenization': {}, 'segmentation': {}, 'normalization': {}},
                'language_models': {'ngram': {}, 'neural_lm': {}, 'contextual_lm': {}},
                'embeddings': {'word2vec': {}, 'glove': {}, 'bert': {}},
                'sequence_labeling': {'pos_tagging': {}, 'ner': {}, 'chunking': {}},
                'text_classification': {},
                'machine_translation': {},
                'question_answering': {},
                'summarization': {},
                'sentiment_analysis': {}
            },
            'docs': {'api': {}, 'tutorials': {}, 'examples': {}},
            'tests': {}
        },
        'cv-algorithms': {
            'src': {
                'image_processing': {'filters': {}, 'transformations': {}, 'enhancement': {}},
                'feature_detection': {'corners': {}, 'edges': {}, 'descriptors': {}},
                'object_detection': {'rcnn': {}, 'yolo': {}, 'ssd': {}},
                'segmentation': {'semantic': {}, 'instance': {}},
                'recognition': {'face': {}, 'pattern': {}},
                'tracking': {}
            },
            'docs': {'api': {}, 'tutorials': {}, 'examples': {}},
            'tests': {}
        },
        'slam-algorithms': {
            'src': {
                'frontend': {'feature_detection': {}, 'feature_matching': {}, 'motion_estimation': {}},
                'backend': {'optimization': {}, 'graph': {}, 'loop_closure': {}},
                'mapping': {'point_cloud': {}, 'occupancy_grid': {}, 'mesh_generation': {}},
                'sensors': {'camera': {}, 'lidar': {}, 'imu': {}},
                'visualization': {}
            },
            'docs': {'api': {}, 'tutorials': {}, 'examples': {}},
            'tests': {}
        },
        'rl-algorithms': {
            'src': {
                'value_based': {'q_learning': {}, 'dqn': {}, 'double_dqn': {}},
                'policy_based': {'reinforce': {}, 'a2c': {}, 'ppo': {}},
                'model_based': {'planning': {}, 'world_models': {}},
                'multi_agent': {},
                'environments': {'custom': {}, 'wrappers': {}},
                'utils': {}
            },
            'docs': {'api': {}, 'tutorials': {}, 'examples': {}},
            'tests': {}
        }
    }

    # 基础依赖
    base_requirements = [
        'numpy>=1.21.0',
        'scipy>=1.7.0',
        'pandas>=1.3.0',
        'matplotlib>=3.4.0',
        'torch>=1.9.0',
        'scikit-learn>=0.24.0'
    ]

    # 项目特定依赖
    project_requirements = {
        'ml-framework': base_requirements + [
            'scikit-learn>=1.0.0',
            'xgboost>=1.5.0',
            'lightgbm>=3.3.0'
        ],
        'dl-framework': base_requirements + [
            'torch>=1.9.0',
            'torchvision>=0.10.0',
            'tqdm>=4.62.0'
        ],
        'llm-framework': base_requirements + [
            'transformers>=4.5.0',
            'tokenizers>=0.10.0',
            'accelerate>=0.5.0'
        ],
        'nlp-algorithms': base_requirements + [
            'transformers>=4.5.0',
            'nltk>=3.6.0',
            'spacy>=3.0.0',
            'gensim>=4.0.0'
        ],
        'cv-algorithms': base_requirements + [
            'opencv-python>=4.5.0',
            'pillow>=8.0.0',
            'albumentations>=1.0.0'
        ],
        'slam-algorithms': base_requirements + [
            'opencv-python>=4.5.0',
            'open3d>=0.13.0',
            'pangolin>=0.5.0',
            'g2o>=1.0.0'
        ],
        'rl-algorithms': base_requirements + [
            'gym>=0.19.0',
            'stable-baselines3>=1.0.0',
            'tensorboard>=2.6.0'
        ]
    }

    # 创建主项目目录
    root_dir = "ai-frameworks-and-algorithms"
    os.makedirs(root_dir, exist_ok=True)

    # 创建项目
    for project_name, structure in projects.items():
        print(f"正在创建项目: {project_name}")
        project_path = os.path.join(root_dir, project_name)
        
        # 创建目录结构
        create_directory_structure(project_path, structure)
        
        # 创建 __init__.py 文件
        create_init_files(project_path)
        
        # 创建 README
        readme_content = f"""# {project_name}

## 简介
这是{project_name}项目，实现了相关的算法和功能。

## 安装
```bash
pip install -r requirements.txt
```

## 项目结构
```
{project_name}/
├── src/         # 源代码
├── docs/        # 文档
├── tests/       # 测试
└── requirements.txt
```

## 使用方法
请参考 docs 目录下的文档和示例。

## 贡献指南
欢迎提交 Pull Request。

## 许可证
MIT License"""

        create_readme(project_path, readme_content)

if __name__ == "__main__":
    create_all_projects()