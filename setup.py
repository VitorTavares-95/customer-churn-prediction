from setuptools import setup, find_packages

setup(
    name='customer-churn-prediction',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'xgboost',
        'tensorflow',
        'sqlalchemy',
        'psycopg2',
        'jupyter',
        'plotly',
        'dash'
    ],
    entry_points={
        'console_scripts': [
            # 'your-command=your_module:main_function'
        ]
    },
)
